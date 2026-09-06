# ============================================================
# WEEK 2 - STRUCTURED SOIL DATA ANALYSIS & PREPROCESSING
# Project: AI-Powered Soil Analytics System for Nutrient
#          Assessment and Intelligent Crop Advisory
#
# Dataset: Crop_recommendationV2.csv
# ============================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler


# ============================================================
# 1. PATH SETTINGS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FILE = os.path.join(
    BASE_DIR,
    "Structured_Data",
    "Original",
    "Crop_recommendationV2.csv"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "Structured_Data",
    "Cleaned"
)

GRAPH_DIR = os.path.join(
    BASE_DIR,
    "Structured_Data",
    "Graphs"
)

REPORT_DIR = os.path.join(
    BASE_DIR,
    "Structured_Data",
    "Reports"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)


# ============================================================
# 2. LOAD DATASET
# ============================================================

print("=" * 60)
print("STRUCTURED DATA ANALYSIS")
print("=" * 60)

print("\nLoading dataset...")

df = pd.read_csv(INPUT_FILE)

print("\nDataset loaded successfully.")

print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])


# ============================================================
# 3. CLEAN COLUMN NAMES
# ============================================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nColumn names:")
for column in df.columns:
    print("-", column)


# ============================================================
# 4. CHECK REQUIRED PARAMETERS
# ============================================================

required_columns = [
    "n",
    "p",
    "k",
    "ph",
    "soil_moisture",
    "organic_matter"
]

print("\n" + "=" * 60)
print("REQUIRED PARAMETER CHECK")
print("=" * 60)

missing_required = [
    column for column in required_columns
    if column not in df.columns
]

if missing_required:
    print("\nMissing required columns:")
    for column in missing_required:
        print("-", column)
else:
    print("\nAll six required soil parameters are present.")

print("\nRequired parameters:")
print("N               :", "n" in df.columns)
print("P               :", "p" in df.columns)
print("K               :", "k" in df.columns)
print("pH              :", "ph" in df.columns)
print("Soil Moisture   :", "soil_moisture" in df.columns)
print("Organic Matter  :", "organic_matter" in df.columns)


# ============================================================
# 5. DATA TYPES
# ============================================================

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)

dtype_report = pd.DataFrame({
    "Column": df.columns,
    "Data_Type": df.dtypes.astype(str).values
})

dtype_report.to_csv(
    os.path.join(REPORT_DIR, "data_types_report.csv"),
    index=False
)


# ============================================================
# 6. MISSING VALUE CHECK
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUE CHECK")
print("=" * 60)

missing_values = df.isnull().sum()

print(missing_values)

missing_report = pd.DataFrame({
    "Column": missing_values.index,
    "Missing_Values": missing_values.values
})

missing_report.to_csv(
    os.path.join(REPORT_DIR, "missing_values_report.csv"),
    index=False
)

if missing_values.sum() == 0:
    print("\nNo missing values found.")
else:
    print("\nMissing values detected.")


# ============================================================
# 7. DUPLICATE CHECK
# ============================================================

print("\n" + "=" * 60)
print("DUPLICATE CHECK")
print("=" * 60)

duplicate_count = df.duplicated().sum()

print("Duplicate rows:", duplicate_count)

if duplicate_count > 0:
    df = df.drop_duplicates().reset_index(drop=True)
    print("Duplicate rows removed.")
else:
    print("No duplicate rows found.")


# ============================================================
# 8. CONVERT NUMERIC COLUMNS
# ============================================================

numeric_columns = [
    "n",
    "p",
    "k",
    "ph",
    "soil_moisture",
    "organic_matter"
]

# Convert available required columns to numeric
for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# ============================================================
# 9. INVALID VALUE CHECK
# ============================================================

print("\n" + "=" * 60)
print("INVALID VALUE CHECK")
print("=" * 60)

invalid_report = []

# General invalid check: negative values
for column in numeric_columns:

    if column in df.columns:

        negative_count = (df[column] < 0).sum()

        invalid_report.append({
            "Column": column,
            "Negative_Values": negative_count
        })

        print(
            f"{column}: {negative_count} negative values"
        )


# pH validity
if "ph" in df.columns:

    invalid_ph = (
        (df["ph"] < 0) |
        (df["ph"] > 14)
    ).sum()

    print("Invalid pH values:", invalid_ph)

else:
    invalid_ph = 0


# Moisture validity
if "soil_moisture" in df.columns:

    invalid_moisture = (
        (df["soil_moisture"] < 0) |
        (df["soil_moisture"] > 100)
    ).sum()

    print("Invalid moisture values:", invalid_moisture)

else:
    invalid_moisture = 0


invalid_report_df = pd.DataFrame(invalid_report)

invalid_report_df.to_csv(
    os.path.join(REPORT_DIR, "invalid_values_report.csv"),
    index=False
)


# ============================================================
# 10. CHECK NEW MISSING VALUES AFTER CONVERSION
# ============================================================

new_missing = df.isnull().sum()

print("\nMissing values after numeric conversion:")

print(new_missing)

# Remove rows with missing required soil parameters
df = df.dropna(
    subset=[
        column for column in required_columns
        if column in df.columns
    ]
).reset_index(drop=True)


# ============================================================
# 11. RANGE / BASIC STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("BASIC STATISTICS")
print("=" * 60)

available_numeric = [
    column for column in numeric_columns
    if column in df.columns
]

