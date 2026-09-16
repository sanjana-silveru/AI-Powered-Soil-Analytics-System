import os
import cv2
import torch
import numpy as np
from PIL import Image
from torchvision import models, transforms

# ============================================================
# PATHS
# ============================================================

MODEL_PATH = r"C:\Users\SILVERU SANJANA\OneDrive\Desktop\Soil_Project\CNN_Model\best_resnet50_soil_model.pth"

DATASET_PATH = r"C:\Users\SILVERU SANJANA\OneDrive\Desktop\Soil_Project\Cleaned_Dataset"

OUTPUT_PATH = r"C:\Users\SILVERU SANJANA\OneDrive\Desktop\Soil_Project\XAI\GradCAM"

# ============================================================
# CLASS NAMES
# ============================================================

CLASS_NAMES = [
    "Alluvial_Soil",
    "Arid_Soil",
    "Black_Soil",
    "Laterite_Soil",
    "Mountain_Soil",
    "Red_Soil",
    "Yellow_Soil"
]

# ============================================================
# DEVICE
# ============================================================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Device:", device)

# ============================================================
# LOAD RESNET-50
# ============================================================

model = models.resnet50(weights=None)

# 7 soil classes
model.fc = torch.nn.Linear(model.fc.in_features, 7)

# Load trained weights
state_dict = torch.load(
    MODEL_PATH,
    map_location=device
)

model.load_state_dict(state_dict)

model = model.to(device)
model.eval()

print("ResNet-50 loaded successfully!")

# ============================================================
# PREPROCESSING
# ============================================================

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# ============================================================
# GRAD-CAM CLASS
# ============================================================

class GradCAM:

    def __init__(self, model, target_layer):

        self.model = model
        self.target_layer = target_layer

        self.activations = None
        self.gradients = None

        self.forward_hook = target_layer.register_forward_hook(
            self.save_activation
        )

        self.backward_hook = target_layer.register_full_backward_hook(
            self.save_gradient
        )

    def save_activation(self, module, input, output):
        self.activations = output.detach()

    def save_gradient(self, module, grad_input, grad_output):
        self.gradients = grad_output[0].detach()

    def generate(self, image_tensor, class_index):

        # Clear previous gradients
        self.model.zero_grad()

        # Forward pass
        output = self.model(image_tensor)

        # Select target class
        score = output[0, class_index]

        # Backward pass
        score.backward()

        # Get activations and gradients
        activations = self.activations[0]
        gradients = self.gradients[0]

        # Global average pooling of gradients
        weights = gradients.mean(dim=(1, 2))

        # Weighted combination
        cam = torch.zeros(
            activations.shape[1:],
            device=activations.device
        )

        for i, weight in enumerate(weights):
            cam += weight * activations[i]

        # ReLU
        cam = torch.relu(cam)

        # Move to CPU
        cam = cam.cpu().numpy()

        # Normalize
        cam -= cam.min()

        if cam.max() != 0:
            cam /= cam.max()

        return cam


# ============================================================
# TARGET LAYER
# ============================================================

target_layer = model.layer4[-1]

gradcam = GradCAM(
    model,
    target_layer
)

print("Grad-CAM target layer:", target_layer)

# ============================================================
# CREATE OUTPUT DIRECTORY
# ============================================================

os.makedirs(OUTPUT_PATH, exist_ok=True)

# ============================================================
# PROCESS IMAGES
# ============================================================

total_images = 0
successful = 0
failed = 0

for class_name in CLASS_NAMES:

    class_folder = os.path.join(
        DATASET_PATH,
        class_name
    )

    if not os.path.exists(class_folder):

        print("Folder not found:", class_folder)

        continue

    # Create output folder
    output_folder = os.path.join(
        OUTPUT_PATH,
        class_name
    )

    os.makedirs(output_folder, exist_ok=True)

    print("\nProcessing:", class_name)

    image_files = [
        f for f in os.listdir(class_folder)
        if f.lower().endswith(
            (".jpg", ".jpeg", ".png", ".bmp")
        )
    ]

    print("Images found:", len(image_files))

    for image_file in image_files:

        total_images += 1

        image_path = os.path.join(
            class_folder,
            image_file
        )

        try:

            # ------------------------------------------------
            # Load image
            # ------------------------------------------------

            original = Image.open(image_path).convert("RGB")

            original_np = np.array(original)

            # ------------------------------------------------
            # Prepare tensor
            # ------------------------------------------------

            input_tensor = transform(original).unsqueeze(0)

            input_tensor = input_tensor.to(device)

            # ------------------------------------------------
            # Prediction
            # ------------------------------------------------

            model.zero_grad()

            output = model(input_tensor)

            probabilities = torch.softmax(
                output,
                dim=1
            )

            confidence, predicted_class = torch.max(
                probabilities,
                dim=1
            )

            predicted_index = predicted_class.item()

            predicted_name = CLASS_NAMES[predicted_index]

            confidence_value = confidence.item() * 100

            # ------------------------------------------------
            # Generate Grad-CAM
            # ------------------------------------------------

            cam = gradcam.generate(
                input_tensor,
                predicted_index
            )

            # ------------------------------------------------
            # Resize CAM
            # ------------------------------------------------

            cam = cv2.resize(
                cam,
                (original_np.shape[1], original_np.shape[0])
            )

            # ------------------------------------------------
            # Create heatmap
            # ------------------------------------------------

            heatmap = np.uint8(
                255 * cam
            )

            heatmap = cv2.applyColorMap(
                heatmap,
                cv2.COLORMAP_JET
            )

            # Convert RGB → BGR
            original_bgr = cv2.cvtColor(
                original_np,
                cv2.COLOR_RGB2BGR
            )

            # ------------------------------------------------
            # Overlay
            # ------------------------------------------------

            overlay = cv2.addWeighted(
                original_bgr,
                0.6,
                heatmap,
                0.4,
                0
            )

            # ------------------------------------------------
            # Save files
            # ------------------------------------------------

            base_name = os.path.splitext(
                image_file
            )[0]

            original_output = os.path.join(
                output_folder,
                base_name + "_original.jpg"
            )

            heatmap_output = os.path.join(
                output_folder,
                base_name + "_heatmap.jpg"
            )

            overlay_output = os.path.join(
                output_folder,
                base_name
                + "_GradCAM_"
                + predicted_name
                + "_"
                + str(round(confidence_value))
                + "pct.jpg"
            )

            cv2.imwrite(
                original_output,
                original_bgr
            )

            cv2.imwrite(
                heatmap_output,
                heatmap
            )

            cv2.imwrite(
                overlay_output,
                overlay
            )

            successful += 1

            # Print progress every image
            print(
                f"[{successful}/{total_images}] "
                f"{class_name}/{image_file} -> "
                f"{predicted_name} "
                f"({confidence_value:.2f}%)"
            )

        except Exception as e:

            failed += 1

            print(
                "ERROR:",
                image_path
            )

            print(e)

# ============================================================
# FINAL RESULT
# ============================================================

print("\n==========================================")
print("GRAD-CAM PROCESSING COMPLETED")
print("==========================================")

print("Total images:", total_images)
print("Successful:", successful)
print("Failed:", failed)

print("\nResults saved at:")

print(OUTPUT_PATH)