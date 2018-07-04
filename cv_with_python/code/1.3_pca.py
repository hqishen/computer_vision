#!/usr/bin/env python
# coding=utf-8

from PIL import Image
from pylab import *
from numpy import *
# import matplotlib.plot as plt
from pcv import pca
from pcv import imtools

impath = "/home/sundae/workspace/computer_vision/cv_with_python/data/a_thumbs"

def _main():
    im_list = imtools.get_imlist(impath)
    im = array(Image.open(im_list[0]))
    m, n = im.shape[0:2]
    imnbr = len(im_list)
#    print("imlist size is %d width %s height %s" %(imnbr, m, n))
    immatrix = array(
        [
        array(Image.open(im)).flatten()
        for im in im_list
        ]
    , 'f')

    V, S, immean = pca.pca(immatrix)
    figure()
    gray()
    subplot(2, 4, 1)

    imshow(immean.reshape(m, n))
    for i in range(7):
        subplot(2, 4, i + 2)
        imshow(V[i].reshape(m,n))
    show();

if __name__ == "__main__":
    _main()

