from collections import OrderedDict
from dataclasses import dataclass
from enum import Enum
from typing import TypeVar

from nmigen import *
from nmigen import tracer

from util.py_util import camel_to_snake


class Bundle:
    def __init__(self, name=None, src_loc_at=1):
        super().__setattr__("name", name or tracer.get_var_name(depth=1 + src_loc_at, default="$" + camel_to_snake(self.__class__.__name__)))
        self._directions = OrderedDict()

    def __setattr__(self, key, value):
        if key == "name":
            super().__setattr__(key, value)
            self._update_name()

        if isinstance(value, Port):
            self._directions[key] = value.direction
            value = value.to_wrap
        elif isinstance(value, (Value, Bundle)):  # TODO: do we really want this behaviour also for values
            self._directions[key] = Direction.DOWNWARDS

        if hasattr(value, "name") and isinstance(value.name, str):
            if value.name.startswith("$"):  # with @UPWARDS and @DOWNWARDS we are breaking nmigens tracer
                value.name = key
            value.name = format("{}__{}".format(self.name, value.name))

        super().__setattr__(key, value)

    def _update_name(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if hasattr(attr, "name") and isinstance(attr.name, str):
                attr.name = format("{}__{}".format(self.name, attr.name.split("__")[-1]))

    def __repr__(self):
        return "<{}(Interface) name={}>".format(self.__class__.__name__, self.name)

    def connect_upstream(self, upstream, allow_partial=False):
        return self._connect(upstream, self, allow_partial)

    def connect_downstream(self, downstream, allow_partial=False):
        return self._connect(self, downstream, allow_partial)

    @property
    def _downwards_ports(self):
        return [k for k, v in self._directions.items() if v == Direction.DOWNWARDS]

    @property
    def _upwards_ports(self):
        return [k for k, v in self._directions.items() if v == Direction.UPWARDS]

    @staticmethod
    def _connect(upstream, downstream, allow_partial):
        assert isinstance(upstream, Bundle) and isinstance(downstream, Bundle)
        if not allow_partial:
            assert upstream._directions == downstream._directions

        statements = []
        for k in upstream._downwards_ports:
            if hasattr(upstream, k) and hasattr(downstream, k):
                assert upstream._directions[k] == downstream._directions[k]
                u, d = getattr(upstream, k), getattr(downstream, k)
                if isinstance(d, Value):
                    statements += [d.eq(u)]
                elif isinstance(d, Bundle):
                    statements += Bundle._connect(u, d, allow_partial)
        for k in downstream._upwards_ports:
            if hasattr(upstream, k) and hasattr(downstream, k):
                assert upstream._directions[k] == downstream._directions[k]
                u, d = getattr(upstream, k), getattr(downstream, k)
                if isinstance(u, Value):
                    statements += [u.eq(d)]
                elif isinstance(u, Bundle):
                    statements += Bundle._connect(d, u, allow_partial)
        return statements


class Direction(Enum):
    DOWNWARDS = 0
    UPWARDS = 1

    T = TypeVar('T')  # we lie about the return type to get nice IDE completions
    def __rmatmul__(self, other: T) -> T:
        return Port(self, other)


DOWNWARDS = Direction.DOWNWARDS
UPWARDS = Direction.UPWARDS


@dataclass
class Port:
    direction: Direction
    to_wrap: object
