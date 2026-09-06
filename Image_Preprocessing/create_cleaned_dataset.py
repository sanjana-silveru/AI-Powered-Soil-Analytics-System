import os
import shutil
import hashlib

# Original dataset
source_dataset = "Original_Dataset/Orignal-Dataset"

# New cleaned dataset
cleaned_dataset = "Cleaned_Dataset"

# Store hashes that we have already seen
image_hashes = set()

total_images = 0
unique_images = 0
duplicate_images = 0

print("==============================")
print("CREATING CLEANED DATASET")
print("==============================")

for soil_class in os.listdir(source_dataset):

    source_class_path = os.path.join(source_dataset, soil_class)

    if not os.path.isdir(source_class_path):
        continue

    # Create corresponding class folder
    cleaned_class_path = os.path.join(
        cleaned_dataset,
        soil_class
    )

    os.makedirs(cleaned_class_path, exist_ok=True)

    print(f"\nProcessing: {soil_class}")

    for file in os.listdir(source_class_path):

        if file.lower().endswith(
            (".jpg", ".jpeg", ".png", ".webp")
        ):

            source_image = os.path.join(
                source_class_path,
                file
            )

            total_images += 1

            try:
                # Calculate image hash
                with open(source_image, "rb") as f:
                    image_hash = hashlib.md5(
                        f.read()
                    ).hexdigest()

                # Check duplicate
                if image_hash in image_hashes:

                    duplicate_images += 1
                    print("Duplicate skipped:", file)

                else:

                    image_hashes.add(image_hash)

                    destination_image = os.path.join(
                        cleaned_class_path,
                        file
                    )

                    shutil.copy2(
                        source_image,
                        destination_image
                    )

                    unique_images += 1

            except Exception as e:

                print("Could not process:", source_image)
                print("Error:", e)


print("\n==============================")
print("CLEANING RESULTS")
print("==============================")

print("Original images:", total_images)
print("Unique images copied:", unique_images)
print("Duplicate images skipped:", duplicate_images)

print("==============================")
print("CLEANED DATASET CREATED")
print("==============================")