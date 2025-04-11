# [TOG (SIGGRAPH Asia 2024)] Refined Inverse Rigging: A Balanced Approach to High-fidelity Blendshape Animation

By Stevo Rackovic, Dusan Jakovetic, and Claudia Soares

Published at SIGGRAPH https://dl.acm.org/doi/full/10.1145/3680528.3687670

## Data extraction/preparation

Avatars/animations used in this paper are private, hence we provide scripts for extracting blendshapes of your own MetaHumans, or creating a random toyset, within ... folder.

To extract blendshapes from the existing avatars, run the following commands

```bash
# Extract base blendshapes
python Scripts/ExtractBlendshapes.py
# Extract higher order corrective terms
python Scripts/ExtractCorrectiveBlendshapes.py
```

Alternativelly, to create random toydata, run 

```bash
# Create random blendshapes and corrective shapes
python Scripts/CreateRandomData.py
```

After data is extracted, and saved in ../Data, compute singular and eigen values for the blendshape matrix, by running 

```bash
# Compute eigen values and singular values for the blendshape matrix
python Scripts/ComputeEigenSingularValues.py
```

All teh extracted/created data will be stored in ../Data repo.

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
abstract = {In this paper, we present an advanced approach to solving the inverse rig problem in blendshape animation, using high-quality corrective blendshapes. Our algorithm focuses on three key areas: ensuring high data fidelity in reconstructed meshes, achieving greater sparsity in weight distributions, and facilitating smoother frame-to-frame transitions. While the incorporation of corrective terms is a known practice, our method differentiates itself by employing a unique combination of l1 norm regularization for sparsity and a temporal smoothness constraint through roughness penalty, focusing on the sum of second differences in consecutive frame weights. A significant innovation in our approach is the temporal decoupling of blendshapes, which permits simultaneous optimization across entire animation sequences. This feature sets our work apart from existing methods and contributes to a more efficient and effective solution. Our algorithm exhibits a marked improvement in maintaining data fidelity and ensuring smooth frame transitions when compared to prior approaches that either lack smoothness regularization or rely solely on linear blendshape models. In addition to superior mesh resemblance and smoothness, our method offers practical benefits, including reduced computational complexity and execution time, achieved through a novel parallelization strategy using clustering methods. Our results not only advance the state-of-the-art in terms of fidelity, sparsity, and smoothness in inverse rigging but also introduce significant efficiency improvements1.},
booktitle = {SIGGRAPH Asia 2024 Conference Papers},
articleno = {45},
numpages = {9},
keywords = {blendshape animation, inverse rig problem, face segmentation},
location = {Tokyo, Japan},
series = {SA '24}
}
