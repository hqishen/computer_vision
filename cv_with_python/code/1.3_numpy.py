#!/usr/bin/env python
# coding=utf-8

from PIL import Image
from numpy import *
from pcv import imtools
from pylab import *

img = array(Image.open("/home/sundae/Pictures/view_1.png").convert('L'))
figure()
imshow(img)
title('origin')

img2 ,cdf = imtools.histeq(img)
figure()
imshow(img2)
title('histogram')
show()

print(img2, cdf)

