# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:03:07 2017

@author: pi
"""

import png
import numpy as np
from scipy.ndimage import gaussian_filter

w=1920
h=1080
np.random.seed(12345)

x=np.random.rand(h,w,3)
y=x

z= (2**16 * ((y-y.min())/y.ptp())).astype(np.uint16) 


with open('test16b.png','wb') as f:
    w = png.Writer(width=z.shape[1],height=z.shape[0],bitdepth=16)
    z2list = z.reshape(-1,z.shape[1]*z.shape[2]).tolist()
    w.write(f,z2list)
