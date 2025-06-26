import numpy as np
import cv2
import matplotlib.pyplot as plt
from collections import deque
import os

def create_image():
    img = np.zeros((100, 100), dtype=np.uint8)
    cv2.rectangle(img, (20, 20), (40, 80), 85, -1)
    cv2.circle(img, (70, 50), 15, 170, -1)
    return img

def region_growing(img, seed, threshold=10):
    visited = np.zeros_like(img, dtype=bool)
    segmented = np.zeros_like(img, dtype=np.uint8)

    rows, cols = img.shape
    seed_val = img[seed]
    queue = deque([seed])
    visited[seed] = True

    while queue:
        r, c = queue.popleft()
        segmented[r, c] = 255

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr, nc]:
                    if abs(int(img[nr, nc]) - int(seed_val)) <= threshold:
                        visited[nr, nc] = True
                        queue.append((nr, nc))
    return segmented

synthetic_input = create_image()
cv2.imwrite("input_image_region.png", synthetic_input) 

seed_point = (30, 30)
segmented_img = region_growing(synthetic_input, seed=seed_point, threshold=15)

cv2.imwrite("results/task2_region_segmented.png", segmented_img)

# Display and save combined
plt.figure(figsize=(8, 3))
plt.subplot(1, 2, 1)
plt.title("Input Image")
plt.imshow(synthetic_input, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Segmented Image")
plt.imshow(segmented_img, cmap='gray')
plt.tight_layout()
plt.savefig("results/task2_region_combined.png")
plt.show()
