# [TOG (SIGGRAPH Asia 2024)] Refined Inverse Rigging: A Balanced Approach to High-fidelity Blendshape Animation

By Stevo Rackovic, Dusan Jakovetic, and Claudia Soares

Published at SIGGRAPH https://dl.acm.org/doi/full/10.1145/3680528.3687670

## Introduction

In this paper, we present an advanced approach to solving the inverse rig problem in blendshape animation, using high-quality corrective blendshapes. Our algorithm focuses on three key areas: ensuring high data fidelity in reconstructed meshes, achieving greater sparsity in weight distributions, and facilitating smoother frame-to-frame transitions. While the incorporation of corrective terms is a known practice, our method differentiates itself by employing a unique combination of 𝑙1 norm regularization for sparsity and a temporal smoothness constraint through roughness penalty, focusing on the sum of second differences in consecutive frame weights. A significant innovation in our approach is the temporal decoupling of blendshapes, which permits simultaneous optimization across entire animation sequences. This feature sets our work apart from existing methods and contributes to a more efficient and effective solution. Our algorithm exhibits a marked improvement in maintaining data fidelity and ensuring smooth frame transitions when compared to prior approaches that either lack smoothness regularization or rely solely on linear blendshape models. In addition to superior mesh resemblance and smoothness, our method offers practical benefits, including reduced computational complexity and execution time, achieved through a novel parallelization strategy using clustering methods. Our results not only advance the state-of-the-art in terms of fidelity, sparsity, and smoothness in inverse rigging but also introduce significant efficiency improvements.

## Installation and Requirements

The python code is made to work on Windows OS, and data can be either created synthetically in Python, or extracted usign Autodesk Maya software (https://www.autodesk.com/products/maya/overview), if an animated avatar is avaliable. 

Required Python modules: 

```python
numpy
scipy
matplotlib
```

## Step 0: (Hyper)Parameter Values

Go to the script Scripts/DataExtraction/Parameters.py, and set the values for hyperparameters for which you want to run experiments. 
Default values aas used in our paper are: 
```python
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
```

## Step 1: Data extraction/preparation

Avatars/animations used in this paper are private, hence we provide scripts for extracting blendshapes of your own MetaHumans (www.unrealengine.com/en-US/metahuman), or creating a random toyset, within ..\Data folder. Choose one of the follwoing two alterantives to proceed (either create synthetic random toydata, or use Maya and MetaHumans platfrom to extract the actual animation)

### 1.1 Creating syhtnetic data 

To create random toydata, run 

```bash
# Create random blendshapes and corrective shapes
python Scripts/DataExtraction/CreateRandomData.py
```
The parameters from Scripts/DataExtraction/Parameters.py that are imported in this script are:
```python
N = 100   # Set here the number of frames of your animaiton
n = 9000  # Set here the number of vertices (times 3) of your avatar. 
m = 60    # Put the number of your character blendhsapes
m1, m2, m3 = 50, 25, 10 # Set the number of corrective terms of first, second and third level, respectively
```
and can be changed if prefered.

### 1.2 Extracting metahuman data 

For this alternative, one needs to have installed Autodesk Maya, and numpy within. Also, need to download MetaHuman avatars. In the paper we used avatar named Omar (www.unrealengine.com/en-US/metahuman).
To extract blendshapes from the existing avatars, open a Python console in Maya, with loaded avatar, and copy the code from the following two scripts sequentially

```bash
# To extract base blendshapes
Scripts/DataExtraction/ExtractBlendshapes.py
# To extract higher order corrective terms
Scripts/DataExtraction/ExtractCorrectiveBlendshapes.py
```

Within the script ExtractBlendshapes.py, specify the parameters as needed
```python
N = 100               # Set here the number of frames of your animaiton
n = 72147             # Set here the number of vertices (times 3) of your avatar. The default value for metahumans is given here
data_dir = r'..\Data' # Put a path to your data directory
```
Within the script ExtractCorrectiveBlendshapes.py, specify the parameters as needed
```python
data_dir = r'..\Data' # Put a path to your data directory
m = 130               # Put the number of your character blendhsapes
m2 = 642              # Put a number of all the controllers under the blendshape node
names = []            # copy the names from a text file here 
```

## Step 2: Eigen/singualr values

After data is extracted, and saved in ../Data, compute singular and eigen values for the blendshape matrix, by running 

```bash
# Compute eigen values and singular values for the blendshape matrix
python Scripts/DataExtraction/ComputeEigenSingularValues.py
```

All the extracted/created data will be stored in ../Data repo.

## Step 3: Training and Inference

The main script for the paper results is ExecuteHolistic.py, that trains a model on specified parameters, and produces predicted weights, storing tehm in ../Predictions repo.
```bash
python Scripts/ExecuteHolistic.py
```
The parameters from Scripts/DataExtraction/Parameters.py that are imported in this script are:
```python
train_frames = 10           # this will take the first 'train_frames' from 'weights.npy' matrix as a training set
num_iter_max = 10           # the maximum number of iterations of the CD solver
num_iter_min = 5            # the minimum number of iterations of the CD solver
lmbd1 =  1                  # the sparsity regularization parameter of the objective funciton
lmbd2 =  1                  # the temporal smoothness regularization parameter of the objective funciton
T = 10                      # Interval batch size
```
The above values are default ones, as the optimal values derived from the paper experiments. If the dimensionality of your avatar is similar to ours, these should work fine.

## Step 4: Plotting the Results

When the predictiosn are made and stored in the previous step, you can run the follwoing script for plotting them and presenting metrics of interest: 
```bash
python Scripts/ShowResults.py
```
The parameters from Scripts/DataExtraction/Parameters.py that are imported in this script are:
```python
train_frames = 10           # this will take the first 'train_frames' from 'weights.npy' matrix as a training set
num_iter_max = 10           # the maximum number of iterations of the CD solver
num_iter_min = 5            # the minimum number of iterations of the CD solver
lmbd1 =  1                  # the sparsity regularization parameter of the objective funciton
lmbd2 =  1                  # the temporal smoothness regularization parameter of the objective funciton
T = 10                      # Interval batch size
```

## Bibliography

If you find our paper code helpful, consider citing:

```bibtex
@inproceedings{10.1145/3680528.3687670,
author = {Rackovi\'{c}, Stevo and Jakoveti\'{c}, Du\v{s}an and Soares, Cl\'{a}udia},
title = {Refined Inverse Rigging: A Balanced Approach to High-fidelity Blendshape Animation},
year = {2024},
isbn = {9798400711312},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3680528.3687670},
doi = {10.1145/3680528.3687670},
booktitle = {SIGGRAPH Asia 2024 Conference Papers},
articleno = {45},
numpages = {9},
keywords = {blendshape animation, inverse rig problem, face segmentation},
location = {Tokyo, Japan},
series = {SA '24}
}
```

### Acknowledgements

This work was partially supported by NOVA LINCS (UIDB/04516/2020) with the financial support of FCT I.P. and Project "Artificial Intelligence Fights Space Debris" No C626449889-0046305 co-funded by Recovery and Resilience Plan and NextGeneration EU Funds, www.recuperarportugal.gov.pt. and by the Ministry of Education of the Republic of Serbia (451-03-9/2021-14/200125).
