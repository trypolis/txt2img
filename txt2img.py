# txt2img
# Make images out of basic text.
#
# Copyright (C) 2020, Ty Gillespie. ALl rights reserved.
# MIT License.

from PIL import Image, ImageDraw


def generate(
    width: int,
    height: int,
    text: str,
    bg: str = "white",
    text_x: int = 10,
    text_y: int = 10,
    fg: str = "black",
    filename: str = "image.png",
):
    i = Image.new("RGB", (width, height), color=bg)
    d = ImageDraw.Draw(i)
    d.text((text_x, text_y), text, fill=fg)
    i.save(filename)
