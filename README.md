# Estimate Illumination Correction Matrix

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![tests](https://github.com/fmi-faim/eicm/workflows/tests/badge.svg)](https://github.com/fmi-faim/eicm/actions)
[![codecov](https://codecov.io/gh/fmi-faim/eicm/branch/main/graph/badge.svg)](https://codecov.io/gh/fmi-faim/eicm)

Two functions to estimate illumination correction matrices from reference
illumination samples.

* [`gaussian_blur.py`](./src/eicm/estimator/gaussian_blur.py): simply
  applies a Gaussian blur
* [`gaussian2D_fit.py`](./src/eicm/estimator/gaussian2D_fit.py): fits a 2D
  Gaussian

## Installation

```shell
pip install git+https://github.com/fmi-faim/eicm@v0.1.0
```
This installs tag [v0.1.0](https://github.com/fmi-faim/eicm/tree/v0.1.0).
