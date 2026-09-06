import os
from PIL import Image

# Input dataset
source_dataset = "Cleaned_Dataset"

# Output dataset
resized_dataset = "Resized_Dataset"

# Target image size
image_size = (224, 224)

total_images = 0
resized_images = 0
failed_images = 0

print("==============================")
print("IMAGE RESIZING")
print("==============================")

for soil_class in os.listdir(source_dataset):

    source_class_path = os.path.join(
        source_dataset,
        soil_class
    )

    if not os.path.isdir(source_class_path):
        continue

    # Create class folder in resized dataset
    resized_class_path = os.path.join(
        resized_dataset,
        soil_class
    )

    os.makedirs(
        resized_class_path,
        exist_ok=True
    )

    print(f"\nProcessing: {soil_class}")

    for file in os.listdir(source_class_path):

        if file.lower().endswith(
            (".jpg", ".jpeg", ".png", ".webp")
        ):

            source_image = os.path.join(
                source_class_path,
                file
            )

            destination_image = os.path.join(
                resized_class_path,
                file
            )

            total_images += 1

            try:

                with Image.open(source_image) as img:

                    # Convert to RGB
                    img = img.convert("RGB")

                    # Resize to 224 × 224
                    resized_img = img.resize(
                        image_size
                    )

                    # Save as JPEG
                    resized_img.save(
                        destination_image,
                        "JPEG"
                    )

                    resized_images += 1

            except Exception as e:

                failed_images += 1

                print(
                    "Could not resize:",
                    source_image
                )

                print("Error:", e)


print("\n==============================")
print("RESIZING RESULTS")
print("==============================")

print("Total images:", total_images)
print("Successfully resized:", resized_images)
print("Failed images:", failed_images)

print("Image size: 224 x 224 pixels")

print("==============================")
print("IMAGE RESIZING COMPLETED")
print("==============================")