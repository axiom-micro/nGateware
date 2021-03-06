from nmigen import Signal

from lib.bus.stream.stream import BasicStream
from lib.data_structure.bundle import DOWNWARDS


class ImageStream(BasicStream):
    """
    A stream that can be used to transfer image data.
    """

    def __init__(self, payload_shape=0, name=None, src_loc_at=1):
        super().__init__(payload_shape, name, src_loc_at=1 + src_loc_at)
        self.line_last = Signal() @ DOWNWARDS
        self.frame_last = Signal() @ DOWNWARDS
