## begin autogenerated stub for class RawPll by xilinx_blackbox.py DO NOT EDIT ##
from nmigen import Signal
from typing import Tuple
class RawPll:
    def __init__(**kwargs):
        pass
    locked: Signal # LOCKED
    pwrdwn: Signal # PWRDWN
    rst: Signal # RST
    class _Clk:
        in1: Signal # CLKIN1
        fbout: Signal # CLKFBOUT
        fbin: Signal # CLKFBIN

        out : Tuple[Signal, Signal, Signal, Signal, Signal, Signal]
    clk : _Clk

## end autogenerated stub for class RawPll by xilinx_blackbox.py ##

## begin autogenerated stub for class Oserdes by xilinx_blackbox.py DO NOT EDIT ##
from nmigen import Signal
from typing import Tuple
class Oserdes:
    def __init__(**kwargs):
        pass
    clk: Signal # CLK
    clkdiv: Signal # CLKDIV
    oce: Signal # OCE
    ofb: Signal # OFB
    oq: Signal # OQ
    rst: Signal # RST
    tce: Signal # TCE
    tfb: Signal # TFB
    tq: Signal # TQ

    d : Tuple[None, Signal, Signal, Signal, Signal, Signal, Signal, Signal, Signal]
    class _Shift:

        out : Tuple[None, Signal, Signal]

        in_ : Tuple[None, Signal, Signal]
    shift : _Shift

    t : Tuple[None, Signal, Signal, Signal, Signal]
    class _Tbyte:
        out: Signal # TBYTEOUT
        in_: Signal # TBYTEIN
    tbyte : _Tbyte

## end autogenerated stub for class Oserdes by xilinx_blackbox.py ##

## begin autogenerated stub for class IdelayCtl by xilinx_blackbox.py DO NOT EDIT ##
from nmigen import Signal
from typing import Tuple
class IdelayCtl:
    def __init__(**kwargs):
        pass
    rdy: Signal # RDY
    refclk: Signal # REFCLK
    rst: Signal # RST

## end autogenerated stub for class IdelayCtl by xilinx_blackbox.py ##
## begin autogenerated stub for class Idelay by xilinx_blackbox.py DO NOT EDIT ##
from nmigen import Signal
from typing import Tuple
class Idelay:
    def __init__(**kwargs):
        pass
    c: Signal # C
    ce: Signal # CE
    cinvctrl: Signal # CINVCTRL
    idatain: Signal # IDATAIN
    inc: Signal # INC
    ld: Signal # LD
    ldpipeen: Signal # LDPIPEEN
    regrst: Signal # REGRST
    class _Cntvalue:
        out: Signal # CNTVALUEOUT
        in_: Signal # CNTVALUEIN
    cntvalue : _Cntvalue
    class _Data:
        out: Signal # DATAOUT
        in_: Signal # DATAIN
    data : _Data

## end autogenerated stub for class Idelay by xilinx_blackbox.py ##
## begin autogenerated stub for class Iserdes by xilinx_blackbox.py DO NOT EDIT ##
from nmigen import Signal
from typing import Tuple
class Iserdes:
    def __init__(**kwargs):
        pass
    bitslip: Signal # BITSLIP
    clk: Signal # CLK
    clkb: Signal # CLKB
    clkdiv: Signal # CLKDIV
    clkdivp: Signal # CLKDIVP
    d: Signal # D
    ddly: Signal # DDLY
    o: Signal # O
    oclk: Signal # OCLK
    oclkb: Signal # OCLKB
    ofb: Signal # OFB
    rst: Signal # RST

    ce : Tuple[None, Signal, Signal]
    class _Dynclk:
        sel: Signal # DYNCLKSEL
        divsel: Signal # DYNCLKDIVSEL
    dynclk : _Dynclk

    q : Tuple[None, Signal, Signal, Signal, Signal, Signal, Signal, Signal, Signal]
    class _Shift:

        out : Tuple[None, Signal, Signal]

        in_ : Tuple[None, Signal, Signal]
    shift : _Shift

## end autogenerated stub for class Iserdes by xilinx_blackbox.py ##











































































































































































































