import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def create_image():
    img = np.zeros((100, 100), dtype=np.uint8)
    cv2.rectangle(img, (20, 20), (40, 80), 85, -1)
    cv2.circle(img, (70, 50), 15, 170, -1)
    return img

def add_gaussian_noise(img, mean=0, sigma=20):
    noise = np.random.normal(mean, sigma, img.shape).astype(np.float32)
    noisy_img = img + noise
    noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
    return noisy_img

def apply_otsu_threshold(img):
    _, otsu_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return otsu_thresh

# Main
synthetic_input = create_image()
cv2.imwrite("input_image.png", synthetic_input) 

noisy = add_gaussian_noise(synthetic_input)
otsu_result = apply_otsu_threshold(noisy)

# Save outputs
cv2.imwrite("results/task1_noisy_image.png", noisy)
cv2.imwrite("results/task1_otsu_result.png", otsu_result)

# Display and save combined
plt.figure(figsize=(10, 3))
plt.subplot(1, 3, 1)
plt.title('Input Image')
plt.imshow(synthetic_input, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Noisy Image')
plt.imshow(noisy, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Otsu Result')
plt.imshow(otsu_result, cmap='gray')
plt.tight_layout()
plt.savefig("results/task1_otsu_all_combined.png")
plt.show()
