import os
from PIL import Image

# Dataset path
dataset_path = "Original_Dataset/Orignal-Dataset"

total_images = 0
corrupted_images = 0

print("==============================")
print("CORRUPTED IMAGE CHECK")
print("==============================")

for soil_class in os.listdir(dataset_path):

    class_path = os.path.join(dataset_path, soil_class)

    if os.path.isdir(class_path):

        print(f"\nChecking: {soil_class}")

        for file in os.listdir(class_path):

            if file.lower().endswith(
                (".jpg", ".jpeg", ".png", ".webp")
            ):

                image_path = os.path.join(class_path, file)

                total_images += 1

                try:
                    with Image.open(image_path) as img:
                        img.verify()

                except Exception:
                    corrupted_images += 1
                    print("Corrupted:", image_path)

print("\n==============================")
print("RESULTS")
print("==============================")

print("Total images checked:", total_images)
print("Corrupted images:", corrupted_images)
print("Valid images:", total_images - corrupted_images)

print("==============================")
print("CORRUPTED IMAGE CHECK COMPLETED")
print("==============================")