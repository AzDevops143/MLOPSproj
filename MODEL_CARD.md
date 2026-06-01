---
language:
- en
license: other
library_name: transformers
tags:
- text-classification
- emotion-detection
- distilbert
- mlops
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
---

# Model Card: MLOps Emotion DistilBERT

## Model Description
This is a fine-tuned version of distilbert-base-uncased for multi-class emotion classification. It was trained as part of an end-to-end MLOps pipeline assignment for the IIT Jodhpur PGD AI Program. The model takes English text as input and predicts one of six basic emotions.

- Base Model: distilbert-base-uncased
- Task: Text Classification
- Language: English
- License: IIT Jodhpur (All Rights Reserved)

## Intended Uses & Limitations
This model is intended for educational purposes and basic emotion detection in short English text. It may not generalize well to complex, nuanced, or highly domain-specific language.

## Training Data
The model was fine-tuned on the dair-ai/emotion dataset. 
- Training Set: 16,000 samples
- Validation Set: 2,000 samples
- Classes: 
  - 0: Sadness
  - 1: Joy
  - 2: Love
  - 3: Anger
  - 4: Fear
  - 5: Surprise

## Training Procedure
The model was trained in a Kaggle Notebook utilizing dual T4 GPUs. Hyperparameter tuning was conducted to compare multiple versions, tracked via Weights & Biases. 

The following hyperparameters were used for the primary version:
- Learning Rate: 3e-5
- Epochs: 2
- Train Batch Size: 16
- Eval Batch Size: 16
- Optimizer: AdamW

## Evaluation Results
Model performance was evaluated on the validation split of the dataset. Metrics such as Accuracy and Weighted F1-score were monitored throughout training and logged directly to the project's W&B Dashboard.

## Pipeline Integration
This model is containerized using Docker for inference and is integrated into a continuous CI/CD pipeline orchestrated via GitHub Actions.

- GitHub Repository: https://github.com/AzDevops143/MLOPSproj
- W&B Dashboard: https://wandb.ai/srajam696-charan/mlops-assignment3/overview
