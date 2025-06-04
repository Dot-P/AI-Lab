# AI-Lab

This repository serves as a sandbox for implementing an open-world recognition framework built around masked Autoencoders (ViT-MAE) with streaming discovery of new classes.

## Objective

The project aims to combine self-supervised pre-training with ViT-MAE, energy-based unknown detection, and incremental clustering so that novel categories can be discovered on the fly. The eventual goal is an end-to-end system that can recognize known objects, detect out-of-distribution examples, and continually grow its label set with minimal supervision.

## Planned Modules

- **Pre-training**: Pre-train a ViT model following the [Masked Autoencoders](https://github.com/facebookresearch/mae) approach by He *et al.* This stage provides representations that generalize well.
- **OOD Detection Branches**: Use energy-based scoring as described in "Energy-based Out-of-distribution Detection" by Liu *et al.* to flag unknown samples.
- **3-Way-BIRCH Clustering**: For streaming data, cluster unknown samples into potential new classes using an incremental BIRCH variant that handles known, unknown, and ambiguous examples.
- **Weight Imprinting**: Initialize new-class weights from cluster centroids as proposed in imprinting-based recognition methods.
- **Spectral Regularization**: Stabilize the classifier by adding spectral norm regularization during training.

## Basic Usage

This repository is still under construction, but the intended workflow is:

1. Run pre-training to create a ViT-MAE checkpoint.
2. Fine-tune with the energy-based OOD branch enabled.
3. Continuously feed streaming data; unknown samples are clustered via 3-Way-BIRCH.
4. When clusters are stable, apply weight imprinting to register them as new classes.

More details will be added as the individual modules are implemented.

## References

- K. He, X. Chen, S. Xie, Y. Li, P. Dollár, and R. Girshick. "Masked Autoencoders Are Scalable Vision Learners," 2021. <https://arxiv.org/abs/2111.06377>
- W. Liu, X. Wang, J. Owens, and Y. Li. "Energy-based Out-of-distribution Detection," NeurIPS 2020. <https://arxiv.org/abs/2010.03759>
- BIRCH: Zhang, Ramakrishnan, and Livny. "BIRCH: An Efficient Data Clustering Method for Very Large Databases," 1996.
- Imprinting: Qi, Brown, and Lowe. "Low-shot learning with imprinted weights," CVPR 2018.

