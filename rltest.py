#!/usr/local/bin/python3

import RLtoolkit.Tiles.tiles as tiles

import numpy as np
from PIL import Image

sz = (18, 22)
# docs:  http://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.size
im = Image.open('gridworld-bridge.png').resize(sz).quantize(colors=2)

# im.show()

im = np.array(im.getdata()).astype(np.float32).reshape(sz[::-1])

print(im)
