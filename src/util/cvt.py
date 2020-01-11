import subprocess

CVT_BIN = "cvt"


def calculate_video_timing(width, height, refresh, reduced_blanking=True):
    if (refresh % 60) != 0:
        reduced_blanking = False # only possible for multiples of 60 Hz

    cvt_bin = ([CVT_BIN] + ["-r"]) if reduced_blanking else [CVT_BIN]
    out, _ = subprocess.Popen(cvt_bin + [str(width), str(height), str(refresh)],
                              stdout=subprocess.PIPE).communicate()
    modeline = out.split(b"\n")[1].split()
    pxclk = float(modeline[2])

    names = ["hres", "hsync_start", "hsync_end", "hscan", "vres", "vsync_start", "vsync_end", "vscan"]
    values = map(int, modeline[3:-2])

    return_dict = dict(zip(names, values))
    return_dict["pxclk"] = pxclk

    return return_dict