#!/usr/local/bin/python3

import numpy as np
from PIL import Image

def returnmatrix(file, sz, start, finish):
    # docs:  http://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.size
    im = Image.open('gridworld-bridge.png').resize(sz[::-1]).quantize(colors=2)
    # im.show()
    # im = np.array(im.getdata()).astype(np.float32).reshape(sz[::-1])
    im = np.asarray(im).astype(float, copy = True)
    im[start] = 0.5
    im[finish] = 0.5

    return im
