import os
import cv2
import pandas as pd


# =========================================================
# DATASET PATH
# =========================================================

dataset_path = "Original_Dataset/Orignal-Dataset"


# =========================================================
# SHARPNESS ANALYSIS
# =========================================================

print("==============================")
print("IMAGE SHARPNESS / BLUR ANALYSIS")
print("==============================")


results = []


for soil_class in os.listdir(dataset_path):

    class_path = os.path.join(dataset_path, soil_class)

    if os.path.isdir(class_path):

        print(f"\nChecking: {soil_class}")

        for file in os.listdir(class_path):

            if file.lower().endswith(
                (".jpg", ".jpeg", ".png", ".webp")
            ):

                image_path = os.path.join(
                    class_path,
                    file
                )

                image = cv2.imread(image_path)

                if image is None:
                    continue

                gray = cv2.cvtColor(
                    image,
                    cv2.COLOR_BGR2GRAY
                )

                # Variance of Laplacian
                sharpness = cv2.Laplacian(
                    gray,
                    cv2.CV_64F
                ).var()

                results.append({
                    "soil_class": soil_class,
                    "filename": file,
                    "sharpness_score": sharpness
                })


# =========================================================
# RESULTS
# =========================================================

df = pd.DataFrame(results)

print("\n==============================")
print("SHARPNESS RESULTS")
print("==============================")

print("Total images analyzed:", len(df))

print("\nSharpness statistics:")
print(df["sharpness_score"].describe())

print("\n10 blurriest images:")
print(df.nsmallest(10, "sharpness_score")[
    ["soil_class", "filename", "sharpness_score"]
])

print("\n10 sharpest images:")
print(df.nlargest(10, "sharpness_score")[
    ["soil_class", "filename", "sharpness_score"]
])


# =========================================================
# SAVE RESULTS
# =========================================================

df.to_csv(
    "sharpness_results.csv",
    index=False
)

print("\nSharpness results saved to:")
print("sharpness_results.csv")

print("==============================")