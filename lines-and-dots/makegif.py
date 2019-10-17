#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Aaron Dettmann

import sys
import argparse
import os

import imageio


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('imagefiles', nargs='+',  help="image files to join")
    parser.add_argument("-o", "--output", help="output file name", default="movie.gif")
    args = parser.parse_args()

    imagefiles = args.imagefiles
    gif_file = args.output

    print(f"Writing to file {gif_file}...")
    num_files = len(imagefiles)

    with imageio.get_writer(gif_file, mode='I', duration=0.05) as writer:
        for i, filename in enumerate(imagefiles, start=1):
            print(f"Adding {filename}... ", end='')
            sys.stdout.flush()

            image = imageio.imread(filename)
            writer.append_data(image)
            print(f"done ({100*(i/num_files):6.2f} %)")

    mp4_file = gif_file.replace('gif', "mp4")
    conv2mp4 = 'ffmpeg -i ' + gif_file + ' -movflags faststart ' + \
               '-pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ' + mp4_file
    os.system(conv2mp4)


if __name__ == '__main__':
    main()
