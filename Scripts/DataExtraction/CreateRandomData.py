# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:52:23 2023

@author: Stevo Rackovic

"""

import os
import numpy as np
import random
from Parameters import T, N, n, m, m1, m2, m3
n = n//3*3 # To make sure it is divisible by 3

print('\nThe script for creating synthetic data running...\n')
print('Created random synthetic data with the following properties:')
print('Number of vertices in the mesh: ', int(n/3))
print('Number of blendshapes: ', m)
print('Number of corrective terms of the first level: ', m1)
print('Number of corrective terms of the second level: ', m2)
print('Number of corrective terms of the third level: ', m3)
print('Number of the frames in the animation: ', N)

work_dir = os.getcwd()
data_dir = os.path.join(work_dir,'Data')
print('Working directory: ', work_dir)
print('Data directory: ', data_dir)

deltas = np.random.randn(n,m)
neutral = np.random.randn(n)
W = np.zeros((N,m))
for j in range(m):
    w_i = np.clip(np.random.randn()*0.5, 0, 1)
    w = [w_i]
    for i in range(N-1):
        increment = np.random.randn()*0.1
        w_i = np.clip( w[i]+increment, 0, 1)
        w.append(w_i)
    W[:,j] += w

np.save(os.path.join(data_dir,'weights.npy'),W)
np.save(os.path.join(data_dir,'deltas.npy'),deltas)
np.save(os.path.join(data_dir,'neutral.npy'),neutral)

bs1, bs2, bs3 = np.random.randn(m1,n), np.random.randn(m2,n), np.random.randn(m3,n)
keys1, keys2, keys3 = np.array([sorted(random.sample(range(m), 2)) for _ in range(m1)]), np.array([sorted(random.sample(range(m), 3)) for _ in range(m2)]), np.array([sorted(random.sample(range(m), 4)) for _ in range(m3)])

np.save(os.path.join(data_dir,'bs1.npy'),bs1)
np.save(os.path.join(data_dir,'bs2.npy'),bs2)
np.save(os.path.join(data_dir,'bs3.npy'),bs3)
np.save(os.path.join(data_dir,'keys1.npy'),keys1)
np.save(os.path.join(data_dir,'keys2.npy'),keys2)
np.save(os.path.join(data_dir,'keys3.npy'),keys3)

print('\nData created successfully, stored at ', data_dir)


