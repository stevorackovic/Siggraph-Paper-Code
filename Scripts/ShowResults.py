# -*- coding: utf-8 -*-
"""
Created on Wed Oct 4 16:54:17 2023

@author: Stevo Rackovic

"""

print('\nThe script for plotting the results is running...\n')
import numpy as np
import os
import matplotlib.pyplot as plt
from DataExtraction.Parameters import train_frames, num_iter_max, num_iter_min, lmbd1, lmbd2, T
work_dir = os.getcwd()
data_dir = os.path.join(work_dir,'Data')
predictions_dir = os.path.join(work_dir,'Predictions')
print('Working directory: ', work_dir)
print('Data directory: ', data_dir)
print('Predictions directory: ', predictions_dir)
from HelperFunctions import quartic_rig, ctr_order, rmse, smoothness

neutral = np.load(os.path.join(data_dir,'neutral.npy'))
deltas = np.load(os.path.join(data_dir,'deltas.npy'))
n,m = deltas.shape
bs1  = np.load(os.path.join(data_dir,'bs1.npy'))
bs2  = np.load(os.path.join(data_dir,'bs2.npy'))
bs3  = np.load(os.path.join(data_dir,'bs3.npy'))
keys1  = np.load(os.path.join(data_dir,'keys1.npy'))
keys2  = np.load(os.path.join(data_dir,'keys2.npy'))
keys3  = np.load(os.path.join(data_dir,'keys3.npy'))
order = ctr_order(deltas)

print('Dimensions of the data:')
print('Number of vertices in the mesh: ', int(n/3))
print('Number of blendshapes: ', m)
print('Number of corrective terms of the first level: ', len(keys1))
print('Number of corrective terms of the second level: ', len(keys2))
print('Number of corrective terms of the third level: ', len(keys3))

weights = np.load(os.path.join(data_dir,'weights.npy'))
weights_train = weights[:train_frames]
N = len(weights_train)
target_meshes = np.array([quartic_rig(C, deltas, bs1, bs2, bs3, keys1, keys2, keys3) for C in weights_train]).T

print('Total animation frames: ', len(weights))
print('Training animation frames: ', len(weights_train))

filename = f'Pred_num_iter_max_{num_iter_max}_num_iter_min_{num_iter_min}_lmbd1_{lmbd1}_lmbd2_{lmbd2}_T_{T}.npy'
Predictions = np.load(os.path.join(predictions_dir, filename)).T
pred_meshes = np.array([quartic_rig(C, deltas, bs1, bs2, bs3, keys1, keys2, keys3) for C in Predictions]).T

fig, ax = plt.subplots(2,1,figsize=(10,5),sharex=True,sharey=True)
ax[0].plot(weights_train,color='r',alpha=.25)
ax[1].plot(Predictions,color='g',alpha=.25)
ax[0].set_ylim(-0.05,1.05)
ax[0].set_ylabel('Activation')
ax[1].set_ylabel('Activation')
ax[1].set_xlabel('Frames')
ax[0].set_title('Grund-truth weigths activations')
ax[1].set_title('Predicted weigths activations')
plt.savefig(os.path.join(work_dir,'Figures','PredictedWeigthsActivations.pdf'))
plt.show()

mesh_errors_mean, mesh_errors_max = [], []
for frame in range(N):
    me1, me2, me3 = rmse(target_meshes[:,frame], pred_meshes[:,frame])
    mesh_errors_mean.append(me1)
    mesh_errors_max.append(me2)
cardinality = [np.sum(Predictions[frame]>0) for frame in range(len(Predictions))]
gt_cardinality = np.mean([np.sum(weights_train[frame]>0) for frame in range(len(weights_train))])
norm = [np.linalg.norm(Predictions[frame],1) for frame in range(len(Predictions))]
gt_norm = np.mean([np.linalg.norm(weights_train[frame],1) for frame in range(len(weights_train))])
roughness = smoothness([Predictions],m)
gt_roughness = np.mean(smoothness([weights_train],m))

fig, ax = plt.subplots(1,5,figsize=(15,3))
fig.subplots_adjust(wspace=0.4)
bp0 = ax[0].boxplot(mesh_errors_max,patch_artist = True)
ax[0].set_ylabel('Max Mesh Error')
bp1 = ax[1].boxplot(mesh_errors_mean,patch_artist = True)
ax[1].set_ylabel('Mean Mesh Error')
bp2 = ax[2].boxplot(cardinality,patch_artist = True)
ax[2].plot(np.ones(3)*gt_cardinality,color='r')
ax[2].set_xlim(0.5,1.5)
ax[2].set_ylabel('Cardinality')
bp3 = ax[3].boxplot(norm,patch_artist = True)
ax[3].plot(np.ones(3)*gt_norm,color='r')
ax[3].set_xlim(0.5,1.5)
ax[3].set_ylabel('L1 norm')
bp4 = ax[4].boxplot(roughness,patch_artist = True)
ax[4].plot(np.ones(3)*gt_roughness,color='r')
ax[4].set_xlim(0.5,1.5)
ax[4].set_ylabel('Roughness')
for i in range(5):
    ax[i].spines['right'].set_visible(False)
    ax[i].spines['top'].set_visible(False)
    ax[i].set_xticks([])
    ax[i].set_xticklabels([])
for bp in [bp0, bp1, bp2, bp3, bp4]:
    for patch in bp['boxes']: 
        patch.set_facecolor('tab:green')
        patch.set_linewidth(0.4)
    for median in bp['medians']: 
        median.set(color ='k')
    for flier in bp['fliers']: 
        flier.set(markeredgecolor ='tab:green',markersize =4)
    for whisker in bp['whiskers']: 
        whisker.set(linewidth = 0.4)
    for cap in bp['caps']: 
        cap.set(linewidth = 0.5)
fig.suptitle('Resulting metrics for the predicted weights')
plt.savefig(os.path.join(work_dir,'Figures','ResultingMetricsPredictedWeights.pdf'))
plt.show()
print('\nFigures made and stored at ', os.path.join(work_dir,'Figures'))
