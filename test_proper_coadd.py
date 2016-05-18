# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:06:14 2016

@author: bruno
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.stats import stats

from astropy.convolution import convolve, convolve_fft
from astropy.time import Time
from astropy.io import fits

from imsim import simtools
import propercoadd as pc


N = 128  # side
test_dir = os.path.abspath('./test_images/one_star')
#x = [np.random.randint(low=10, high=N-10) for j in range(100)]
#y = [np.random.randint(low=10, high=N-10) for j in range(100)]
#xy = [(x[i], y[i]) for i in range(100)]
now = '2016-05-17T00:00:00.1234567'
t = Time(now)

filenames = []
for i in range(30):
    SN = i + 2.
    m = simtools.delta_point(N, center=True)
    im = simtools.image(m, N, t_exp=1, FWHM=10, SN=SN, bkg_pdf='gaussian')

    filenames.append(
        simtools.capsule_corp(im, t, t_exp=1, i=i, zero=3.1415, path=test_dir))

for afile in filenames:
    px = pc.SingleImage(afile, imagefile=True)


#im_con = convolve(im, psf)

#im_con_fft = convolve_fft(im, psf)

#plt.figure()
#plt.subplot(121)
#plt.imshow(im_con, interpolation='none')
#plt.subplot(122)
#plt.imshow(im_con_fft, interpolation='None')
#plt.title('conv - fft')
#plt.show()


