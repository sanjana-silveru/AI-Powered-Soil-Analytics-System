import os
import hashlib

# Dataset path
dataset_path = "Original_Dataset/Orignal-Dataset"

# Store image hashes
image_hashes = {}

total_images = 0
duplicate_images = 0

print("==============================")
print("DUPLICATE IMAGE CHECK")
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
                    # Calculate file hash
                    with open(image_path, "rb") as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()

                    if file_hash in image_hashes:

                        duplicate_images += 1

                        print("\nDuplicate found:")
                        print("Original:", image_hashes[file_hash])
                        print("Duplicate:", image_path)

                    else:
                        image_hashes[file_hash] = image_path

                except Exception as e:

                    print("Could not read:", image_path)
                    print("Error:", e)


print("\n==============================")
print("RESULTS")
print("==============================")

print("Total images checked:", total_images)
print("Unique images:", len(image_hashes))
print("Duplicate images:", duplicate_images)

print("==============================")
print("DUPLICATE IMAGE CHECK COMPLETED")
print("==============================")