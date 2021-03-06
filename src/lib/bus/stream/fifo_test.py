import unittest

from lib.bus.stream.fifo import UnbufferedAsyncStreamFIFO, BufferedAsyncStreamFIFO, UnbufferedSyncStreamFIFO, \
    BufferedSyncStreamFIFO
from lib.bus.stream.sim_util import write_to_stream, read_from_stream
from lib.bus.stream.stream import BasicStream
from util.sim import SimPlatform, do_nothing


class TestFifo(unittest.TestCase):
    def check_fifo_basic(self, fifo_generator):
        input = BasicStream(32)
        fifo = fifo_generator(input, 1024)

        def testbench():
            for i in range(10):
                yield from write_to_stream(input, payload=i)

            # async fifos need some time due to cdc
            yield from do_nothing()

            assert (yield fifo.r_level) == 10

            for i in range(10):
                assert (yield from read_from_stream(fifo.output)) == i, "read data doesnt match written data"

        platform = SimPlatform()
        platform.add_sim_clock("sync", 100e6)
        platform.sim(fifo, testbench)

    def test_sim_async_stream_fifo(self):
        fifo_gen = lambda input, depth: UnbufferedAsyncStreamFIFO(input, depth, o_domain="sync", i_domain="sync")
        self.check_fifo_basic(fifo_gen)

    def test_async_stream_fifo_buffered(self):
        fifo_gen = lambda input, depth: BufferedAsyncStreamFIFO(input, depth, o_domain="sync", i_domain="sync")
        self.check_fifo_basic(fifo_gen)

    def test_sync_stream_fifo(self):
        fifo_gen = lambda input, depth: UnbufferedSyncStreamFIFO(input, depth)
        self.check_fifo_basic(fifo_gen)

    def test_sync_stream_fifo_buffered(self):
        fifo_gen = lambda input, depth: BufferedSyncStreamFIFO(input, depth)
        self.check_fifo_basic(fifo_gen)
