import os
import shutil
import random

SOURCE_DIR = "Resized_Dataset"
OUTPUT_DIR = "Split_Dataset"

TRAIN_RATIO = 0.70
VAL_RATIO = 0.15
TEST_RATIO = 0.15

random.seed(42)

classes = [
    "Alluvial_Soil",
    "Arid_Soil",
    "Black_Soil",
    "Laterite_Soil",
    "Mountain_Soil",
    "Red_Soil",
    "Yellow_Soil"
]

# Create output folders
for split in ["Train", "Validation", "Test"]:
    for class_name in classes:
        os.makedirs(
            os.path.join(OUTPUT_DIR, split, class_name),
            exist_ok=True
        )

total_train = 0
total_val = 0
total_test = 0

for class_name in classes:

    class_path = os.path.join(SOURCE_DIR, class_name)

    images = [
        file for file in os.listdir(class_path)
        if file.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    # Shuffle images randomly
    random.shuffle(images)

    total = len(images)

    train_count = int(total * TRAIN_RATIO)
    val_count = int(total * VAL_RATIO)

    train_images = images[:train_count]
    val_images = images[train_count:train_count + val_count]
    test_images = images[train_count + val_count:]

    # Copy training images
    for image in train_images:
        shutil.copy2(
            os.path.join(class_path, image),
            os.path.join(OUTPUT_DIR, "Train", class_name, image)
        )

    # Copy validation images
    for image in val_images:
        shutil.copy2(
            os.path.join(class_path, image),
            os.path.join(OUTPUT_DIR, "Validation", class_name, image)
        )

    # Copy testing images
    for image in test_images:
        shutil.copy2(
            os.path.join(class_path, image),
            os.path.join(OUTPUT_DIR, "Test", class_name, image)
        )

    total_train += len(train_images)
    total_val += len(val_images)
    total_test += len(test_images)

    print(
        class_name,
        "-> Train:", len(train_images),
        "Validation:", len(val_images),
        "Test:", len(test_images)
    )

print("\n==============================")
print("DATASET SPLIT COMPLETED")
print("==============================")
print("Training images:", total_train)
print("Validation images:", total_val)
print("Testing images:", total_test)
print("Total images:", total_train + total_val + total_test)
print("==============================")