## begin autogenerated stub for class Ps7 by xilinx_blackbox.py DO NOT EDIT ##
from nmigen import Signal
from typing import Tuple
class Ps7:
    def __init__(**kwargs):
        pass
    fpgaidlen: Signal # FPGAIDLEN
    mio: Signal # MIO
    psclk: Signal # PSCLK
    psporb: Signal # PSPORB
    pssrstb: Signal # PSSRSTB
    class _Ddr:
        web: Signal # DDRWEB
        vrp: Signal # DDRVRP
        vrn: Signal # DDRVRN
        rasb: Signal # DDRRASB
        odt: Signal # DDRODT
        drstb: Signal # DDRDRSTB
        dq: Signal # DDRDQ
        dm: Signal # DDRDM
        csb: Signal # DDRCSB
        ckp: Signal # DDRCKP
        ckn: Signal # DDRCKN
        cke: Signal # DDRCKE
        casb: Signal # DDRCASB
        ba: Signal # DDRBA
        arb: Signal # DDRARB
        a: Signal # DDRA
        class _Dqs:
            n: Signal # DDRDQSN
            p: Signal # DDRDQSP
        dqs : _Dqs
    ddr : _Ddr
    class _Dma_3:
        aclk: Signal # DMA3ACLK
        daready: Signal # DMA3DAREADY
        datype: Signal # DMA3DATYPE
        davalid: Signal # DMA3DAVALID
        drlast: Signal # DMA3DRLAST
        drready: Signal # DMA3DRREADY
        drtype: Signal # DMA3DRTYPE
        drvalid: Signal # DMA3DRVALID
        rstn: Signal # DMA3RSTN
    class _Dma_2:
        aclk: Signal # DMA2ACLK
        daready: Signal # DMA2DAREADY
        datype: Signal # DMA2DATYPE
        davalid: Signal # DMA2DAVALID
        drlast: Signal # DMA2DRLAST
        drready: Signal # DMA2DRREADY
        drtype: Signal # DMA2DRTYPE
        drvalid: Signal # DMA2DRVALID
        rstn: Signal # DMA2RSTN
    class _Dma_1:
        aclk: Signal # DMA1ACLK
        daready: Signal # DMA1DAREADY
        datype: Signal # DMA1DATYPE
        davalid: Signal # DMA1DAVALID
        drlast: Signal # DMA1DRLAST
        drready: Signal # DMA1DRREADY
        drtype: Signal # DMA1DRTYPE
        drvalid: Signal # DMA1DRVALID
        rstn: Signal # DMA1RSTN
    class _Dma_0:
        aclk: Signal # DMA0ACLK
        daready: Signal # DMA0DAREADY
        datype: Signal # DMA0DATYPE
        davalid: Signal # DMA0DAVALID
        drlast: Signal # DMA0DRLAST
        drready: Signal # DMA0DRREADY
        drtype: Signal # DMA0DRTYPE
        drvalid: Signal # DMA0DRVALID
        rstn: Signal # DMA0RSTN
    dma : Tuple[_Dma_0, _Dma_1, _Dma_2, _Dma_3]
    class _Emio:
        sramintin: Signal # EMIOSRAMINTIN
        class _Wdt:
            clki: Signal # EMIOWDTCLKI
            rsto: Signal # EMIOWDTRSTO
        wdt : _Wdt
        class _Usb_0:
            portindctl: Signal # EMIOUSB0PORTINDCTL
            class _Vbuspwr:
                fault: Signal # EMIOUSB0VBUSPWRFAULT
                select: Signal # EMIOUSB0VBUSPWRSELECT
            vbuspwr : _Vbuspwr
        class _Usb_1:
            portindctl: Signal # EMIOUSB1PORTINDCTL
            class _Vbuspwr:
                fault: Signal # EMIOUSB1VBUSPWRFAULT
                select: Signal # EMIOUSB1VBUSPWRSELECT
            vbuspwr : _Vbuspwr
        usb : Tuple[_Usb_0, _Usb_1]
        class _Uart_0:
            tx: Signal # EMIOUART0TX
            rx: Signal # EMIOUART0RX
            rtsn: Signal # EMIOUART0RTSN
            rin: Signal # EMIOUART0RIN
            dtrn: Signal # EMIOUART0DTRN
            dsrn: Signal # EMIOUART0DSRN
            dcdn: Signal # EMIOUART0DCDN
            ctsn: Signal # EMIOUART0CTSN
        class _Uart_1:
            tx: Signal # EMIOUART1TX
            rx: Signal # EMIOUART1RX
            rtsn: Signal # EMIOUART1RTSN
            rin: Signal # EMIOUART1RIN
            dtrn: Signal # EMIOUART1DTRN
            dsrn: Signal # EMIOUART1DSRN
            dcdn: Signal # EMIOUART1DCDN
            ctsn: Signal # EMIOUART1CTSN
        uart : Tuple[_Uart_0, _Uart_1]
        class _Ttc_0:
            waveo: Signal # EMIOTTC0WAVEO
            clki: Signal # EMIOTTC0CLKI
        class _Ttc_1:
            waveo: Signal # EMIOTTC1WAVEO
            clki: Signal # EMIOTTC1CLKI
        ttc : Tuple[_Ttc_0, _Ttc_1]
        class _Trace:
            clk: Signal # EMIOTRACECLK
            ctl: Signal # EMIOTRACECTL
            data: Signal # EMIOTRACEDATA
        trace : _Trace
        class _Spi_0:
            stn: Signal # EMIOSPI0STN
            sson: Signal # EMIOSPI0SSON
            ssntn: Signal # EMIOSPI0SSNTN
            ssin: Signal # EMIOSPI0SSIN
            so: Signal # EMIOSPI0SO
            si: Signal # EMIOSPI0SI
            motn: Signal # EMIOSPI0MOTN
            mo: Signal # EMIOSPI0MO
            mi: Signal # EMIOSPI0MI
            class _Sclk:
                i: Signal # EMIOSPI0SCLKI
                o: Signal # EMIOSPI0SCLKO
                tn: Signal # EMIOSPI0SCLKTN
            sclk : _Sclk
        class _Spi_1:
            stn: Signal # EMIOSPI1STN
            sson: Signal # EMIOSPI1SSON
            ssntn: Signal # EMIOSPI1SSNTN
            ssin: Signal # EMIOSPI1SSIN
            so: Signal # EMIOSPI1SO
            si: Signal # EMIOSPI1SI
            motn: Signal # EMIOSPI1MOTN
            mo: Signal # EMIOSPI1MO
            mi: Signal # EMIOSPI1MI
            class _Sclk:
                i: Signal # EMIOSPI1SCLKI
                o: Signal # EMIOSPI1SCLKO
                tn: Signal # EMIOSPI1SCLKTN
            sclk : _Sclk
        spi : Tuple[_Spi_0, _Spi_1]
        class _Sdio_0:
            wp: Signal # EMIOSDIO0WP
            led: Signal # EMIOSDIO0LED
            clkfb: Signal # EMIOSDIO0CLKFB
            clk: Signal # EMIOSDIO0CLK
            cdn: Signal # EMIOSDIO0CDN
            class _Data:
                i: Signal # EMIOSDIO0DATAI
                o: Signal # EMIOSDIO0DATAO
                tn: Signal # EMIOSDIO0DATATN
            data : _Data
            class _Cmd:
                i: Signal # EMIOSDIO0CMDI
                o: Signal # EMIOSDIO0CMDO
                tn: Signal # EMIOSDIO0CMDTN
            cmd : _Cmd
            class _Bus:
                pow: Signal # EMIOSDIO0BUSPOW
                volt: Signal # EMIOSDIO0BUSVOLT
            bus : _Bus
        class _Sdio_1:
            wp: Signal # EMIOSDIO1WP
            led: Signal # EMIOSDIO1LED
            clkfb: Signal # EMIOSDIO1CLKFB
            clk: Signal # EMIOSDIO1CLK
            cdn: Signal # EMIOSDIO1CDN
            class _Data:
                i: Signal # EMIOSDIO1DATAI
                o: Signal # EMIOSDIO1DATAO
                tn: Signal # EMIOSDIO1DATATN
            data : _Data
            class _Cmd:
                i: Signal # EMIOSDIO1CMDI
                o: Signal # EMIOSDIO1CMDO
                tn: Signal # EMIOSDIO1CMDTN
            cmd : _Cmd
            class _Bus:
                pow: Signal # EMIOSDIO1BUSPOW
                volt: Signal # EMIOSDIO1BUSVOLT
            bus : _Bus
        sdio : Tuple[_Sdio_0, _Sdio_1]
        class _Pjtagt:
            ck: Signal # EMIOPJTAGTCK
            di: Signal # EMIOPJTAGTDI
            do: Signal # EMIOPJTAGTDO
            dtn: Signal # EMIOPJTAGTDTN
            ms: Signal # EMIOPJTAGTMS
        pjtagt : _Pjtagt
        class _I2c_0:
            class _Sda:
                i: Signal # EMIOI2C0SDAI
                o: Signal # EMIOI2C0SDAO
                tn: Signal # EMIOI2C0SDATN
            sda : _Sda
            class _Scl:
                i: Signal # EMIOI2C0SCLI
                o: Signal # EMIOI2C0SCLO
                tn: Signal # EMIOI2C0SCLTN
            scl : _Scl
        class _I2c_1:
            class _Sda:
                i: Signal # EMIOI2C1SDAI
                o: Signal # EMIOI2C1SDAO
                tn: Signal # EMIOI2C1SDATN
            sda : _Sda
            class _Scl:
                i: Signal # EMIOI2C1SCLI
                o: Signal # EMIOI2C1SCLO
                tn: Signal # EMIOI2C1SCLTN
            scl : _Scl
        i2c : Tuple[_I2c_0, _I2c_1]
        class _Gpio:
            i: Signal # EMIOGPIOI
            o: Signal # EMIOGPIOO
            tn: Signal # EMIOGPIOTN
        gpio : _Gpio
        class _Enet_0:
            extintin: Signal # EMIOENET0EXTINTIN
            class _Sof:
                rx: Signal # EMIOENET0SOFRX
                tx: Signal # EMIOENET0SOFTX
            sof : _Sof
            class _Ptp:
                class _Delayreq:
                    tx: Signal # EMIOENET0PTPDELAYREQTX
                    rx: Signal # EMIOENET0PTPDELAYREQRX
                delayreq : _Delayreq
                class _Pdelayre:
                    sptx: Signal # EMIOENET0PTPPDELAYRESPTX
                    sprx: Signal # EMIOENET0PTPPDELAYRESPRX
                    qtx: Signal # EMIOENET0PTPPDELAYREQTX
                    qrx: Signal # EMIOENET0PTPPDELAYREQRX
                pdelayre : _Pdelayre
                class _Syncframe:
                    tx: Signal # EMIOENET0PTPSYNCFRAMETX
                    rx: Signal # EMIOENET0PTPSYNCFRAMERX
                syncframe : _Syncframe
            ptp : _Ptp
            class _Mdio:
                i: Signal # EMIOENET0MDIOI
                mdc: Signal # EMIOENET0MDIOMDC
                o: Signal # EMIOENET0MDIOO
                tn: Signal # EMIOENET0MDIOTN
            mdio : _Mdio
            class _Gmii:
                col: Signal # EMIOENET0GMIICOL
                crs: Signal # EMIOENET0GMIICRS
                rxclk: Signal # EMIOENET0GMIIRXCLK
                rxd: Signal # EMIOENET0GMIIRXD
                rxdv: Signal # EMIOENET0GMIIRXDV
                rxer: Signal # EMIOENET0GMIIRXER
                txclk: Signal # EMIOENET0GMIITXCLK
                txd: Signal # EMIOENET0GMIITXD
                class _Txe:
                    r: Signal # EMIOENET0GMIITXER
                    n: Signal # EMIOENET0GMIITXEN
                txe : _Txe
            gmii : _Gmii
        class _Enet_1:
            extintin: Signal # EMIOENET1EXTINTIN
            class _Sof:
                rx: Signal # EMIOENET1SOFRX
                tx: Signal # EMIOENET1SOFTX
            sof : _Sof
            class _Ptp:
                class _Delayreq:
                    tx: Signal # EMIOENET1PTPDELAYREQTX
                    rx: Signal # EMIOENET1PTPDELAYREQRX
                delayreq : _Delayreq
                class _Pdelayre:
                    sptx: Signal # EMIOENET1PTPPDELAYRESPTX
                    sprx: Signal # EMIOENET1PTPPDELAYRESPRX
                    qtx: Signal # EMIOENET1PTPPDELAYREQTX
                    qrx: Signal # EMIOENET1PTPPDELAYREQRX
                pdelayre : _Pdelayre
                class _Syncframe:
                    tx: Signal # EMIOENET1PTPSYNCFRAMETX
                    rx: Signal # EMIOENET1PTPSYNCFRAMERX
                syncframe : _Syncframe
            ptp : _Ptp
            class _Mdio:
                i: Signal # EMIOENET1MDIOI
                mdc: Signal # EMIOENET1MDIOMDC
                o: Signal # EMIOENET1MDIOO
                tn: Signal # EMIOENET1MDIOTN
            mdio : _Mdio
            class _Gmii:
                col: Signal # EMIOENET1GMIICOL
                crs: Signal # EMIOENET1GMIICRS
                rxclk: Signal # EMIOENET1GMIIRXCLK
                rxd: Signal # EMIOENET1GMIIRXD
                rxdv: Signal # EMIOENET1GMIIRXDV
                rxer: Signal # EMIOENET1GMIIRXER
                txclk: Signal # EMIOENET1GMIITXCLK
                txd: Signal # EMIOENET1GMIITXD
                class _Txe:
                    r: Signal # EMIOENET1GMIITXER
                    n: Signal # EMIOENET1GMIITXEN
                txe : _Txe
            gmii : _Gmii
        enet : Tuple[_Enet_0, _Enet_1]
        class _Can_0:
            class _Phy:
                rx: Signal # EMIOCAN0PHYRX
                tx: Signal # EMIOCAN0PHYTX
            phy : _Phy
        class _Can_1:
            class _Phy:
                rx: Signal # EMIOCAN1PHYRX
                tx: Signal # EMIOCAN1PHYTX
            phy : _Phy
        can : Tuple[_Can_0, _Can_1]
    emio : _Emio
    class _Event:
        o: Signal # EVENTEVENTO
        i: Signal # EVENTEVENTI
        class _Standbywf:
            e: Signal # EVENTSTANDBYWFE
            i: Signal # EVENTSTANDBYWFI
        standbywf : _Standbywf
    event : _Event
    class _Fclk:
        resetn: Signal # FCLKRESETN
        clktrign: Signal # FCLKCLKTRIGN
        clk: Signal # FCLKCLK
    fclk : _Fclk
    class _Ftm:
        class _Tp2f:
            debug: Signal # FTMTP2FDEBUG
            trig: Signal # FTMTP2FTRIG
            trigack: Signal # FTMTP2FTRIGACK
        tp2f : _Tp2f
        class _Tf2p:
            debug: Signal # FTMTF2PDEBUG
            trig: Signal # FTMTF2PTRIG
            trigack: Signal # FTMTF2PTRIGACK
        tf2p : _Tf2p
        class _Dtracein:
            atid: Signal # FTMDTRACEINATID
            clock: Signal # FTMDTRACEINCLOCK
            data: Signal # FTMDTRACEINDATA
            valid: Signal # FTMDTRACEINVALID
        dtracein : _Dtracein
    ftm : _Ftm
    class _Irq:
        p2f: Signal # IRQP2F
        f2p: Signal # IRQF2P
    irq : _Irq
    class _Maxigp_1:
        aclk: Signal # MAXIGP1ACLK
        araddr: Signal # MAXIGP1ARADDR
        arburst: Signal # MAXIGP1ARBURST
        arcache: Signal # MAXIGP1ARCACHE
        aresetn: Signal # MAXIGP1ARESETN
        arid: Signal # MAXIGP1ARID
        arprot: Signal # MAXIGP1ARPROT
        arqos: Signal # MAXIGP1ARQOS
        arready: Signal # MAXIGP1ARREADY
        arsize: Signal # MAXIGP1ARSIZE
        arvalid: Signal # MAXIGP1ARVALID
        awaddr: Signal # MAXIGP1AWADDR
        awburst: Signal # MAXIGP1AWBURST
        awcache: Signal # MAXIGP1AWCACHE
        awid: Signal # MAXIGP1AWID
        awprot: Signal # MAXIGP1AWPROT
        awqos: Signal # MAXIGP1AWQOS
        awready: Signal # MAXIGP1AWREADY
        awsize: Signal # MAXIGP1AWSIZE
        awvalid: Signal # MAXIGP1AWVALID
        bid: Signal # MAXIGP1BID
        bvalid: Signal # MAXIGP1BVALID
        rdata: Signal # MAXIGP1RDATA
        rid: Signal # MAXIGP1RID
        rlast: Signal # MAXIGP1RLAST
        rvalid: Signal # MAXIGP1RVALID
        wdata: Signal # MAXIGP1WDATA
        wid: Signal # MAXIGP1WID
        wlast: Signal # MAXIGP1WLAST
        wready: Signal # MAXIGP1WREADY
        wstrb: Signal # MAXIGP1WSTRB
        wvalid: Signal # MAXIGP1WVALID
        class _Arl:
            ock: Signal # MAXIGP1ARLOCK
            en: Signal # MAXIGP1ARLEN
        arl : _Arl
        class _Awl:
            ock: Signal # MAXIGP1AWLOCK
            en: Signal # MAXIGP1AWLEN
        awl : _Awl
        class _Bre:
            sp: Signal # MAXIGP1BRESP
            ady: Signal # MAXIGP1BREADY
        bre : _Bre
        class _Rre:
            sp: Signal # MAXIGP1RRESP
            ady: Signal # MAXIGP1RREADY
        rre : _Rre
    class _Maxigp_0:
        aclk: Signal # MAXIGP0ACLK
        araddr: Signal # MAXIGP0ARADDR
        arburst: Signal # MAXIGP0ARBURST
        arcache: Signal # MAXIGP0ARCACHE
        aresetn: Signal # MAXIGP0ARESETN
        arid: Signal # MAXIGP0ARID
        arprot: Signal # MAXIGP0ARPROT
        arqos: Signal # MAXIGP0ARQOS
        arready: Signal # MAXIGP0ARREADY
        arsize: Signal # MAXIGP0ARSIZE
        arvalid: Signal # MAXIGP0ARVALID
        awaddr: Signal # MAXIGP0AWADDR
        awburst: Signal # MAXIGP0AWBURST
        awcache: Signal # MAXIGP0AWCACHE
        awid: Signal # MAXIGP0AWID
        awprot: Signal # MAXIGP0AWPROT
        awqos: Signal # MAXIGP0AWQOS
        awready: Signal # MAXIGP0AWREADY
        awsize: Signal # MAXIGP0AWSIZE
        awvalid: Signal # MAXIGP0AWVALID
        bid: Signal # MAXIGP0BID
        bvalid: Signal # MAXIGP0BVALID
        rdata: Signal # MAXIGP0RDATA
        rid: Signal # MAXIGP0RID
        rlast: Signal # MAXIGP0RLAST
        rvalid: Signal # MAXIGP0RVALID
        wdata: Signal # MAXIGP0WDATA
        wid: Signal # MAXIGP0WID
        wlast: Signal # MAXIGP0WLAST
        wready: Signal # MAXIGP0WREADY
        wstrb: Signal # MAXIGP0WSTRB
        wvalid: Signal # MAXIGP0WVALID
        class _Arl:
            ock: Signal # MAXIGP0ARLOCK
            en: Signal # MAXIGP0ARLEN
        arl : _Arl
        class _Awl:
            ock: Signal # MAXIGP0AWLOCK
            en: Signal # MAXIGP0AWLEN
        awl : _Awl
        class _Bre:
            sp: Signal # MAXIGP0BRESP
            ady: Signal # MAXIGP0BREADY
        bre : _Bre
        class _Rre:
            sp: Signal # MAXIGP0RRESP
            ady: Signal # MAXIGP0RREADY
        rre : _Rre
    maxigp : Tuple[_Maxigp_0, _Maxigp_1]
    class _Saxi:
        class _Hp_0:
            wvalid: Signal # SAXIHP0WVALID
            wstrb: Signal # SAXIHP0WSTRB
            wrissuecap1en: Signal # SAXIHP0WRISSUECAP1EN
            wready: Signal # SAXIHP0WREADY
            wlast: Signal # SAXIHP0WLAST
            wid: Signal # SAXIHP0WID
            wdata: Signal # SAXIHP0WDATA
            wcount: Signal # SAXIHP0WCOUNT
            wacount: Signal # SAXIHP0WACOUNT
            rvalid: Signal # SAXIHP0RVALID
            rlast: Signal # SAXIHP0RLAST
            rid: Signal # SAXIHP0RID
            rdissuecap1en: Signal # SAXIHP0RDISSUECAP1EN
            rdata: Signal # SAXIHP0RDATA
            rcount: Signal # SAXIHP0RCOUNT
            racount: Signal # SAXIHP0RACOUNT
            bvalid: Signal # SAXIHP0BVALID
            bid: Signal # SAXIHP0BID
            awvalid: Signal # SAXIHP0AWVALID
            awsize: Signal # SAXIHP0AWSIZE
            awready: Signal # SAXIHP0AWREADY
            awqos: Signal # SAXIHP0AWQOS
            awprot: Signal # SAXIHP0AWPROT
            awid: Signal # SAXIHP0AWID
            awcache: Signal # SAXIHP0AWCACHE
            awburst: Signal # SAXIHP0AWBURST
            awaddr: Signal # SAXIHP0AWADDR
            arvalid: Signal # SAXIHP0ARVALID
            arsize: Signal # SAXIHP0ARSIZE
            arready: Signal # SAXIHP0ARREADY
            arqos: Signal # SAXIHP0ARQOS
            arprot: Signal # SAXIHP0ARPROT
            arid: Signal # SAXIHP0ARID
            aresetn: Signal # SAXIHP0ARESETN
            arcache: Signal # SAXIHP0ARCACHE
            arburst: Signal # SAXIHP0ARBURST
            araddr: Signal # SAXIHP0ARADDR
            aclk: Signal # SAXIHP0ACLK
            class _Rre:
                ady: Signal # SAXIHP0RREADY
                sp: Signal # SAXIHP0RRESP
            rre : _Rre
            class _Bre:
                ady: Signal # SAXIHP0BREADY
                sp: Signal # SAXIHP0BRESP
            bre : _Bre
            class _Awl:
                en: Signal # SAXIHP0AWLEN
                ock: Signal # SAXIHP0AWLOCK
            awl : _Awl
            class _Arl:
                en: Signal # SAXIHP0ARLEN
                ock: Signal # SAXIHP0ARLOCK
            arl : _Arl
        class _Hp_1:
            wvalid: Signal # SAXIHP1WVALID
            wstrb: Signal # SAXIHP1WSTRB
            wrissuecapen: Signal # SAXIHP1WRISSUECAP1EN
            wready: Signal # SAXIHP1WREADY
            wlast: Signal # SAXIHP1WLAST
            wid: Signal # SAXIHP1WID
            wdata: Signal # SAXIHP1WDATA
            wcount: Signal # SAXIHP1WCOUNT
            wacount: Signal # SAXIHP1WACOUNT
            rvalid: Signal # SAXIHP1RVALID
            rlast: Signal # SAXIHP1RLAST
            rid: Signal # SAXIHP1RID
            rdissuecapen: Signal # SAXIHP1RDISSUECAP1EN
            rdata: Signal # SAXIHP1RDATA
            rcount: Signal # SAXIHP1RCOUNT
            racount: Signal # SAXIHP1RACOUNT
            bvalid: Signal # SAXIHP1BVALID
            bid: Signal # SAXIHP1BID
            awvalid: Signal # SAXIHP1AWVALID
            awsize: Signal # SAXIHP1AWSIZE
            awready: Signal # SAXIHP1AWREADY
            awqos: Signal # SAXIHP1AWQOS
            awprot: Signal # SAXIHP1AWPROT
            awid: Signal # SAXIHP1AWID
            awcache: Signal # SAXIHP1AWCACHE
            awburst: Signal # SAXIHP1AWBURST
            awaddr: Signal # SAXIHP1AWADDR
            arvalid: Signal # SAXIHP1ARVALID
            arsize: Signal # SAXIHP1ARSIZE
            arready: Signal # SAXIHP1ARREADY
            arqos: Signal # SAXIHP1ARQOS
            arprot: Signal # SAXIHP1ARPROT
            arid: Signal # SAXIHP1ARID
            aresetn: Signal # SAXIHP1ARESETN
            arcache: Signal # SAXIHP1ARCACHE
            arburst: Signal # SAXIHP1ARBURST
            araddr: Signal # SAXIHP1ARADDR
            aclk: Signal # SAXIHP1ACLK
            class _Rre:
                ady: Signal # SAXIHP1RREADY
                sp: Signal # SAXIHP1RRESP
            rre : _Rre
            class _Bre:
                ady: Signal # SAXIHP1BREADY
                sp: Signal # SAXIHP1BRESP
            bre : _Bre
            class _Awl:
                en: Signal # SAXIHP1AWLEN
                ock: Signal # SAXIHP1AWLOCK
            awl : _Awl
            class _Arl:
                en: Signal # SAXIHP1ARLEN
                ock: Signal # SAXIHP1ARLOCK
            arl : _Arl
        class _Hp_2:
            wvalid: Signal # SAXIHP2WVALID
            wstrb: Signal # SAXIHP2WSTRB
            wrissuecap1en: Signal # SAXIHP2WRISSUECAP1EN
            wready: Signal # SAXIHP2WREADY
            wlast: Signal # SAXIHP2WLAST
            wid: Signal # SAXIHP2WID
            wdata: Signal # SAXIHP2WDATA
            wcount: Signal # SAXIHP2WCOUNT
            wacount: Signal # SAXIHP2WACOUNT
            rvalid: Signal # SAXIHP2RVALID
            rlast: Signal # SAXIHP2RLAST
            rid: Signal # SAXIHP2RID
            rdissuecap1en: Signal # SAXIHP2RDISSUECAP1EN
            rdata: Signal # SAXIHP2RDATA
            rcount: Signal # SAXIHP2RCOUNT
            racount: Signal # SAXIHP2RACOUNT
            bvalid: Signal # SAXIHP2BVALID
            bid: Signal # SAXIHP2BID
            awvalid: Signal # SAXIHP2AWVALID
            awsize: Signal # SAXIHP2AWSIZE
            awready: Signal # SAXIHP2AWREADY
            awqos: Signal # SAXIHP2AWQOS
            awprot: Signal # SAXIHP2AWPROT
            awid: Signal # SAXIHP2AWID
            awcache: Signal # SAXIHP2AWCACHE
            awburst: Signal # SAXIHP2AWBURST
            awaddr: Signal # SAXIHP2AWADDR
            arvalid: Signal # SAXIHP2ARVALID
            arsize: Signal # SAXIHP2ARSIZE
            arready: Signal # SAXIHP2ARREADY
            arqos: Signal # SAXIHP2ARQOS
            arprot: Signal # SAXIHP2ARPROT
            arid: Signal # SAXIHP2ARID
            aresetn: Signal # SAXIHP2ARESETN
            arcache: Signal # SAXIHP2ARCACHE
            arburst: Signal # SAXIHP2ARBURST
            araddr: Signal # SAXIHP2ARADDR
            aclk: Signal # SAXIHP2ACLK
            class _Rre:
                ady: Signal # SAXIHP2RREADY
                sp: Signal # SAXIHP2RRESP
            rre : _Rre
            class _Bre:
                ady: Signal # SAXIHP2BREADY
                sp: Signal # SAXIHP2BRESP
            bre : _Bre
            class _Awl:
                en: Signal # SAXIHP2AWLEN
                ock: Signal # SAXIHP2AWLOCK
            awl : _Awl
            class _Arl:
                en: Signal # SAXIHP2ARLEN
                ock: Signal # SAXIHP2ARLOCK
            arl : _Arl
        class _Hp_3:
            wvalid: Signal # SAXIHP3WVALID
            wstrb: Signal # SAXIHP3WSTRB
            wrissuecap1en: Signal # SAXIHP3WRISSUECAP1EN
            wready: Signal # SAXIHP3WREADY
            wlast: Signal # SAXIHP3WLAST
            wid: Signal # SAXIHP3WID
            wdata: Signal # SAXIHP3WDATA
            wcount: Signal # SAXIHP3WCOUNT
            wacount: Signal # SAXIHP3WACOUNT
            rvalid: Signal # SAXIHP3RVALID
            rlast: Signal # SAXIHP3RLAST
            rid: Signal # SAXIHP3RID
            rdissuecap1en: Signal # SAXIHP3RDISSUECAP1EN
            rdata: Signal # SAXIHP3RDATA
            rcount: Signal # SAXIHP3RCOUNT
            racount: Signal # SAXIHP3RACOUNT
            bvalid: Signal # SAXIHP3BVALID
            bid: Signal # SAXIHP3BID
            awvalid: Signal # SAXIHP3AWVALID
            awsize: Signal # SAXIHP3AWSIZE
            awready: Signal # SAXIHP3AWREADY
            awqos: Signal # SAXIHP3AWQOS
            awprot: Signal # SAXIHP3AWPROT
            awid: Signal # SAXIHP3AWID
            awcache: Signal # SAXIHP3AWCACHE
            awburst: Signal # SAXIHP3AWBURST
            awaddr: Signal # SAXIHP3AWADDR
            arvalid: Signal # SAXIHP3ARVALID
            arsize: Signal # SAXIHP3ARSIZE
            arready: Signal # SAXIHP3ARREADY
            arqos: Signal # SAXIHP3ARQOS
            arprot: Signal # SAXIHP3ARPROT
            arid: Signal # SAXIHP3ARID
            aresetn: Signal # SAXIHP3ARESETN
            arcache: Signal # SAXIHP3ARCACHE
            arburst: Signal # SAXIHP3ARBURST
            araddr: Signal # SAXIHP3ARADDR
            aclk: Signal # SAXIHP3ACLK
            class _Rre:
                ady: Signal # SAXIHP3RREADY
                sp: Signal # SAXIHP3RRESP
            rre : _Rre
            class _Bre:
                ady: Signal # SAXIHP3BREADY
                sp: Signal # SAXIHP3BRESP
            bre : _Bre
            class _Awl:
                en: Signal # SAXIHP3AWLEN
                ock: Signal # SAXIHP3AWLOCK
            awl : _Awl
            class _Arl:
                en: Signal # SAXIHP3ARLEN
                ock: Signal # SAXIHP3ARLOCK
            arl : _Arl
        hp : Tuple[_Hp_0, _Hp_1, _Hp_2, _Hp_3]
        class _Gp_0:
            wvalid: Signal # SAXIGP0WVALID
            wstrb: Signal # SAXIGP0WSTRB
            wready: Signal # SAXIGP0WREADY
            wlast: Signal # SAXIGP0WLAST
            wid: Signal # SAXIGP0WID
            wdata: Signal # SAXIGP0WDATA
            rvalid: Signal # SAXIGP0RVALID
            rlast: Signal # SAXIGP0RLAST
            rid: Signal # SAXIGP0RID
            rdata: Signal # SAXIGP0RDATA
            bvalid: Signal # SAXIGP0BVALID
            bid: Signal # SAXIGP0BID
            awvalid: Signal # SAXIGP0AWVALID
            awsize: Signal # SAXIGP0AWSIZE
            awready: Signal # SAXIGP0AWREADY
            awqos: Signal # SAXIGP0AWQOS
            awprot: Signal # SAXIGP0AWPROT
            awid: Signal # SAXIGP0AWID
            awcache: Signal # SAXIGP0AWCACHE
            awburst: Signal # SAXIGP0AWBURST
            awaddr: Signal # SAXIGP0AWADDR
            arvalid: Signal # SAXIGP0ARVALID
            arsize: Signal # SAXIGP0ARSIZE
            arready: Signal # SAXIGP0ARREADY
            arqos: Signal # SAXIGP0ARQOS
            arprot: Signal # SAXIGP0ARPROT
            arid: Signal # SAXIGP0ARID
            aresetn: Signal # SAXIGP0ARESETN
            arcache: Signal # SAXIGP0ARCACHE
            arburst: Signal # SAXIGP0ARBURST
            araddr: Signal # SAXIGP0ARADDR
            aclk: Signal # SAXIGP0ACLK
            class _Rre:
                ady: Signal # SAXIGP0RREADY
                sp: Signal # SAXIGP0RRESP
            rre : _Rre
            class _Bre:
                ady: Signal # SAXIGP0BREADY
                sp: Signal # SAXIGP0BRESP
            bre : _Bre
            class _Awl:
                en: Signal # SAXIGP0AWLEN
                ock: Signal # SAXIGP0AWLOCK
            awl : _Awl
            class _Arl:
                en: Signal # SAXIGP0ARLEN
                ock: Signal # SAXIGP0ARLOCK
            arl : _Arl
        class _Gp_1:
            wvalid: Signal # SAXIGP1WVALID
            wstrb: Signal # SAXIGP1WSTRB
            wready: Signal # SAXIGP1WREADY
            wlast: Signal # SAXIGP1WLAST
            wid: Signal # SAXIGP1WID
            wdata: Signal # SAXIGP1WDATA
            rvalid: Signal # SAXIGP1RVALID
            rlast: Signal # SAXIGP1RLAST
            rid: Signal # SAXIGP1RID
            rdata: Signal # SAXIGP1RDATA
            bvalid: Signal # SAXIGP1BVALID
            bid: Signal # SAXIGP1BID
            awvalid: Signal # SAXIGP1AWVALID
            awsize: Signal # SAXIGP1AWSIZE
            awready: Signal # SAXIGP1AWREADY
            awqos: Signal # SAXIGP1AWQOS
            awprot: Signal # SAXIGP1AWPROT
            awid: Signal # SAXIGP1AWID
            awcache: Signal # SAXIGP1AWCACHE
            awburst: Signal # SAXIGP1AWBURST
            awaddr: Signal # SAXIGP1AWADDR
            arvalid: Signal # SAXIGP1ARVALID
            arsize: Signal # SAXIGP1ARSIZE
            arready: Signal # SAXIGP1ARREADY
            arqos: Signal # SAXIGP1ARQOS
            arprot: Signal # SAXIGP1ARPROT
            arid: Signal # SAXIGP1ARID
            aresetn: Signal # SAXIGP1ARESETN
            arcache: Signal # SAXIGP1ARCACHE
            arburst: Signal # SAXIGP1ARBURST
            araddr: Signal # SAXIGP1ARADDR
            aclk: Signal # SAXIGP1ACLK
            class _Rre:
                ady: Signal # SAXIGP1RREADY
                sp: Signal # SAXIGP1RRESP
            rre : _Rre
            class _Bre:
                ady: Signal # SAXIGP1BREADY
                sp: Signal # SAXIGP1BRESP
            bre : _Bre
            class _Awl:
                en: Signal # SAXIGP1AWLEN
                ock: Signal # SAXIGP1AWLOCK
            awl : _Awl
            class _Arl:
                en: Signal # SAXIGP1ARLEN
                ock: Signal # SAXIGP1ARLOCK
            arl : _Arl
        gp : Tuple[_Gp_0, _Gp_1]
        class _Acp:
            aclk: Signal # SAXIACPACLK
            araddr: Signal # SAXIACPARADDR
            arburst: Signal # SAXIACPARBURST
            arcache: Signal # SAXIACPARCACHE
            aresetn: Signal # SAXIACPARESETN
            arid: Signal # SAXIACPARID
            arprot: Signal # SAXIACPARPROT
            arqos: Signal # SAXIACPARQOS
            arready: Signal # SAXIACPARREADY
            arsize: Signal # SAXIACPARSIZE
            aruser: Signal # SAXIACPARUSER
            arvalid: Signal # SAXIACPARVALID
            awaddr: Signal # SAXIACPAWADDR
            awburst: Signal # SAXIACPAWBURST
            awcache: Signal # SAXIACPAWCACHE
            awid: Signal # SAXIACPAWID
            awprot: Signal # SAXIACPAWPROT
            awqos: Signal # SAXIACPAWQOS
            awready: Signal # SAXIACPAWREADY
            awsize: Signal # SAXIACPAWSIZE
            awuser: Signal # SAXIACPAWUSER
            awvalid: Signal # SAXIACPAWVALID
            bid: Signal # SAXIACPBID
            bvalid: Signal # SAXIACPBVALID
            rdata: Signal # SAXIACPRDATA
            rid: Signal # SAXIACPRID
            rlast: Signal # SAXIACPRLAST
            rvalid: Signal # SAXIACPRVALID
            wdata: Signal # SAXIACPWDATA
            wid: Signal # SAXIACPWID
            wlast: Signal # SAXIACPWLAST
            wready: Signal # SAXIACPWREADY
            wstrb: Signal # SAXIACPWSTRB
            wvalid: Signal # SAXIACPWVALID
            class _Arl:
                ock: Signal # SAXIACPARLOCK
                en: Signal # SAXIACPARLEN
            arl : _Arl
            class _Awl:
                ock: Signal # SAXIACPAWLOCK
                en: Signal # SAXIACPAWLEN
            awl : _Awl
            class _Bre:
                sp: Signal # SAXIACPBRESP
                ady: Signal # SAXIACPBREADY
            bre : _Bre
            class _Rre:
                sp: Signal # SAXIACPRRESP
                ady: Signal # SAXIACPRREADY
            rre : _Rre
        acp : _Acp
    saxi : _Saxi

