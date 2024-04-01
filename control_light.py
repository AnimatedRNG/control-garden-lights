#!/usr/bin/env python3

import datetime
import ephem
import leglight
import math
from zoneinfo import ZoneInfo


# Fudge factor to get some extra light.
EXTRA_LIGHT = 0.2


def main():
    light = leglight.discover(2)[0]
    twilight = -12 * ephem.degree

    zone = ZoneInfo("US/Eastern")

    for i in range(24):
        s = ephem.Sun()
        bs = ephem.city("Boston")
        local = datetime.datetime(2024, 6, 1, i, 0, tzinfo=zone)
        bs.date = ephem.Date(local)
        s.compute(bs)
        print(
            local,
            max(min(-math.sin(float(ephem.degrees(s.alt))) + EXTRA_LIGHT, 1.0), 0.0),
            s.alt > twilight,
        )
    """if s.alt < twilight:
        light.on()
    else:
        light.off()
    print('Is it light in Boston?', s.alt > twilight)"""


if __name__ == "__main__":
    main()
