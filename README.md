# 🧬 Annotation Transfer Across the Microscope

This project focuses on **transferring annotation information across microscope magnification levels** — for example, from 1000x to 400x and 100x — to support multi-scale data labeling and efficient patch-level tracking. The goal is to enable **cross-scale annotation consistency** without the need to re-label at each scale manually.

---

## 🔍 Overview

In digital microscopy, especially in hematological or pathological studies, it's often required to:
- Label regions of interest (e.g., infected blood cells) at **1000x** magnification.
- Match or project these labels to **lower magnification views** (e.g., 400x or 100x) for context-aware data interpretation or training machine learning models.

This tool supports:
- Manual or semi-automated coordinate registration between magnification scales.
- Patch image extraction and overlay visualization.
- Coordinate conversion for annotation transfer.
- Integration with the **Olympus microscope tracking app**.

---

## 📦 Features

- ✅ Annotation projection across 100x, 400x, and 1000x magnifications
- ✅ Support for **image coordinate transformation**
- ✅ Compatible with microscope images collected using the **Multi-Scale Olympus Microscope App**
- ✅ MATLAB implementation with interactive GUI (requires App Designer)
- ✅ Export transferred annotations for downstream ML pipelines

---

## 🧰 Requirements

- python
- OpenCV
- Computer Vision Toolbox

---

## 🚀 Getting Started

1. Load high-magnification (1000x) image and corresponding annotations.
2. Select or compute transformation matrix to lower magnification levels.
3. Transfer and visualize annotations across views.
4. Export new annotated views as image-label pairs.

---

## 📚 Related Projects

- **[Multi-Scale Data Collection App for Olympus Microscope](https://github.com/your-repo-link)** — Used to acquire images and track patches across microscope levels.
- **Malaria Dataset Preparation Toolkit** (used for building ML-ready datasets from multi-scale microscopy)

---

## 📖 Citation

If you find this project useful, please cite our related paper:

```bibtex
@INPROCEEDINGS{9878617,
  author    = {Sultani, Waqas and Nawaz, Wajahat and Javed, Syed and Danish, Muhammad Sohail and Saadia, Asma and Ali, Mohsen},
  title     = {Towards Low-Cost and Efficient Malaria Detection},
  booktitle = {2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2022},
  pages     = {20655-20664},
  doi       = {10.1109/CVPR52688.2022.02003}
}
