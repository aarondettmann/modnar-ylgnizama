#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Lines and dots
"""

# Author: Aaron Dettmann

from random import randint, choice

import matplotlib.pyplot as plt


class Board:

    IMPACT_X = tuple(range(-1, 3))
    IMPACT_Y = tuple(range(-1, 3))

    def __init__(self, start_size=(10, 10), line_num=2, line_len=2):
        """
        Lines and dots

        The board is represented by a coordinate system with x and y
        directions. Only integer coordinates are valid positions.

        Args:
            :start_size: (tuple) Board size at game start (x, y)
            :line_num: (int) Number of lines
            :line_len: (int) Number of line nodes

        Attr:
            :i: (int) Number of the current iteration
            :dots: (list) List of dot coordinates
            :lines: (list) List of lines with line coordinates
            :line_num: [see args]
            :line_len: [see args]
        """

        # Iteration number
        self.i = 0

        # Coordinates of dots and lines
        self.dots = []
        self.lines = []

        self.line_num = line_num
        self.line_len = line_len

        # Starting conditions of lines and dots
        x_max, y_max = start_size
        for _ in range(self.line_num):
            line = []
            for _ in range(self.line_len):
                while True:
                    line_point = (randint(0, x_max), randint(0, y_max))
                    if line_point not in line:
                        line.append(line_point)
                        break
            self.lines.append(line)

        self._update_dots()

    def __str__(self):
        state = ""
        state += f"Iteration: {self.i}\n"
        state += f"Lines: {self.lines}\n"
        state += f"Dots: {self.dots}\n"
        state += f"{'='*100}"
        return state

    @property
    def line_dots(self):
        """Return a list of all line start/support/end points"""

        line_dots = []
        for line in self.lines:
            for point in line:
                line_dots.append(point)
        return line_dots

    def _update_dots(self):
        """Update the dots for the current state of the lines"""

        self.dots = []
        for line in self.lines:
            for point in line:
                self._add_surrounding_points(point)

    def _add_surrounding_points(self, point):
        """
        Add the surrounding points to the dots list for a given point

        Args:
            :point: (tuple) Point defined by coordinates (x, y)
        """

        x, y = point

        for dx in self.IMPACT_X:
            for dy in self.IMPACT_Y:

                # Do not add the given point itself
                if dx == 0 and dy == 0:
                    continue

                x_new = x + dx
                y_new = y + dy

                # Dot not move into negative coordinates
                if x_new < 0 or y_new < 0:
                    continue

                new_point = (x_new, y_new)
                if new_point not in self.dots and new_point not in self.line_dots:
                    self.dots.append(new_point)

    def _get_new_lines(self):
        """Update the lines based on current dots"""

        self.lines = []
        for _ in range(self.line_num):
            while True:
                new_line = []
                for _ in range(self.line_len):
                    while True:
                        p = choice(self.dots)
                        if p not in new_line:
                            new_line.append(p)
                            break

                if new_line not in self.lines:
                    self.lines.append(new_line)
                    break

    def step(self):
        self.i += 1
        self._get_new_lines()
        self._update_dots()


def plot_game(game, board_size=(50, 50)):
    """
    Plot the current game state

    Args:
        :game: (obj) Instance of the game
    """

    fig, ax = plt.subplots(dpi=300)
    ax.set_aspect('equal')

    for line in game.lines:
        x = []
        y = []

        for point in line:
            x.append(point[0])
            y.append(point[1])

        ax.plot(x, y, color='red', linewidth=0.5)

    for dot in game.dots:
        ax.scatter(dot[0], dot[1], color='black', s=0.3)

    plt.xlim(0, board_size[0])
    plt.ylim(0, board_size[1])
    plt.tight_layout()
    plt.savefig(f"{game.i:05d}.png")
    plt.close('all')


def main():
    start_size = (15, 10)
    plot_size = tuple(c*10 for c in start_size)
    game = Board(start_size, line_num=10, line_len=3)

    for _ in range(165):
        print(game)
        plot_game(game, board_size=plot_size)
        game.step()


if __name__ == '__main__':
    main()
