# Grains of Saliency

Official repository for the paper: Colton R. Crum, Samuel Webster, Adam Czajka, "Grains of Saliency: Optimizing Saliency-based Training of Biometric Attack Detection Models," IEEE/IAPR International Joint Conference on Biometrics (IJCB), September 15-18, 2024, Buffalo, NY, USA 

Paper: [IEEEXplore] | [ArXiv pre-print](https://arxiv.org/abs/2405.00650)

## Abstract

Incorporating human-perceptual intelligence into model training has shown to increase the generalization capability of models in several difficult biometric tasks, such as presentation attack detection (PAD) and detection of synthetic samples. After the initial collection phase, human visual saliency (e.g., eye-tracking data, or handwritten annotations) can be integrated into model training through attention mechanisms, augmented training samples, or through human perception-related components of loss functions. Despite their successes, a vital, but seemingly neglected, aspect of any saliency-based training is the level of salience granularity (e.g., bounding boxes, single saliency maps, or saliency aggregated from multiple subjects) necessary to find a balance between reaping the full benefits of human saliency and the cost of its collection. In this paper, we explore several different levels of salience granularity and demonstrate that increased generalization capabilities of PAD and synthetic face detection can be achieved by using simple yet effective saliency post-processing techniques across several different CNNs.

## Installation and Usage

...

## Citations

IJCB 2024 paper:

```
@InProceedings{Crum_IJCB_2024,
  author    = {Colton R. Crum and Samuel Webster and Adam Czajka},
  booktitle = {The IEEE/IAPR International Joint Conference on Biometrics (IJCB)},
  title     = {{Grains of Saliency: Optimizing Saliency-based Training of Biometric Attack Detection Models}},
  year      = {2024},
  address   = {Buffalo, NY, USA},
  month     = {September 15-18},
  pages     = {1-8},
  publisher = {IEEE}
}
```

This GitHub repository:

```
@Misc{ND_GrainsOfSaliency_GitHub,
  howpublished = {\url{https://github.com/CVRL/GrainsOfSaliency/}},
  note         = {Accessed: X},
  title        = {{Grains of Saliency: Optimizing Saliency-based Training of Biometric Attack Detection Models (IJCB 2024 paper repository)}},
  author       = {Colton R. Crum and Samuel Webster and Adam Czajka},
}
```

## License

...

...
