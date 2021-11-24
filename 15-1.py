# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:59:00 2021

@author: curtin
"""
#numpy.savetxt
import numpy as np
a=np.random.rand(5,6)
print(a)

np.savetxt('array.txt',a,fmt='%0.5f',delimiter=',')
This is a test.
