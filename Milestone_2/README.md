# 🤖 Milestone 2 – AI/ML Soil Analysis Engine

## 1. Overview

Milestone 2 focused on developing the **AI/ML Soil Analysis Engine** for the Soil Analytics System.

The main purpose of this milestone was to transform the cleaned and prepared dataset from Milestone 1 into an intelligent analysis system using:

* Deep Learning
* Convolutional Neural Networks (CNN)
* ResNet-50
* Structured Machine Learning
* Feature Importance Analysis
* Explainable AI (XAI)
* Grad-CAM

The milestone contains two major analysis approaches:

1. **Image-based soil classification**
2. **Structured soil parameter analysis**

These components form the AI foundation that was later integrated into the Farmer PWA in Milestone 3.

---

# 2. Objectives

The main objectives of Milestone 2 were:

* To develop a CNN-based soil image classification model.
* To classify soil images into different soil categories.
* To use ResNet-50 for Deep Learning-based classification.
* To develop a structured Machine Learning analysis system.
* To analyze important soil and environmental parameters.
* To determine feature importance.
* To implement Explainable AI.
* To use Grad-CAM to visualize important image regions.
* To save the trained model for later integration with the Farmer PWA.

---

# 3. AI/ML System Architecture

The Milestone 2 system consists of two major paths:

```text
                         AI/ML SOIL ANALYSIS ENGINE
                                    │
                  ┌─────────────────┴─────────────────┐
                  │                                   │
             Soil Image                       Structured Data
                  │                                   │
                  ↓                                   ↓
             ResNet-50                       ML Analysis Model
                  │                                   │
                  ↓                                   ↓
          Soil Classification                Feature Analysis
                  │                                   │
                  └─────────────────┬─────────────────┘
                                    ↓
                             Analysis Results
                                    │
                                    ↓
                              Explainability
```

---

# 4. CNN-Based Soil Image Classification

## 4.1 CNN Model

A **Convolutional Neural Network (CNN)** was developed to classify soil images.

The model used was **ResNet-50**.

ResNet-50 is a deep neural network architecture that uses residual connections to allow deeper networks to be trained effectively.

The model was trained to classify the seven soil categories prepared during M1:

* Alluvial
* Arid
* Black
* Laterite
* Mountain
* Red
* Yellow

---

# 5. ResNet-50 Model

The ResNet-50 model was used as the main image classification model.

The model receives a soil image as input and processes the image through multiple convolutional layers.

The final classification layer produces the predicted soil class.

### CNN Workflow

```text
Soil Image
     ↓
Image Preprocessing
     ↓
ResNet-50
     ↓
Feature Extraction
     ↓
Classification Layer
     ↓
Predicted Soil Type
     ↓
Confidence Score
```

---

# 6. Model Files

The trained CNN model files were saved for later use.

```text
CNN_Model/
│
├── best_resnet50_soil_model.pth
└── resnet50_soil_model.pth
```

The `.pth` files contain the trained PyTorch model weights.

The best-performing saved model was retained for use in the soil prediction pipeline.

---

# 7. CNN Model Configuration

The CNN model was configured for the seven soil classes.

The final classification layer was adapted to the number of soil categories.

The model uses ResNet-50's extracted image features to identify patterns associated with different soil types.

The fully connected layer used for classification was configured with the extracted feature representation.

The model was also tested using CPU-based execution during the development process.

---

# 8. Soil Image Prediction

After training, the CNN model was used to predict soil types from input images.

For each input image, the system produces:

* Predicted soil type
* Prediction confidence

For example:

```text
Input:
Soil Image

Output:
Predicted Soil Type → Arid
Confidence → 29.84%
```

The prediction output was later connected to the M3 Farmer PWA.

---

# 9. Structured Soil Analysis

In addition to image classification, structured soil information was analyzed using Machine Learning.

The system works with the following parameters:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* pH
* Moisture
* Organic Matter

Additional environmental variables were also considered in the structured analysis.

---

# 10. Machine Learning Model

A **Gradient Boosting / XGBoost-based Machine Learning approach** was used for structured data analysis.

The purpose of this model was to identify relationships between soil/environmental parameters and the target analysis.

The structured ML pipeline included:

```text
Structured Soil Data
        ↓
Data Preprocessing
        ↓
Feature Selection
        ↓
ML Model
        ↓
Prediction
        ↓
Feature Importance
```

---

# 11. Feature Importance Analysis

Feature importance analysis was performed to understand the relative contribution of the input features to the Machine Learning model.

The analyzed feature importance values were:

| Feature        | Importance |
| -------------- | ---------: |
| Potassium (K)  |   0.280171 |
| Humidity       |   0.248110 |
| Rainfall       |   0.165616 |
| Temperature    |   0.135268 |
| Phosphorus (P) |   0.103551 |
| pH             |   0.052944 |
| Soil Moisture  |   0.007235 |
| Organic Matter |   0.007106 |

These values wer

