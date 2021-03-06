from nmigen import *
from nmigen.lib.fifo import SyncFIFOBuffered

from lib.bus.stream.stream import BasicStream
from lib.peripherals.csr_bank import StatusSignal, ControlSignal
from util.nmigen_misc import with_reset
from .axi_endpoint import Response
from .util import get_axi_master_from_maybe_slave


class AxiReader(Elaboratable):
    def __init__(
            self,
            address_source: BasicStream,
            axi_slave=None, axi_data_width=64,
            last_fifo_depth=1024
    ):
        self.address_source = address_source
        self.axi_slave = axi_slave
        self.last_fifo_depth = last_fifo_depth

        self.flush = Signal()
        self.output = address_source.clone(name="buffer_reader_output_stream")
        self.output.payload = Signal(axi_data_width)

        self.allow_flush = ControlSignal(reset=1)
        self.force_flush = ControlSignal()
        self.limit_outstanding = ControlSignal(reset=bool(address_source.out_of_band_signals))
        self.max_outstanding = ControlSignal(32, reset=last_fifo_depth)
        self.flush_outstanding_timeout = ControlSignal(16, reset=1024)

        self.last_resp = StatusSignal(Response)
        self.error_count = StatusSignal(32)
        self.outstanding = StatusSignal(32)
        self.state = StatusSignal(2)
        self.timeouts = StatusSignal(32)

    def elaborate(self, platform):
        m = Module()

        axi = get_axi_master_from_maybe_slave(self.axi_slave, m, platform)
        assert len(self.output.payload) == axi.data_bits
        assert len(self.address_source.payload) == axi.addr_bits

        with m.If(self.force_flush):
            m.d.comb += axi.read_data.ready.eq(1)
        with m.Else():
            with m.FSM():
                def common():
                    m.d.comb += axi.read_address.valid.eq(self.address_source.valid)
                    m.d.comb += axi.read_address.payload.eq(self.address_source.payload)
                    m.d.comb += self.address_source.ready.eq(axi.read_address.ready)
                    m.d.comb += axi.read_address.burst_len.eq(0)  # we dont generate bursts

                    m.d.comb += axi.read_data.ready.eq(self.output.ready)
                    m.d.comb += self.output.valid.eq(axi.read_data.valid)
                    m.d.comb += self.output.payload.eq(axi.read_data.payload)

                    with m.If(self.flush & (self.outstanding > 1) & self.allow_flush):
                        m.next = "flush"

                timeout_counter = Signal.like(self.flush_outstanding_timeout)

                def timeout():
                    m.d.sync += timeout_counter.eq(timeout_counter + 1)
                    with m.If(timeout_counter == self.flush_outstanding_timeout):
                        m.d.sync += self.timeouts.eq(self.timeouts + 1)
                        m.d.sync += self.outstanding.eq(0)
                        m.next = "normal"

                with m.State("normal"):
                    m.d.comb += self.state.eq(0)
                    m.d.sync += timeout_counter.eq(0)
                    common()
                    with m.If((self.outstanding >= self.max_outstanding) & self.limit_outstanding):
                        m.next = "limit_outstanding"

                with m.State("limit_outstanding"):
                    m.d.comb += self.state.eq(1)
                    common()
                    m.d.comb += self.address_source.ready.eq(0)
                    timeout()
                    with m.If((self.outstanding < self.max_outstanding)):
                        m.next = "normal"

                with m.State("flush"):
                    m.d.comb += self.state.eq(2)
                    m.d.comb += axi.read_data.ready.eq(1)
                    timeout()
                    with m.If(self.outstanding == 0 & ~axi.read_data.ready):
                        m.next = "normal"

        m.d.sync += self.last_resp.eq(axi.read_data.resp)
        with m.If(axi.read_data.valid & (axi.read_data.resp != Response.OKAY)):
            m.d.sync += self.error_count.eq(self.error_count + 1)

        address_written = Signal()
        m.d.comb += address_written.eq(axi.read_address.valid & axi.read_address.ready)
        data_read = Signal()
        m.d.comb += data_read.eq(axi.read_data.valid & axi.read_data.ready)
        with m.If(address_written & ~data_read):
            m.d.sync += self.outstanding.eq(self.outstanding + 1)
        with m.Elif(data_read & ~address_written):
            with m.If(self.outstanding != 0):
                m.d.sync += self.outstanding.eq(self.outstanding - 1)

        if self.address_source.out_of_band_signals:
            last_fifo = m.submodules.last_fifo = with_reset(m, self.force_flush)(
                SyncFIFOBuffered(width=len(Cat(self.address_source.out_of_band_signals.values())), depth=self.last_fifo_depth)
            )
            # we dont have to check r_rdy and w_rdy because we are limiting the outstanding transaction to the fifo
            # size
            m.d.comb += last_fifo.w_en.eq(address_written)
            m.d.comb += last_fifo.w_data.eq(Cat(self.address_source.out_of_band_signals.values()))
            m.d.comb += last_fifo.r_en.eq(data_read)
            m.d.comb += Cat(self.output.out_of_band_signals.values()).eq(last_fifo.r_data)

        return m
