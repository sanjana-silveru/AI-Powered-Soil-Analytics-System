import os

dataset_path = "Cleaned_Dataset"

expected_classes = [
    "Alluvial_Soil",
    "Arid_Soil",
    "Black_Soil",
    "Laterite_Soil",
    "Mountain_Soil",
    "Red_Soil",
    "Yellow_Soil"
]

image_extensions = (".jpg", ".jpeg", ".png", ".webp")

print("==============================")
print("LABEL VERIFICATION")
print("==============================")

# Get folders
actual_classes = [
    folder for folder in os.listdir(dataset_path)
    if os.path.isdir(os.path.join(dataset_path, folder))
]

print("\nExpected classes:")
for cls in expected_classes:
    print("-", cls)

print("\nActual classes:")
for cls in actual_classes:
    print("-", cls)

# Check missing classes
missing_classes = set(expected_classes) - set(actual_classes)

# Check unexpected classes
unexpected_classes = set(actual_classes) - set(expected_classes)

print("\n==============================")
print("CLASS CHECK")
print("==============================")

if missing_classes:
    print("Missing classes:", missing_classes)
else:
    print("Missing classes: None")

if unexpected_classes:
    print("Unexpected classes:", unexpected_classes)
else:
    print("Unexpected classes: None")


# Count images
total_images = 0

print("\n==============================")
print("IMAGE COUNT BY CLASS")
print("==============================")

for soil_class in expected_classes:

    class_path = os.path.join(dataset_path, soil_class)

    if not os.path.exists(class_path):
        print(f"{soil_class}: FOLDER NOT FOUND")
        continue

    images = [
        file for file in os.listdir(class_path)
        if file.lower().endswith(image_extensions)
    ]

    count = len(images)
    total_images += count

    print(f"{soil_class}: {count}")


print("\n==============================")
print("LABEL VERIFICATION RESULTS")
print("==============================")

print("Total images:", total_images)
print("Total classes:", len(actual_classes))

if not missing_classes and not unexpected_classes:
    print("Label structure: CORRECT")
else:
    print("Label structure: NEEDS REVIEW")

print("==============================")
print("LABEL VERIFICATION COMPLETED")
print("==============================")