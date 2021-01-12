# txt2img
# Make images out of basic text.
#
# Copyright (C) 2020-2021, Ty Gillespie. All rights reserved.
# MIT License.

import txt2img


if __name__ == "__main__":
 txt2img.generate(200, 200, "This is an example image", "white", 10, 10, "black", "your_image.png")
