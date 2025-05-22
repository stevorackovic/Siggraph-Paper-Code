# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:26:48 2024

@author: Stevo Rackovic

"""

train_frames = 20           # this will take the first 'train_frames' from 'weights.npy' matrix as a training set
num_iter_max = 10           # the maximum number of iterations of the CD solver
num_iter_min = 5            # the minimum number of iterations of the CD solver
lmbd1 =  1                  # the sparsity regularization parameter of the objective funciton
lmbd2 =  1                  # the temporal smoothness regularization parameter of the objective funciton
T = 10                      # Interval batch size
N = 100                     # Set here the number of frames of your animaiton
n = 9000                    # Set here the number of vertices (times 3) of your avatar. 
m = 60                      # Put the number of your character blendhsapes
m1, m2, m3 = 50, 25, 10     # Set the number of corrective terms of first, second and third level, respectively
