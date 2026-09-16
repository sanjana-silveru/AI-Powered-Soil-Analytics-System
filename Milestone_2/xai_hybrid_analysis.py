import os
import shutil


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = r"C:\Users\SILVERU SANJANA\OneDrive\Desktop\Soil_Project"

GRADCAM_DIR = os.path.join(
    BASE_DIR,
    "XAI",
    "GradCAM"
)

SHAP_DIR = os.path.join(
    BASE_DIR,
    "Structured_Data",
    "ML_Results",
    "SHAP"
)

XAI_OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "XAI",
    "Hybrid_Explanation"
)


# ============================================================
# CREATE OUTPUT DIRECTORY
# ============================================================

os.makedirs(XAI_OUTPUT_DIR, exist_ok=True)


print("\n============================================================")
print("          XAI HYBRID SOIL ANALYSIS")
print("============================================================")


# ============================================================
# GET SOIL IMAGE
# ============================================================

image_path = input(
    "\nEnter the complete path of the soil image used "
    "for hybrid analysis: "
).strip().strip('"')


if not os.path.exists(image_path):

    print("\nERROR: Image not found!")
    print("Please check the image path.")
    exit()


image_name = os.path.basename(image_path)

image_name_without_ext = os.path.splitext(
    image_name
)[0]


print("\nSearching for Grad-CAM explanation...")


# ============================================================
# SEARCH GRAD-CAM FOLDERS
# ============================================================

gradcam_matches = []

for root, dirs, files in os.walk(GRADCAM_DIR):

    for file in files:

        if image_name_without_ext.lower() in file.lower():

            gradcam_matches.append(
                os.path.join(root, file)
            )


# ============================================================
# DISPLAY GRAD-CAM RESULTS
# ============================================================

if len(gradcam_matches) == 0:

    print("\nNo matching Grad-CAM file found.")

else:

    print("\nGrad-CAM explanation found!")

    for path in gradcam_matches:

        print("\n", path)

        destination = os.path.join(
            XAI_OUTPUT_DIR,
            os.path.basename(path)
        )

        try:

            shutil.copy2(
                path,
                destination
            )

            print(
                "Copied to Hybrid_Explanation:"
            )

            print(destination)

        except Exception as e:

            print(
                "Could not copy file:",
                e
            )


# ============================================================
# SHAP FILES
# ============================================================

print("\n------------------------------------------------------------")
print("SHAP EXPLANATION")
print("------------------------------------------------------------")


shap_files = [
    "nitrogen_feature_importance.csv",
    "nitrogen_feature_importance.png",
    "nitrogen_shap_feature_importance.png",
    "nitrogen_shap_summary.png"
]


found_shap_files = []


for file in shap_files:

    path = os.path.join(
        SHAP_DIR,
        file
    )

    if os.path.exists(path):

        found_shap_files.append(path)

        destination = os.path.join(
            XAI_OUTPUT_DIR,
            file
        )

        shutil.copy2(
            path,
            destination
        )

        print("\nFound:", file)

        print(
            "Copied to:",
            destination
        )


# ============================================================
# SHAP SUMMARY
# ============================================================

print("\n------------------------------------------------------------")

if len(found_shap_files) == 4:

    print(
        "All 4 Nitrogen SHAP files found successfully!"
    )

else:

    print(
        f"{len(found_shap_files)} of 4 SHAP files found."
    )


# ============================================================
# FINAL XAI STATUS
# ============================================================

print("\n============================================================")
print("              XAI INTEGRATION STATUS")
print("============================================================")

if len(gradcam_matches) > 0:

    print("Grad-CAM: AVAILABLE")

else:

    print("Grad-CAM: NOT FOUND")


if len(found_shap_files) > 0:

    print("SHAP: AVAILABLE")

else:

    print("SHAP: NOT FOUND")


print("\nXAI output directory:")
print(XAI_OUTPUT_DIR)


print("\n============================================================")
print("          XAI INTEGRATION COMPLETED")
print("============================================================")