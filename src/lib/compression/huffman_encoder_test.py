import unittest
from collections import defaultdict

from nmigen import *
from lib.bus.stream.sim_util import write_to_stream, read_from_stream
from lib.bus.stream.stream import PacketizedStream
from lib.compression.bit_stuffing import BitStuffer
from lib.compression.huffman_encoder import HuffmanEncoder
from util.sim import SimPlatform
from bitarray import bitarray


class HuffmanTest(unittest.TestCase):
    def test_hello_world(self):
        platform = SimPlatform()
        m = Module()

        input = PacketizedStream(8)
        input_data = "hello, world :)"
        distribution = defaultdict(lambda: 0)
        for c in input_data:
            distribution[ord(c)] += 1
        huffman = m.submodules.huffman = HuffmanEncoder(input, distribution)

        def write_process():
            for i, c in enumerate(input_data):
                yield from write_to_stream(input, payload=ord(c), last=(i == len(input_data) - 1))

        def read_process():
            read = ""
            while True:
                data, length, last = (yield from read_from_stream(huffman.output, extract=("payload", "current_width", "last")))
                bitstring = "{:0255b}".format(data)[::-1][:length]
                read += bitstring
                if last:
                    break
            print(read)
            decode_iter = bitarray(read).iterdecode({k: bitarray(v[::-1]) for k, v in huffman.table.items()})
            decoded = ""
            try:
                for c in decode_iter:
                    decoded += chr(c)
            except ValueError:  # Decoding may not finish with the byte boundary
                pass
            self.assertEquals(input_data, decoded)

        platform.add_sim_clock("sync", 100e6)
        platform.add_process(write_process, "sync")
        platform.sim(m, read_process)

    def test_hello_world_bit_stuffing(self):
        platform = SimPlatform()
        m = Module()

        input = PacketizedStream(8)
        input_data = "hello, world :)"
        distribution = defaultdict(lambda: 0)
        for c in input_data:
            distribution[ord(c)] += 1
        huffman = m.submodules.huffman = HuffmanEncoder(input, distribution)
        bit_stuffing = m.submodules.bit_stuffing = BitStuffer(huffman.output, 8)

        def write_process():
            for i, c in enumerate(input_data):
                yield from write_to_stream(input, payload=ord(c), last=(i == len(input_data) - 1))

        def read_process():
            read = []
            while True:
                payload, last = (yield from read_from_stream(bit_stuffing.output, extract=("payload", "last")))
                read.append("{:08b}".format(payload))
                if last:
                    break
            read_bitarray = "".join(x[::-1] for x in read)
            print(read_bitarray)
            decode_iter = bitarray(read_bitarray).iterdecode({k: bitarray(v[::-1]) for k, v in huffman.table.items()})
            for c, expected in zip(decode_iter, input_data):
                self.assertEquals(chr(c), expected)

        platform.add_sim_clock("sync", 100e6)
        platform.add_process(write_process, "sync")
        platform.sim(m, read_process)