#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Adapted from:
https://www.reddit.com/r/Python/comments/dk69jv/a_vintage_program_i_made_it_in_basic_25yrs_ago/
"""

import sys

import cv2
import numpy

RESOLUTION = (500, 500)
PAUSE = 20


def cli():
    frame = numpy.zeros((*RESOLUTION, 4), numpy.uint8)

    i = 2
    while i < 255:
        for x in range(0, 1800, 200):
            for y in range(0, 1400, 200):
                cv2.circle(frame, (x, y), i+2, (i, i, i))
                cv2.circle(frame, (x, y), 254-i, (255-i, 255-i, i))
                cv2.imshow('image', frame)

        i += 2
        k = cv2.waitKey(PAUSE)

        if k == 27:
            break
        if i > 254:
            i = 2

    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
