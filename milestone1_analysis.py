import os
from collections import Counter
from PIL import Image
import matplotlib.pyplot as plt


# =========================================================
# 1. DATASET PATH
# =========================================================

dataset_path = "Original_Dataset/Orignal-Dataset"
os.makedirs("graphs", exist_ok=True)


# =========================================================
# 2. SOIL DATASET CHECK
# =========================================================

print("==============================")
print("SOIL DATASET CHECK")
print("==============================")

total_images = 0
class_counts = {}


# Count images in each soil class
for soil_class in os.listdir(dataset_path):

    class_path = os.path.join(dataset_path, soil_class)

    if os.path.isdir(class_path):

        image_count = 0

        for file in os.listdir(class_path):

            if file.lower().endswith(
                (".jpg", ".jpeg", ".png", ".webp")
            ):
                image_count += 1

        class_counts[soil_class] = image_count
        total_images += image_count


# =========================================================
# 3. DISPLAY IMAGE COUNT AND PERCENTAGE
# =========================================================

for soil_class, count in class_counts.items():

    percentage = (count / total_images) * 100

    print(
        f"{soil_class}: {count} images ({percentage:.2f}%)"
    )


print("==============================")
print("Total images:", total_images)
print("==============================")


# =========================================================
# 4. SOIL CLASS DISTRIBUTION GRAPH
# =========================================================

soil_classes = list(class_counts.keys())
image_counts = list(class_counts.values())


plt.figure(figsize=(10, 6))

plt.bar(soil_classes, image_counts)

plt.xlabel("Soil Class")
plt.ylabel("Number of Images")
plt.title("Distribution of Soil Classes")

plt.xticks(rotation=45)

plt.tight_layout()


# Save graph
plt.savefig(
    "graphs/soil_class_distribution.png",
    dpi=300
)

plt.show()

print("Soil class distribution graph saved successfully!")


# =========================================================
# 5. IMAGE DIMENSION REPORT
# =========================================================

print("\n==============================")
print("IMAGE DIMENSION REPORT")
print("==============================")


dimensions = []


for soil_class in os.listdir(dataset_path):

    class_path = os.path.join(dataset_path, soil_class)

    if os.path.isdir(class_path):

        for file in os.listdir(class_path):

            if file.lower().endswith(
                (".jpg", ".jpeg", ".png", ".webp")
            ):

                image_path = os.path.join(
                    class_path,
                    file
                )

                try:

                    with Image.open(image_path) as img:

                        dimensions.append(img.size)

                except Exception:

                    print(
                        "Could not read:",
                        image_path
                    )


# Count repeated dimensions
dimension_counts = Counter(dimensions)


print(
    "Total images checked:",
    len(dimensions)
)


print("\nMost common dimensions:")


for dimension, count in dimension_counts.most_common(20):

    print(
        f"{dimension[0]} x {dimension[1]} -> {count} images"
    )


print("==============================")
print("IMAGE ANALYSIS COMPLETED")
print("==============================")
import cv2
import pandas as pd

IMAGE_FOLDER = "Original_Dataset/Orignal-Dataset"

results = []

for root, dirs, files in os.walk(IMAGE_FOLDER):

    for file in files:

        if file.lower().endswith(
            (".jpg", ".jpeg", ".png", ".bmp", ".webp")
        ):

            image_path = os.path.join(root, file)

            image = cv2.imread(image_path)

            if image is None:
                continue

            gray = cv2.cvtColor(
                image,
                cv2.COLOR_BGR2GRAY
            )

            # Calculate sharpness using Laplacian variance
            sharpness = cv2.Laplacian(
                gray,
                cv2.CV_64F
            ).var()

            results.append({
                "filename": file,
                "path": image_path,
                "sharpness_score": sharpness
            })


df = pd.DataFrame(results)

# Sort from blurriest to sharpest
df = df.sort_values(
    "sharpness_score"
)

# Save results
df.to_csv(
    "sharpness_results.csv",
    index=False
)

print("\n==============================")
print("IMAGE SHARPNESS ANALYSIS")
print("==============================")

print(
    "Total images analyzed:",
    len(df)
)

print("\nSharpness statistics:")
print(
    df["sharpness_score"].describe()
)

print("\n10 blurriest images:")
print(
    df.head(10)
)

print("\n10 sharpest images:")
print(
    df.tail(10)
)