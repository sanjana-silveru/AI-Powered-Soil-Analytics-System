from PIL import Image, ImageEnhance
import random
import os

# Select one training image
image_path = "Split_Dataset/Train/Alluvial_Soil/16.jpg"

# Temporary output folder
output_folder = "augmentation_test"
os.makedirs(output_folder, exist_ok=True)

# Open image
image = Image.open(image_path).convert("RGB")

# 1. Rotation
rotated = image.rotate(20)
rotated.save(os.path.join(output_folder, "rotated.jpg"))

# 2. Horizontal flip
flipped = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
flipped.save(os.path.join(output_folder, "flipped.jpg"))

# 3. Brightness adjustment
brightness = ImageEnhance.Brightness(image)
bright_image = brightness.enhance(1.3)
bright_image.save(os.path.join(output_folder, "brightness.jpg"))

# 4. Slight zoom/crop
width, height = image.size
crop_amount = 20

cropped = image.crop(
    (
        crop_amount,
        crop_amount,
        width - crop_amount,
        height - crop_amount
    )
)

zoomed = cropped.resize((224, 224))
zoomed.save(os.path.join(output_folder, "zoomed.jpg"))

print("==============================")
print("AUGMENTATION VERIFICATION")
print("==============================")
print("Original image:", image_path)
print("Augmented images created: 4")
print("Output folder:", output_folder)
print("==============================")
print("Augmentation verification completed!")