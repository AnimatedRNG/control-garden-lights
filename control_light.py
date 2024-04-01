#!/usr/bin/env python3

import datetime
import ephem
import leglight
import math
from zoneinfo import ZoneInfo


# Fudge factor to get some extra light.
EXTRA_LIGHT = 0.2


def main():
    light = leglight.discover(10)[0]

    s = ephem.Sun()
    bs = ephem.city("Boston")
    s.compute(bs)
    intensity = max(min(-math.sin(float(ephem.degrees(s.alt))) + EXTRA_LIGHT, 1.0), 0.0)
    if intensity > 0:
        light.on()
        light.brightness(intensity * 100)
        light.color(6500)
    else:
        light.off()


if __name__ == "__main__":
    main()
