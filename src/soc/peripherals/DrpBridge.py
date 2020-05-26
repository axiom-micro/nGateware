# TODO: add tests
# TODO: this seems to be broken

from nmigen import *

from soc import Response
from soc.SocPlatform import SocPlatform
from soc.memorymap import MemoryMap
from util.bundle import Bundle


class DrpInterface(Bundle):
    def __init__(self, DWE, DEN, DADDR, DI, DO, DRDY, DCLK):
        super().__init__()
        self.data_write_enable: Signal = DWE
        self.data_enable: Signal = DEN
        self.address: Signal = DADDR
        self.data_in: Signal = DI
        self.data_out: Signal = DO
        self.ready: Signal = DRDY
        self.clk : Signal = DCLK


class DrpBridge(Elaboratable):
    def __init__(self, drp_interface):
        """
        A bridge for the xilinx dynamic reconfiguration port. This is for example used in the Xilinx 7 series MMCM and
        PLL primitives.

        :param drp_interface: the drp interface of the drp slave
        """
        self.drp_interface: DrpInterface = drp_interface

    def elaborate(self, platform: SocPlatform):
        m = Module()

        def handle_read(m, addr, data, read_done):
            m.d.comb += self.drp_interface.clk.eq(ClockSignal())
            m.d.sync += self.drp_interface.address.eq(addr)
            m.d.sync += self.drp_interface.data_enable.eq(1)
            with m.If(self.drp_interface.ready):
                m.d.sync += self.drp_interface.data_enable.eq(0)
                m.d.sync += data.eq(self.drp_interface.data_out)
                read_done(Response.OK)

        def handle_write(m, addr, data, write_done):
            m.d.comb += self.drp_interface.clk.eq(ClockSignal())
            m.d.sync += self.drp_interface.address.eq(addr)
            m.d.sync += self.drp_interface.data_enable.eq(1)
            m.d.sync += self.drp_interface.data_write_enable.eq(1)
            m.d.sync += self.drp_interface.data_in.eq(data)
            with m.If(self.drp_interface.ready):
                m.d.sync += self.drp_interface.data_enable.eq(0)
                m.d.sync += self.drp_interface.data_write_enable.eq(0)
                write_done(Response.OK)

        memorymap = MemoryMap()
        memorymap.allocate("drp", writable=True, bits=2**self.drp_interface.address.width * 8)

        m.submodules += platform.BusSlave(
            handle_read=handle_read,
            handle_write=handle_write,
            memorymap=memorymap
        )

        return m
