from PIL import Image
import numpy as np
import os

dataset_path = "Resized_Dataset"

total_images = 0
normalized_images = 0
failed_images = 0

minimum_pixel = 1.0
maximum_pixel = 0.0

for class_name in os.listdir(dataset_path):

    class_path = os.path.join(dataset_path, class_name)

    if not os.path.isdir(class_path):
        continue

    for filename in os.listdir(class_path):

        if filename.lower().endswith((".jpg", ".jpeg", ".png")):

            total_images += 1

            image_path = os.path.join(class_path, filename)

            try:
                image = Image.open(image_path).convert("RGB")

                # Convert image to NumPy array
                image_array = np.array(image).astype(np.float32)

                # Normalize pixel values from 0-255 to 0-1
                normalized_array = image_array / 255.0

                # Check normalized range
                minimum_pixel = min(
                    minimum_pixel,
                    normalized_array.min()
                )

                maximum_pixel = max(
                    maximum_pixel,
                    normalized_array.max()
                )

                if (
                    normalized_array.min() >= 0.0
                    and normalized_array.max() <= 1.0
                ):
                    normalized_images += 1

            except Exception as e:
                failed_images += 1
                print("Failed:", image_path)
                print("Error:", e)

print("\n--- Normalization Results ---")
print("Total images:", total_images)
print("Successfully normalized:", normalized_images)
print("Failed images:", failed_images)
print("Minimum pixel value:", minimum_pixel)
print("Maximum pixel value:", maximum_pixel)