statistics = df[available_numeric].describe().T

print(statistics)

statistics.to_csv(
    os.path.join(REPORT_DIR, "basic_statistics.csv")
)


# ============================================================
# 12. OUTLIER DETECTION USING IQR
# ============================================================

print("\n" + "=" * 60)
print("OUTLIER DETECTION")
print("=" * 60)

outlier_results = []

for column in available_numeric:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    outlier_count = len(outliers)

    print(
        f"{column}: {outlier_count} outliers"
    )

    outlier_results.append({
        "Column": column,
        "Q1": Q1,
        "Q3": Q3,
        "IQR": IQR,
        "Lower_Bound": lower_bound,
        "Upper_Bound": upper_bound,
        "Outlier_Count": outlier_count
    })


outlier_df = pd.DataFrame(outlier_results)

outlier_df.to_csv(
    os.path.join(REPORT_DIR, "outlier_report.csv"),
    index=False
)


# ============================================================
# IMPORTANT:
# DO NOT AUTOMATICALLY DELETE OUTLIERS
# ============================================================

print("\nOutliers have been identified but NOT deleted.")

print(
    "Reason: extreme soil values may be genuine observations."
)


# ============================================================
# 13. CATEGORICAL COLUMN ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("CATEGORICAL DATA ANALYSIS")
print("=" * 60)

categorical_columns = df.select_dtypes(
    include=["object", "category"]
).columns.tolist()

print("\nCategorical columns:")

for column in categorical_columns:

    print("\n", column)

    value_counts = df[column].value_counts()

    print(value_counts)

    value_counts.to_csv(
        os.path.join(
            REPORT_DIR,
            f"{column}_distribution.csv"
        )
    )


# ============================================================
# 14. CROP LABEL DISTRIBUTION
# ============================================================

if "label" in df.columns:

    print("\n" + "=" * 60)
    print("CROP LABEL DISTRIBUTION")
    print("=" * 60)

    label_counts = df["label"].value_counts()

    print(label_counts)

    plt.figure(figsize=(12, 6))

    label_counts.plot(kind="bar")

    plt.title("Crop Label Distribution")

    plt.xlabel("Crop")

    plt.ylabel("Number of Samples")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            GRAPH_DIR,
            "crop_label_distribution.png"
        )
    )

    plt.close()


# ============================================================
# 15. HISTOGRAMS OF REQUIRED SOIL PARAMETERS
# ============================================================

for column in available_numeric:

    plt.figure(figsize=(8, 5))

    plt.hist(
        df[column],
        bins=30
    )

    plt.title(
        f"Distribution of {column}"
    )

    plt.xlabel(column)

    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            GRAPH_DIR,
            f"{column}_distribution.png"
        )
    )

    plt.close()


# ============================================================
# 16. BOXPLOTS FOR OUTLIER VISUALIZATION
# ============================================================

for column in available_numeric:

    plt.figure(figsize=(8, 5))

    plt.boxplot(
        df[column].dropna()
    )

    plt.title(
        f"Boxplot of {column}"
    )

    plt.ylabel(column)

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            GRAPH_DIR,
            f"{column}_boxplot.png"
        )
    )

    plt.close()


# ============================================================
# 17. CORRELATION MATRIX
# ============================================================

print("\n" + "=" * 60)
print("CORRELATION ANALYSIS")
print("=" * 60)

correlation = df[available_numeric].corr()

print(correlation)

correlation.to_csv(
    os.path.join(
        REPORT_DIR,
        "correlation_matrix.csv"
    )
)


# Correlation graph
plt.figure(figsize=(8, 6))

plt.imshow(
    correlation,
    aspect="auto"
)

plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Soil Parameter Correlation Matrix")

plt.tight_layout()

plt.savefig(
    os.path.join(
        GRAPH_DIR,
        "correlation_matrix.png"
    )
)

plt.close()


# ============================================================
# 18. SAVE CLEANED DATASET
# ============================================================

cleaned_file = os.path.join(
    OUTPUT_DIR,
    "soil_data_cleaned.csv"
)

df.to_csv(
    cleaned_file,
    index=False
)

print("\n" + "=" * 60)

print("CLEANED DATASET SAVED")

print("=" * 60)

print(cleaned_file)


# ============================================================
# 19. FEATURE SCALING
# ============================================================

print("\n" + "=" * 60)
print("FEATURE SCALING")
print("=" * 60)

scaled_df = df.copy()

scaler = StandardScaler()

scaled_df[available_numeric] = scaler.fit_transform(
    scaled_df[available_numeric]
)

scaled_file = os.path.join(
    OUTPUT_DIR,
    "soil_data_scaled.csv"
)

scaled_df.to_csv(
    scaled_file,
    index=False
)

print("Scaled dataset saved:")
print(scaled_file)


# ============================================================
# 20. FINAL DATASET SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("FINAL DATASET SUMMARY")
print("=" * 60)

print("Final rows    :", df.shape[0])
print("Final columns :", df.shape[1])

print("\nRequired parameters:")

for column in required_columns:

    if column in df.columns:

        print(
            f"{column}: "
            f"MIN={df[column].min():.3f}, "
            f"MAX={df[column].max():.3f}, "
            f"MEAN={df[column].mean():.3f}"
        )


print("\nMissing values:")
print(df.isnull().sum().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nAnalysis completed successfully.")

print("=" * 60)