import os
from PIL import Image


# =========================================================
# DATASET PATH
# =========================================================

dataset_path = "Original_Dataset/Orignal-Dataset"


# =========================================================
# IMAGE QUALITY CHECK
# =========================================================

print("==============================")
print("IMAGE QUALITY CHECK")
print("==============================")


total_images = 0
valid_images = 0
corrupted_images = 0


for soil_class in os.listdir(dataset_path):

    class_path = os.path.join(dataset_path, soil_class)

    if os.path.isdir(class_path):

        print(f"\nChecking: {soil_class}")

        for file in os.listdir(class_path):

            if file.lower().endswith(
                (".jpg", ".jpeg", ".png", ".webp")
            ):

                total_images += 1

                image_path = os.path.join(
                    class_path,
                    file
                )

                try:

                    with Image.open(image_path) as img:

                        # Verify that the image can be read
                        img.verify()

                    valid_images += 1

                except Exception:

                    corrupted_images += 1

                    print("Corrupted/Unreadable:", image_path)


# =========================================================
# RESULTS
# =========================================================

print("\n==============================")
print("IMAGE QUALITY RESULTS")
print("==============================")

print("Total images:", total_images)
print("Valid images:", valid_images)
print("Corrupted images:", corrupted_images)

if total_images > 0:

    valid_percentage = (
        valid_images / total_images
    ) * 100

    corrupted_percentage = (
        corrupted_images / total_images
    ) * 100

    print(
        f"Valid images: {valid_percentage:.2f}%"
    )

    print(
        f"Corrupted images: {corrupted_percentage:.2f}%"
    )

print("==============================")