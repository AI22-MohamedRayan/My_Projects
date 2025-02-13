import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(8, 6))
plt.subplot(2, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title('Grayscale Image')

blur = cv2.GaussianBlur(gray, (11, 11), 0)

plt.subplot(2, 2, 2)
plt.imshow(blur, cmap='gray')
plt.title('Blurred Image')

edges = cv2.Canny(blur, threshold1=30, threshold2=100)

dilated = cv2.dilate(edges, (3, 3), iterations=2)

plt.subplot(2, 2, 3)
plt.imshow(dilated, cmap='gray')
plt.title('Dilated Edges')

(cnt, _) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

plt.subplot(2, 2, 4)
plt.imshow(rgb)
plt.title('Contours Detected')

plt.tight_layout()
plt.show()

print("Counts of the freezer items in the image:", len(cnt))
