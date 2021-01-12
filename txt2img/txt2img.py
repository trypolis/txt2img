# txt2img
# Make images out of basic text.
#
# Copyright (C) 2020-2021, Ty Gillespie. All rights reserved.
# MIT License.

from PIL import Image, ImageDraw

def generate(width, height, text, bg="white", text_x=10, text_y=10, fg="black", filename="image.png"):
 """Generate an image.
 Parems:
  width: the width (in pixels), of the image.
  height: the height (in pixels) of the image.
  text: the text that goes on the image.
  bg (optional): the background color (by default white).
  text_x (optional): the top x of the text. By default 10.
  text_y (optional): the top y of the text. By default 10.
  fg (optional): the foreground color. By default black.
  filename (optional): the output filename (by default image.png).
 """
 i = Image.new("RGB", (width, height), color=bg)
 d = ImageDraw.Draw(i)
 d.text((text_x, text_y), text, fill=fg)
 i.save(filename)