## end autogenerated stub for class Ps7 by xilinx_blackbox.py ##

## begin autogenerated stub for class Mmcm by xilinx_blackbox.py DO NOT EDIT ##
from nmigen import Signal
from typing import Tuple
class Mmcm:
    def __init__(**kwargs):
        pass
    daddr: Signal # DADDR
    dclk: Signal # DCLK
    den: Signal # DEN
    di: Signal # DI
    do: Signal # DO
    drdy: Signal # DRDY
    dwe: Signal # DWE
    locked: Signal # LOCKED
    psclk: Signal # PSCLK
    psdone: Signal # PSDONE
    psen: Signal # PSEN
    psincdec: Signal # PSINCDEC
    pwrdwn: Signal # PWRDWN
    rst: Signal # RST
    class _Clk:
        fbstopped: Signal # CLKFBSTOPPED
        fboutb: Signal # CLKFBOUTB
        fbout: Signal # CLKFBOUT
        fbin: Signal # CLKFBIN
        class _Out:
            0: Signal # CLKOUT0
            0b: Signal # CLKOUT0B
            1: Signal # CLKOUT1
            1b: Signal # CLKOUT1B
            2: Signal # CLKOUT2
            2b: Signal # CLKOUT2B
            3: Signal # CLKOUT3
            3b: Signal # CLKOUT3B
            4: Signal # CLKOUT4
            5: Signal # CLKOUT5
            6: Signal # CLKOUT6
        out : _Out
        class _Ins:
            el: Signal # CLKINSEL
            topped: Signal # CLKINSTOPPED
        ins : _Ins

        in_ : Tuple[None, Signal, Signal]
    clk : _Clk

## end autogenerated stub for class Mmcm by xilinx_blackbox.py ##
## begin autogenerated stub for class Bufg by xilinx_blackbox.py DO NOT EDIT ##
from nmigen import Signal
from typing import Tuple
class Bufg:
    def __init__(**kwargs):
        pass
    i: Signal # I
    o: Signal # O

## end autogenerated stub for class Bufg by xilinx_blackbox.py ##
