# Data

This directory contains the datasets used for ChatGPT code authorship attribution experiments.

## Contents

```
data/
└── ChatGPT/
    ├── GCJ_2017_Test/              # Google Code Jam 2017 test dataset
    ├── GCJ_2018_Test/              # Google Code Jam 2018 test dataset
    ├── ChatGPT_feature_based.zip   # Dataset for the feature-based approach
    └── ChatGPT_naive.zip           # Dataset for the naive approach
```

## Description

| Dataset | Description |
|---------|-------------|
| **GCJ_2017_Test** | Human-authored C/C++ source codes from the Google Code Jam 2017 competition |
| **GCJ_2018_Test** | Human-authored C/C++ source codes from the Google Code Jam 2018 competition |
| **ChatGPT_feature_based.zip** | Combined human + ChatGPT code samples with labels derived from the feature-based grouping approach |
| **ChatGPT_naive.zip** | Combined human + ChatGPT code samples using naive (session-based) labeling |

## Usage

Unzip the desired dataset and place it in `src/code-imitator-master/data/dataset_2017/` before running feature extraction. See the [main README](../README.md) for full instructions.
