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

OUTPUT_PATH = r"C:\Users\SILVERU SANJANA\OneDrive\Desktop\Soil_Project\XAI\GradCAM_Test"


# ============================================================
# CLASSES
# ============================================================

CLASS_NAMES = [
    "Alluvial",
    "Arid",
    "Black",
    "Laterite",
    "Mountain",
    "Red",
    "Yellow"
]


# ============================================================
# DEVICE
# ============================================================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Device:", device)


# ============================================================
# LOAD RESNET-50
# ============================================================

model = models.resnet50(weights=None)

model.fc = torch.nn.Linear(
    model.fc.in_features,
    7
)

state_dict = torch.load(
    MODEL_PATH,
    map_location=device
)

model.load_state_dict(state_dict)

model = model.to(device)
model.eval()

print("ResNet-50 loaded successfully!")


# ============================================================
# TRANSFORM
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
# FIND ONE IMAGE
# ============================================================

image_path = None

for root, dirs, files in os.walk(DATASET_PATH):

    for file in files:

        if file.lower().endswith(
            (".jpg", ".jpeg", ".png", ".bmp")
        ):

            image_path = os.path.join(
                root,
                file
            )

            break

    if image_path:
        break


if image_path is None:

    print("ERROR: No image found!")

    raise SystemExit


print()
print("Test image:")
print(image_path)


# ============================================================
# LOAD IMAGE
# ============================================================

image = Image.open(
    image_path
).convert("RGB")

original = np.array(image)


# ============================================================
# PREPARE IMAGE
# ============================================================

input_tensor = transform(
    image
).unsqueeze(0).to(device)

input_tensor.requires_grad_(True)


# ============================================================
# HOOK FOR GRAD-CAM
# ============================================================

activations = None
gradients = None


def forward_hook(module, input, output):

    global activations

    activations = output


def backward_hook(module, grad_input, grad_output):

    global gradients

    gradients = grad_output[0]


target_layer = model.layer4[-1]

target_layer.register_forward_hook(
    forward_hook
)

target_layer.register_full_backward_hook(
    backward_hook
)


# ============================================================
# PREDICTION
# ============================================================

output = model(input_tensor)

probabilities = torch.softmax(
    output,
    dim=1
)

predicted_class = torch.argmax(
    probabilities,
    dim=1
).item()

confidence = probabilities[
    0,
    predicted_class
].item()

predicted_name = CLASS_NAMES[
    predicted_class
]


print()
print("Prediction:", predicted_name)
print(
    f"Confidence: {confidence * 100:.2f}%"
)


# ============================================================
# BACKPROPAGATION
# ============================================================

model.zero_grad()

score = output[
    0,
    predicted_class
]

score.backward()


# ============================================================
# GENERATE GRAD-CAM
# ============================================================

weights = gradients.mean(
    dim=(2, 3),
    keepdim=True
)

cam = (
    weights * activations
).sum(dim=1)

cam = torch.relu(cam)

cam = cam.detach().cpu().numpy()[0]

cam = cam - cam.min()

if cam.max() != 0:

    cam = cam / cam.max()


# ============================================================
# RESIZE CAM
# ============================================================

cam = cv2.resize(
    cam,
    (
        original.shape[1],
        original.shape[0]
    )
)


# ============================================================
# HEATMAP
# ============================================================

heatmap = np.uint8(
    255 * cam
)

heatmap = cv2.applyColorMap(
    heatmap,
    cv2.COLORMAP_JET
)


# ============================================================
# ORIGINAL IMAGE
# ============================================================

original_bgr = cv2.cvtColor(
    original,
    cv2.COLOR_RGB2BGR
)


# ============================================================
# OVERLAY
# ============================================================

overlay = cv2.addWeighted(
    original_bgr,
    0.6,
    heatmap,
    0.4,
    0
)


# ============================================================
# SAVE RESULTS
# ============================================================

os.makedirs(
    OUTPUT_PATH,
    exist_ok=True
)

cv2.imwrite(
    os.path.join(
        OUTPUT_PATH,
        "original.jpg"
    ),
    original_bgr
)

cv2.imwrite(
    os.path.join(
        OUTPUT_PATH,
        "heatmap.jpg"
    ),
    heatmap
)

cv2.imwrite(
    os.path.join(
        OUTPUT_PATH,
        "gradcam_overlay.jpg"
    ),
    overlay
)


# ============================================================
# DONE
# ============================================================

print()
print("==========================================")
print("GRAD-CAM TEST COMPLETED")
print("==========================================")

print("Original:")
print(
    os.path.join(
        OUTPUT_PATH,
        "original.jpg"
    )
)

print("Heatmap:")
print(
    os.path.join(
        OUTPUT_PATH,
        "heatmap.jpg"
    )
)

print("Overlay:")
print(
    os.path.join(
        OUTPUT_PATH,
        "gradcam_overlay.jpg"
    )
)

print("==========================================")