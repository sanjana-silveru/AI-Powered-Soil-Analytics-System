import os
from PIL import Image, ImageStat


# =========================================================
# DATASET PATH
# =========================================================

dataset_path = "Original_Dataset/Orignal-Dataset"


# =========================================================
# IMAGE BRIGHTNESS CHECK
# =========================================================

print("==============================")
print("IMAGE BRIGHTNESS ANALYSIS")
print("==============================")


total_images = 0
dark_images = 0
normal_images = 0
bright_images = 0

brightness_values = []


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

                try:

                    with Image.open(image_path) as img:

                        # Convert image to grayscale
                        gray_img = img.convert("L")

                        # Calculate average brightness
                        stat = ImageStat.Stat(gray_img)
                        brightness = stat.mean[0]

                        brightness_values.append(brightness)
                        total_images += 1

                        # Classify brightness
                        if brightness < 60:
                            dark_images += 1

                        elif brightness > 200:
                            bright_images += 1

                        else:
                            normal_images += 1

                except Exception:

                    print("Could not read:", image_path)


# =========================================================
# RESULTS
# =========================================================

print("\n==============================")
print("BRIGHTNESS RESULTS")
print("==============================")


print("Total images:", total_images)
print("Dark images:", dark_images)
print("Normal brightness images:", normal_images)
print("Bright images:", bright_images)


if total_images > 0:

    dark_percentage = (
        dark_images / total_images
    ) * 100

    normal_percentage = (
        normal_images / total_images
    ) * 100

    bright_percentage = (
        bright_images / total_images
    ) * 100

    average_brightness = (
        sum(brightness_values)
        / len(brightness_values)
    )

    print(
        f"Dark images: {dark_percentage:.2f}%"
    )

    print(
        f"Normal brightness: {normal_percentage:.2f}%"
    )

    print(
        f"Bright images: {bright_percentage:.2f}%"
    )

    print(
        f"Average brightness: {average_brightness:.2f}"
    )


print("==============================")
print("BRIGHTNESS ANALYSIS COMPLETED")
print("==============================")