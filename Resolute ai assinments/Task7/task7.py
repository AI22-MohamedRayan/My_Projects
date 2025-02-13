import cv2
import numpy as np
import matplotlib.pyplot as plt
import torch
from torchvision import models, transforms

def load_image(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image, image_rgb

def preprocess_image(image_rgb):
    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.ToTensor()
    ])
    return transform(image_rgb).unsqueeze(0)

def load_model():
    model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()
    return model

def run_inference(model, image_tensor):
    with torch.no_grad():
        outputs = model(image_tensor)
    return outputs

def filter_boxes(outputs, threshold=0.5):
    boxes = outputs[0]['boxes']
    scores = outputs[0]['scores']
    filtered_boxes = boxes[scores > threshold]
    return filtered_boxes

def draw_boxes(image, boxes):
    for box in boxes:
        x1, y1, x2, y2 = box.int().numpy()
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
    return image

def count_boxes(image_path):
    image, image_rgb = load_image(image_path)
    image_tensor = preprocess_image(image_rgb)
    model = load_model()
    outputs = run_inference(model, image_tensor)
    filtered_boxes = filter_boxes(outputs)
    count = len(filtered_boxes)
    print(f"Total number of boxes: {count}")
    image_with_boxes = draw_boxes(image, filtered_boxes)
    plt.imshow(cv2.cvtColor(image_with_boxes, cv2.COLOR_BGR2RGB))
    plt.title(f"Total number of boxes: {count}")
    plt.show()

image_path = '1.jpg'
count_boxes(image_path)
