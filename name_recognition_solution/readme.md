## Overview
This project aims to train a Named Entity Recognition (NER) model for identifying mountain names within text. 
The NER model is built using state-of-the-art natural language processing techniques and can be used to extract mountain names from unstructured text data.

## Dataset
The dataset used for training and evaluation is not publicly available. It was collected and labeled for the specific purpose of this project.
It includes facts about mountains, search prompt or even typo to get real-world scenario.

## Model Architecture
The model architecture chosen for this task is Roberta, a pre-trained model fine-tuned for NER on our dataset.

## Training
The model training process involves the following steps:

1. Data Preprocessing: The labeled dataset is preprocessed to prepare it for model training.
2. Model Fine-tuning: The pre-trained model is fine-tuned on the labeled dataset for NER.
3. Model Evaluation: The model is evaluated on a validation dataset to measure its performance.
4. Model Saving: The trained model weights are saved for later use.

## Inference
To use the trained model for inference, you can refer to the inference script in this repository. 

## ISSUE
Unfortunately, the model doesn't work as expected. The guess - I should look into labeling logic. If I have change to redo it, I would train custom model on dataset of mountains name from here - https://github.com/You-now-Who/dataset/blob/main/List%20of%20Mounains/Mountain.csv.

# Very important
Please, download 'very_important_image.jpg'.

## Demo

For a quick demonstration of how to use the model you can refer to the Jupyter notebook `pre_train_roberta_model_solution.ipynb` provided in this repository. 
The notebook provides step-by-step instructions and code examples.

### Set up the environment:
```
pip install -r requirements.txt
```


