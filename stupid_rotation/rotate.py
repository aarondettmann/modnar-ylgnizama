#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math as m

import matplotlib.pyplot as plt


def rotate_points_2D(points, angle):
    """Rotate points using complex numbers"""

    # Number representing the rotation
    z = complex(m.cos(angle), m.sin(angle))

    points_rot = []
    for point in points:
        p_rotated = complex(*point)*z
        points_rot.append([p_rotated.real, p_rotated.imag])

    return points_rot


def main():
    """Rotate a box"""

    box = [
        [-1, -1],
        [1, -1],
        [1, 1],
        [-1, 1],
        [-1, -1],
    ]

    fig, axs = plt.subplots(1, 1)
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    axs.set_aspect('equal')

    for angle in range(0, 90, 2):
        box_rotated = rotate_points_2D(box, m.radians(angle))

        x = [p[0] for p in box_rotated]
        y = [p[1] for p in box_rotated]
        axs.plot(x, y, marker='o', color='blue')
        plt.pause(0.1)

    plt.show()


if __name__ == '__main__':
    main()
