# 🖼️ Image-Filter
A basic Python image filter project

Coded in my **CMPEN 454: Computer Vision** class at **Penn State** during the **Summer of 2021**.

---

## ✨ Project Overview

This project implements a simple 2D image filtering pipeline using **NumPy**. It includes custom padding (`zero` and `replication`) and convolution logic (with manual 180° filter rotation) for grayscale images. The code demonstrates how image filters like blur, sharpen, and edge detectors can be applied without relying on external image processing libraries.

---

## 📦 Functions Overview

### `pad(img, method='zero')`

Pads a grayscale image using either:
- `'zero'`: Pads with zeros (default)
- `'replication'`: Replicates border pixels

### `myImageFilter(image, filter)`

Applies a custom filter to an image using:
- Manual 180° filter rotation
- Sliding window convolution
- Uses **replication padding**

---

## 🧪 Example Usage

```python
import numpy as np
from filter import myImageFilter

# Sample 5x5 grayscale image
image = np.array([
    [10, 20, 30, 40, 50],
    [15, 25, 35, 45, 55],
    [20, 30, 40, 50, 60],
    [25, 35, 45, 55, 65],
    [30, 40, 50, 60, 70]
])

# 3x3 averaging filter
kernel = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

# Apply the image filter
output = myImageFilter(image, kernel)
print(output)
