from nmigen import *

from lib.bus.stream.stream_transformer import StreamTransformer
from lib.peripherals.csr_bank import ControlSignal
from lib.video.image_stream import ImageStream
from lib.video.rgb import RGB24
from lib.video.video_transformer import VideoTransformer
from util.nmigen_misc import nAvrg


class RecoloringDebayerer(Elaboratable):
    """Debayer an image by simply coloring the pixels in the correct color"""
    def __init__(self, input: ImageStream):
        self.input = input
        self.output = ImageStream(24)

        self.shift_x = ControlSignal()
        self.shift_y = ControlSignal()

    def elaborate(self, platform):
        m = Module()

        x_odd = Signal()
        y_odd = Signal()
        with StreamTransformer(self.input, self.output, m):
            with m.If(self.input.line_last):
                m.d.comb += self.output.line_last.eq(1)
                m.d.sync += x_odd.eq(0)
                m.d.sync += y_odd.eq(~y_odd)
            with m.Else():
                m.d.sync += x_odd.eq(~x_odd)
            with m.If(self.input.frame_last):
                m.d.comb += self.output.frame_last.eq(1)
                m.d.sync += y_odd.eq(0)
                m.d.sync += x_odd.eq(0)

        x = x_odd ^ self.shift_x
        y = y_odd ^ self.shift_y

        rgb = RGB24()
        with m.If(x & ~y):
            m.d.comb += rgb.r.eq(self.input.payload)
        with m.Elif(~x & y):
            m.d.comb += rgb.b.eq(self.input.payload)
        with m.Else():
            m.d.comb += rgb.g.eq(self.input.payload // 2)

        m.d.comb += self.output.payload.eq(rgb)

        return m


class SimpleInterpolatingDebayerer(Elaboratable):
    """Debayer an image by interpolating the colour with the neighbouring pixels"""
    def __init__(self, input: ImageStream, width=3000, height=3000):
        self.input = input
        self.output = ImageStream(24)

        self.width = width
        self.height = height

        self.shift_x = ControlSignal()
        self.shift_y = ControlSignal()

    def elaborate(self, platform):
        m = Module()

        def transformer_function(x, y, image_proxy):
            x_even = Signal()
            m.d.comb += x_even.eq((x + self.shift_x) % 2 == 0)
            y_even = Signal()
            m.d.comb += y_even.eq((y + self.shift_y) % 2 == 0)

            rgb = RGB24()
            with m.If(x_even & ~y_even):  # we are a red pixel
                m.d.comb += rgb.r.eq(image_proxy[x, y])
                m.d.comb += rgb.g.eq(nAvrg(
                    (image_proxy[x-1, y]),
                    (image_proxy[x+1, y]),
                    (image_proxy[x, y-1]),
                    (image_proxy[x, y+1]),
                ))
                m.d.comb += rgb.b.eq(nAvrg(
                    (image_proxy[x - 1, y - 1]),
                    (image_proxy[x + 1, y + 1]),
                    (image_proxy[x + 1, y - 1]),
                    (image_proxy[x - 1, y + 1]),
                ))
            with m.Elif(~x_even & y_even):  # we are a blue pixel
                m.d.comb += rgb.b.eq(image_proxy[x, y])
                m.d.comb += rgb.g.eq(nAvrg(
                    (image_proxy[x - 1, y]),
                    (image_proxy[x + 1, y]),
                    (image_proxy[x, y - 1]),
                    (image_proxy[x, y + 1]),
                ))
                m.d.comb += rgb.r.eq(nAvrg(
                    (image_proxy[x - 1, y - 1]),
                    (image_proxy[x + 1, y + 1]),
                    (image_proxy[x + 1, y - 1]),
                    (image_proxy[x - 1, y + 1]),
                ))
            with m.Elif(~x_even & ~y_even):  # we are a green pixel in a red row
                m.d.comb += rgb.g.eq(image_proxy[x, y])
                m.d.comb += rgb.r.eq(nAvrg(
                    (image_proxy[x - 1, y]),
                    (image_proxy[x + 1, y]),
                ))
                m.d.comb += rgb.b.eq(nAvrg(
                    (image_proxy[x, y - 1]),
                    (image_proxy[x, y + 1]),
                ))
            with m.Elif(x_even & y_even):  # we are a green pixel in a blue row
                m.d.comb += rgb.g.eq(image_proxy[x, y])
                m.d.comb += rgb.b.eq(nAvrg(
                    (image_proxy[x - 1, y]),
                    (image_proxy[x + 1, y]),
                ))
                m.d.comb += rgb.r.eq(nAvrg(
                    (image_proxy[x, y - 1]),
                    (image_proxy[x, y + 1]),
                ))

            return rgb

        video_transformer = m.submodules.video_transformer = VideoTransformer(self.input, transformer_function,
                                                                              self.width, self.height)
        m.d.comb += self.output.connect_upstream(video_transformer.output)

        return m