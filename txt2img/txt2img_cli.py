# txt2img
# Make images out of basic text.
#
# Copyright (C) 2020-2021, Ty Gillespie. All rights reserved.
# MIT License.

import txt2img

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('width', type=int, help='The width of the new image')
parser.add_argument('height', type=int, help='The height of the new image')
parser.add_argument('text', help='The text to render on the image')
parser.add_argument('--bg', default='white', help='Background colour')
parser.add_argument('-x', '--text-x', type=int, default=10, help='The upper x coordinate of the text')
parser.add_argument('-y', '--text-y', type=int, default=10, help='The upper y coordinate of the text')
parser.add_argument('--fg', default='black', help='Text foreground colour')
parser.add_argument('-f', '--filename', type=argparse.FileType('wb'), default='image.png', help='Where to save the image')

if __name__ == '__main__':
 args = parser.parse_args()
 txt2img.generate(args.width, args.height, args.text, args.bg, args.text_x, args.text_y, args.fg, args.filename)
 print("Done!")
