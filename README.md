# 📌 Milestone 1 – Data Ingestion & Preparation

## 1. Overview

Milestone 1 focused on the **collection, organization, inspection, cleaning, validation, and preparation of the soil image dataset** required for the AI-powered soil analytics system.

The main purpose of this milestone was to create a reliable and properly structured dataset that could be used in the later stages of the project, particularly for **CNN-based soil image classification**.

The dataset contains images representing different soil types. The data preparation process was performed before developing the AI/ML models in Milestone 2.

---

## 2. Objectives

The main objectives of Milestone 1 were:

* To collect and organize the available soil image dataset.
* To identify the different soil categories.
* To inspect the dataset for duplicate images.
* To verify the labels associated with the images.
* To clean and prepare the dataset.
* To analyze the distribution of images across soil classes.
* To prepare the images for further Machine Learning and Deep Learning tasks.
* To establish the required project environment and folder structure.

---

## 3. Dataset Description

The soil image dataset consists of **seven soil classes**:

1. Alluvial
2. Arid
3. Black
4. Laterite
5. Mountain
6. Red
7. Yellow

Each class contains soil images belonging to that particular soil category.

The dataset was organized into separate folders based on soil type to make it suitable for image classification.

---

## 4. Initial Dataset Analysis

Before the cleaning process, the dataset contained a total of **1189 images**.

The initial class distribution was:

| Soil Class | Number of Images |
| ---------- | ---------------: |
| Alluvial   |               52 |
| Arid       |              284 |
| Black      |              255 |
| Laterite   |              219 |
| Mountain   |              201 |
| Red        |              109 |
| Yellow     |               69 |
| **Total**  |         **1189** |

This initial analysis helped identify the number of images available for each soil category.

### 📊 Soil Class Distribution

![Soil Class Distribution](graphs/soil_class_distribution.png)

*Figure 1: Distribution of soil images across the seven soil classes.*

---

## 5. Dataset Cleaning

The collected dataset was examined to identify problems that could affect model training.

The cleaning process included:

### 5.1 Duplicate Image Removal

Duplicate images were identified and removed from the dataset.

Removing duplicate images is important because repeated copies of the same image can introduce bias into the dataset and may affect the reliability of model training and evaluation.

After duplicate removal and label verification, the dataset contained approximately **1140 images**.

---

### 5.2 Label Verification

The labels of the images were checked to ensure that images were placed under the correct soil category.

The seven labels were verified as:

* Alluvial
* Arid
* Black
* Laterite
* Mountain
* Red
* Yellow

This step helped ensure that the model would receive the correct soil class during training.

---

## 6. Dataset Normalization and Preparation

After cleaning, the images were further prepared for use in the Deep Learning pipeline.

The preparation process included:

* Organizing images according to their soil classes.
* Removing duplicate images.
* Checking image labels.
* Resizing images to a consistent format.
* Normalizing image data.
* Preparing the cleaned dataset for CNN model development.

The cleaned dataset was retained as the main prepared dataset for subsequent milestones.

---

## 7. Dataset Folder Organization

The project dataset was organized into structured folders so that each soil category could be easily identified and processed.

The main dataset structure was organized around the soil classes:

```text
Cleaned_Dataset/
│
├── Alluvial/
├── Arid/
├── Black/
├── Laterite/
├── Mountain/
├── Red/
└── Yellow/
```

This organization makes it easier for an image classification model to associate each image with its corresponding soil class.

---

## 8. Dataset Statistics After Cleaning

The cleaning process reduced the number of images by removing duplicates and performing label verification.

### Dataset Progress

```text
Initial Dataset
      ↓
1189 Images
      ↓
Duplicate Removal
      ↓
Label Verification
      ↓
Approximately 1140 Images
      ↓
Image Preparation
      ↓
Cleaned Dataset
```

The prepared dataset was then used as the input for the AI/ML development performed in Milestone 2.

---

## 9. Dataset Size and Storage

The project maintained separate dataset resources during the preparation stage.

The approximate storage sizes were:

| Dataset Resource |    Size |
| ---------------- | ------: |
| Original Dataset |  518 MB |
| Resized Dataset  | 15.2 MB |

The cleaned dataset was retained for use in the later stages of the project.

---

## 10. Data Preprocessing

The image preprocessing stage prepared the dataset for CNN-based processing.

The main preprocessing operations were:

### Image Resizing

Images were resized into a consistent input format so that they could be processed by the CNN model.

### Normalization

Pixel values were normalized to provide a consistent numerical representation for model processing.

### Dataset Organization

Images were organized according to their corresponding soil classes.

These preprocessing steps help provide consistent input to the Deep Learning model.

---

## 11. Data Quality Verification

Data quality was checked before moving to the next milestone.

The verification process included:

* Checking soil class folders.
* Checking image counts.
* Removing duplicate images.
* Verifying labels.
* Checking the prepared dataset.
* Generating class distribution information.
* Confirming that the dataset was ready for model development.

---

## 12. M1 Analysis

The dataset analysis showed that the number of images was not equal across all soil classes.

For example, **Arid** and **Black** contained more images than some of the other classes, while **Alluvial** and **Yellow** contained fewer images.

This distribution was documented because differences in class size are relevant when preparing an image classification dataset.

The dataset cleaning and organization performed in M1 provided a structured foundation for the CNN model developed in M2.

---

## 13. M1 Deliverables

The completed Milestone 1 work includes:

* Dataset collection
* Dataset inventory
* Soil class identification
* Dataset organization
* Duplicate image removal
* Label verification
* Image preprocessing
* Dataset normalization
* Dataset statistics
* Soil class distribution analysis
* Cleaned dataset preparation
* Project environment setup
* Documentation of the data preparation process

---

## 14. M1 Outcome

At the end of Milestone 1, the soil image dataset was **organized, cleaned, verified, and prepared for AI/ML model development**.

The prepared dataset became the foundation for **Milestone 2 – AI/ML Soil Analysis Engine**, where the ResNet-50 CNN model and other Machine Learning components were developed.

### 🔗 Milestone Connection

```text
MILESTONE 1
Data Ingestion & Preparation
          ↓
Cleaned & Prepared Dataset
          ↓
MILESTONE 2
AI/ML Soil Analysis Engine
          ↓
Soil Classification & Analysis
```

---

## 📷 M1 Project Evidence

### Dataset Distribution

![M1 Soil Class Distribution](graphs/soil_class_distribution.png)

*Figure 1: Soil class distribution generated during dataset analysis.*

### Dataset Organization

> Add your screenshot of the dataset folders here.

```markdown
![M1 Dataset Organization](path/to/your/dataset-screenshot.png)
```

### Data Cleaning / Preprocessing

> Add your screenshot showing the cleaning, preprocessing, or dataset analysis here.

```markdown
![M1 Data Preprocessing](path/to/your/preprocessing-screenshot.png)
```

---

## ✅ Milestone 1 Summary

**Milestone 1 successfully established the data foundation for the Soil Analytics System by collecting, analyzing, cleaning, verifying, organizing, and preprocessing the soil image dataset.**
