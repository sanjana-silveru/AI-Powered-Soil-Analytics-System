# 🌱 AI-Powered Soil Analytics System for Nutrient Assessment and Intelligent Crop Advisory

## 📌 Project Overview

The **AI-Powered Soil Analytics System for Nutrient Assessment and Intelligent Crop Advisory** is an AI/ML-based system developed to analyze soil conditions and provide intelligent agricultural recommendations.

The system combines **soil image classification, structured soil parameter analysis, Explainable AI, soil health assessment, crop suitability analysis, and a farmer-friendly Progressive Web Application (PWA).**

The system works with the following important soil parameters:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* pH
* Moisture
* Organic Matter

The project was developed through three major milestones.

---

# 🚀 Milestone 1 – Data Ingestion & Preparation

## Objective

Milestone 1 focused on **collecting, organizing, cleaning, validating, and preparing the soil dataset** required for the AI/ML models.

## 1. Dataset Collection

The soil image dataset contains seven major soil classes:

* Alluvial
* Arid
* Black
* Laterite
* Mountain
* Red
* Yellow

The dataset was organized according to soil type so that it could be used for CNN-based image classification.

## 2. Dataset Analysis

Before cleaning, the dataset contained approximately **1189 images**.

The initial distribution was:

| Soil Type |   Images |
| --------- | -------: |
| Alluvial  |       52 |
| Arid      |      284 |
| Black     |      255 |
| Laterite  |      219 |
| Mountain  |      201 |
| Red       |      109 |
| Yellow    |       69 |
| **Total** | **1189** |

## 3. Duplicate Removal and Label Verification

Duplicate images were identified and removed, and soil labels were verified.

After duplicate removal and label verification, approximately **1140 images** remained.

The cleaned dataset was then further normalized and prepared for model development.

## 4. Image Preprocessing

The dataset preparation process included:

* Image organization
* Duplicate removal
* Label verification
* Image resizing
* Normalization
* Dataset structure preparation

The prepared dataset was used as the foundation for the CNN model developed in Milestone 2.

## 5. Dataset Visualization

A soil class distribution graph was generated to understand the distribution of images among the different soil categories.

### M1 Outcome

Milestone 1 resulted in a **cleaned and organized dataset** ready for Machine Learning and Deep Learning tasks.

---

# 🤖 Milestone 2 – AI/ML Soil Analysis Engine

## Objective

Milestone 2 focused on developing the **AI/ML engine** for soil image classification and structured soil analysis.

The milestone combined:

1. CNN-based soil image classification
2. Structured Machine Learning
3. Explainable AI

---

## 1. CNN-Based Soil Classification

A **ResNet-50 Convolutional Neural Network (CNN)** was trained for soil image classification.

The model classifies soil images into the seven soil categories:

* Alluvial
* Arid
* Black
* Laterite
* Mountain
* Red
* Yellow

The trained model files include:

```text
CNN_Model/
├── best_resnet50_soil_model.pth
└── resnet50_soil_model.pth
```

The model uses the soil image as input and produces a predicted soil type with a confidence value.

---

## 2. Structured Soil Analysis

In addition to image analysis, structured soil parameters were analyzed using Machine Learning.

The parameters considered include:

* Nitrogen
* Phosphorus
* Potassium
* pH
* Moisture
* Organic Matter

A **Gradient Boosting / XGBoost-based approach** was used for structured soil analysis.

This allows the system to analyze numerical soil information and identify the importance of different features.

---

## 3. Feature Importance Analysis

Feature importance analysis was performed to understand which parameters contributed most to the structured model.

The analyzed feature importance values included:

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

This analysis provides an understanding of how different parameters influence the model.

---

## 4. Explainable AI

Explainable AI techniques were incorporated to make CNN predictions easier to understand.

**Grad-CAM (Gradient-weighted Class Activation Mapping)** was used to visualize important regions of a soil image that contributed to the CNN prediction.

For example, Grad-CAM was tested on an Alluvial soil image where the model produced an **Arid prediction with approximately 29.84% confidence**.

The visualization helps identify which parts of the image influenced the model's prediction.

---

## 5. M2 Outcome

Milestone 2 produced a structured AI/ML soil analysis engine consisting of:

* CNN soil classification
* Structured soil analysis
* Feature importance analysis
* Explainable AI using Grad-CAM
* Trained ResNet-50 model

These components were later integrated into the Farmer PWA during Milestone 3.

---

# 🌾 Milestone 3 – Recommendation Engine & Farmer PWA

## Objective

Milestone 3 focused on converting the AI/ML analysis results into **actionable agricultural recommendations** and developing a farmer-friendly web application.

The main components were:

* Knowledge Base
* Recommendation Engine
* Crop Suitability
* Soil Health Analysis
* Farmer PWA
* CNN API integration

---

# 1. Knowledge Base

A knowledge base was created to store rules and information required for soil analysis and recommendations.

The system considers:

* Nitrogen
* Phosphorus
* Potassium
* pH
* Moisture
* Organic Matter

These values are compared against defined suitable ranges to determine the condition of each soil parameter.

---

# 2. Recommendation Engine

A rule-based recommendation engine was developed to identify soil conditions and generate recommendations.

For example, a test input containing:

```text
Nitrogen = 15
Phosphorus = 25
Potassium = 120
pH = 5.5
Moisture = 45
Organic Matter = 1.5
```

produced results identifying:

