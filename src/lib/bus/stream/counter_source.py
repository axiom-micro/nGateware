from nmigen import *

from lib.bus.stream.stream import BasicStream
from lib.peripherals.csr_bank import ControlSignal


class CounterStreamSource(Elaboratable):
    def __init__(self, width, count_if_not_ready=False):
        self.output = BasicStream(width, name="counter_stream")

        self.count_if_not_ready = ControlSignal(reset=count_if_not_ready)

    def elaborate(self, platform):
        m = Module()

        with m.If(self.output.ready | self.count_if_not_ready):
            m.d.comb += self.output.valid.eq(1)
            m.d.sync += self.output.payload.eq(self.output.payload + 1)

        return m
