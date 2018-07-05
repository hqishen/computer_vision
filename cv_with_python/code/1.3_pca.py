#!/usr/bin/env python
# coding=utf-8
import sys
import pickle
from PIL import Image
from pylab import *
from numpy import *

sys.path.append('..')
from pcv_tools import pca
from pcv_tools import imtools


impath = "/home/sundae/workspace/computer_vision/cv_with_python/source_data/a_thumbs"

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

    print(immean)
    # save result to the files
    with open("font_pca_modes.pkg", 'wb') as f:
        pickle.dump(immean, f)
        pickle.dump(V, f)

    ''' # load contents from file with name is .pkg
    with open("font_pca_modes.pkg", 'rb') as f:
        immean  = pickle.load(f)
        V = pickle.load(f)
    '''


if __name__ == "__main__":
    _main()