* Nitrogen → Low
* Phosphorus → Adequate
* Potassium → Adequate
* pH → Acidic
* Moisture → Suitable
* Organic Matter → Low

The system then generates recommendations based on the identified soil conditions.

---

# 3. Crop Suitability Analysis

A crop suitability module was developed to identify crops that can be suitable for the analyzed soil conditions.

The system can provide crops such as:

* Rice
* Wheat
* Maize
* Cotton
* Groundnut
* Chickpea
* Pigeonpea
* Sorghum
* Millet
* Sugarcane

A balanced soil test was also performed using:

```text
Nitrogen = 35
Phosphorus = 25
Potassium = 180
pH = 6.8
Moisture = 50
Organic Matter = 3
```

The test identified multiple suitable crops, including Rice, Wheat, Maize, Cotton, and Groundnut.

---

# 4. Soil Health Analysis

A soil health scoring system was developed to convert soil parameter conditions into an overall health score.

The application categorizes soil conditions as:

```text
Healthy
Moderately Healthy
Needs Improvement
Poor
```

Testing was performed using different soil conditions.

Example test results included:

* Soil health improvement test → **77.92**
* Alkaline soil test → **67.22**

These tests were used to verify that different soil conditions produce different health scores.

---

# 5. Farmer PWA – Soil Smart 🌱

A farmer-friendly Progressive Web Application named **Soil Smart 🌱** was developed using:

* Next.js
* React
* TypeScript
* Tailwind CSS

The application provides an easy interface for farmers to enter soil information and analyze soil conditions.

---

# 6. Soil Parameter Input

The application supports the following parameters:

```text
Nitrogen
Phosphorus
Potassium
pH
Moisture
Organic Matter
```

The entered values are analyzed to calculate:

* Soil health score
* Soil health status
* Parameter conditions
* Suitable crops
* Soil recommendations

---

# 7. Soil Image Upload

The PWA also supports soil image uploads.

Supported image formats:

* JPG
* PNG

The application validates uploaded images and limits the file size to **5 MB**.

Users can:

* Select a soil image
* Preview the image
* Remove the image
* Analyze the image

---

# 8. CNN Integration

The CNN model developed in Milestone 2 was integrated into the Milestone 3 application through a prediction API.

The workflow is:

```text
Soil Image
     ↓
Farmer PWA
     ↓
Prediction API
     ↓
ResNet-50 CNN Model
     ↓
Predicted Soil Type
     ↓
Confidence Score
     ↓
Displayed in Soil Smart
```

The application displays the predicted soil type and confidence along with the other soil analysis results.

---

# 9. Multilingual Support

The Farmer PWA supports three languages:

* 🇬🇧 English
* 🇮🇳 Hindi
* 🇮🇳 Kannada

Important application content such as soil conditions, recommendations, and history can be displayed using the selected language.

---

# 10. Analysis History

The application stores previous soil analyses using browser **Local Storage**.

This allows users to view previous analysis results without losing them when navigating through the application.

The history includes information such as:

* Soil values
* Health score
* Health status
* Analysis results

---

# 📁 Project Structure

```text
Soil_Project/
│
├── Knowledge_Base/
│
├── Recommendation_Engine/
│
├── Crop_Suitability/
│
├── Soil_Health/
│
├── Test_Data/
│
├── Results/
│
├── CNN_Model/
│   ├── best_resnet50_soil_model.pth
│   └── resnet50_soil_model.pth
│
├── Original_Dataset/
│
├── Cleaned_Dataset/
│
├── farmer-pwa/
│
└── README.md
```

---

# 🛠️ Technologies Used

### Machine Learning

* Python
* Gradient Boosting
* XGBoost

### Deep Learning

* ResNet-50
* Convolutional Neural Networks
* PyTorch

### Explainable AI

* Grad-CAM
* Feature Importance Analysis

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

# 🔄 Overall System Workflow

```text
                SOIL ANALYTICS SYSTEM
                         │
             ┌───────────┴───────────┐
             │                       │
       Soil Image              Soil Parameters
             │                       │
             ↓                       ↓
       ResNet-50 CNN          ML Analysis Engine
             │                       │
             ↓                       ↓
      Soil Classification     Parameter Analysis
             │                       │
             └───────────┬───────────┘
                         ↓
                  Soil Health Score
                         ↓
                 Crop Suitability
                         ↓
                  Recommendations
                         ↓
                Soil Smart PWA 🌱
```

---

# 📊 Project Results

The completed system is capable of:

* Preparing and cleaning soil datasets.
* Classifying soil images using ResNet-50.
* Providing CNN prediction confidence.
* Analyzing structured soil parameters.
* Identifying important soil features.
* Providing explainable CNN predictions using Grad-CAM.
* Calculating soil health scores.
* Identifying soil parameter conditions.
* Suggesting suitable crops.
* Generating soil improvement recommendations.
* Supporting English, Hindi, and Kannada.
* Maintaining previous analysis history.
* Providing a farmer-friendly interface.

---

# 🔮 Future Scope

The system can be further improved by adding:

* IoT-based soil sensor integration
* Real-time soil monitoring
* Weather data integration
* Larger and more diverse soil datasets
* Improved CNN training
* Mobile application deployment
* Cloud deployment
* Region-specific crop recommendations
* Advanced fertilizer recommendations
* Real-time agricultural advisory

---

# 👩‍💻 Author

**Sanjana Silveru**

B.Tech Student

GitHub: **sanjana-silveru**

