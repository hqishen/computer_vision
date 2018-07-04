#!/usr/bin/env python
# coding=utf-8

import numpy as np
from PIL import Image
from pylab import *


def _main():
    i = 0; j = 2; k = 0
    im1 = array(Image.open("/home/sundae/Pictures/view_1.png").convert('L'))
    figure()
    imshow(im1)
    im2 = 255 - im1;
    figure()
    imshow(im2)
    im3 = (100.0  / 255) * im1 + 100 # clamp to interval 100...200
    figure()
    imshow(im3)
    im4 = 255.0 * (im1 / 255.0) **2
    figure()
    imshow(im4)
    show()
    print(int(im1.min()), int(im1.max()))


if __name__ == "__main__":
    _main();

