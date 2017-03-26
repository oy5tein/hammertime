# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:03:07 2017

@author: pi
"""

import png
import numpy as np

pngreader = png.Reader('test16b.png')

img = pngreader.read()

print "type: ", img