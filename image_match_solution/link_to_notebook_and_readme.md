# Data Science Project: Satellite Image Analysis

# LINK TO KAGGLE NOTEBOOK:
https://www.kaggle.com/katepynka/template-matching-solution

## Overview
This project focuses on the analysis of satellite images to identify and compare specific geographical features.

## Methodology
The project employs template matching and feature detection algorithms (like SIFT) for image comparison. I choose this solution because the dataset includes images in different seasons or condition.
It includes preprocessing steps such as resizing, compressing and grayscale conversion, followed by feature extraction and matching.

## Key Features
- **Image Preprocessing**: Resizing images for uniformity and converting them to grayscale to reduce computational complexity.
- **Feature Extraction**: Using SIFT (Scale-Invariant Feature Transform) to extract distinctive features from each image.
- **Feature Matching**: Comparing features of different images to identify potential matches and assess similarities.
- **Parallel Processing**: Implementing `ProcessPoolExecutor` for efficient handling of multiple image comparisons.

## Dataset
Deforestation in Ukraine from Sentinel2 data (https://www.kaggle.com/datasets/isaienkov/deforestation-in-ukraine/data)

## Requirements
To run the notebook, you need several Python libraries, as listed in the `requirements.txt` file. 

