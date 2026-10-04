# Data Classification Using AI

## Project Description

This project is a basic machine learning classification system developed as part of the DecodeLabs Artificial Intelligence Internship.

The project uses the **Iris dataset** and the **K-Nearest Neighbors (KNN)** classification algorithm to classify flowers into three species:

- Setosa
- Versicolor
- Virginica

The model uses four flower measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

## Features

- Loads and explores the Iris dataset
- Splits the dataset into training and testing sets
- Uses 80% of the data for training and 20% for testing
- Trains a KNN classifier with 5 nearest neighbors
- Predicts flower species using unseen test data
- Calculates model accuracy
- Displays a confusion matrix
- Displays precision, recall, and F1-score
- Predicts the species of a new flower

## Technologies Used

- Python
- Scikit-learn
- K-Nearest Neighbors (KNN)
- Visual Studio Code

## How to Run

### 1. Install Scikit-learn

```bash
pip install scikit-learn
```

### 2. Run the Program

```bash
python iris_classifier.py
```

If using a specific Python 3.11 installation:

```bash
py -3.11 iris_classifier.py
```

## Dataset

The project uses the built-in Iris dataset provided by Scikit-learn.

The dataset contains:

- 150 flower samples
- 4 input features
- 3 flower species

## Model

The project uses the **K-Nearest Neighbors (KNN)** classification algorithm with:

```text
K = 5
```

The dataset is divided into:

```text
Training Data: 80%
Testing Data:  20%
```

## Evaluation

The model is evaluated using:

- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-score

With `random_state=42`, the model achieved **100% accuracy on the 30 test samples in this particular train/test split**.

## Project Structure

```text
Project 2/
├── iris_classifier.py
└── README.md
```

## Internship Information

**Internship:** Artificial Intelligence  
**Organization:** DecodeLabs  
**Project:** Project 2 - Data Classification Using AI
