from nmigen.build import Resource, Pins, DiffPairs, Connector, Attrs

from devices.plugins.plugin_connector import add_plugin_connector
from .microzed_platform import MicroZedZ020Platform


class BetaPlatform(MicroZedZ020Platform):
    def __init__(self):
        super().__init__()
        self.connect_mainboard()

    def connect_mainboard(self):
        add_plugin_connector(
            platform=self, number="south", conn=("expansion", 1),
            lvds=["94 96", "93 95", "97 99", "87 89", "81 83", "73 75"],
        )
        add_plugin_connector(
            platform=self, number="north", conn=("expansion", 0),
            lvds=["68 70", "74 76", "82 84", "92 94", "93 91", "89 87"]
        )

        # TODO: add ext & shield connectors (but how?)
        # best would be a way to (transpranetly) handle the routing fabrics
        self.add_resources([
            Resource("routing", 'east', DiffPairs('29', '31', dir='io', conn=("expansion", 1)),
                     Attrs(IOSTANDARD="LVCMOS33")),
            Resource("routing", 'west', Pins("56", dir='o', conn=("expansion", 0)), Attrs(IOSTANDARD="LVCMOS33")),
        ])
