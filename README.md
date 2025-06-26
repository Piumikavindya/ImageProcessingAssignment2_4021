# ImageProcessingAssignment2_4021

# EC7212 – Computer Vision and Image Processing  
## Take Home Assignment 2 – Python Image Processing Tasks  
### Kavindya P.P - EG/2020/4021  

---

### Tasks  

1. **Otsu Thresholding with Gaussian Noise**  
   - Generate a synthetic image with 2 objects and 1 background (3 pixel values).
   - Add Gaussian noise to the image.
   - Apply **Otsu’s Thresholding Algorithm**.

2. **Region Growing Segmentation**  
   - Implement region growing starting from seed points inside the object.
   - Recursively add neighboring pixels within a pre-defined intensity range.

---

### Output
All generated results will be saved in the `results/` folder:
- `input_synthetic_image.png` – Clean synthetic image for Task 1.
- `noisy_image.png` – Gaussian noise added.
- `otsu_result.png` – Binary result from Otsu’s method.
- `otsu_all_combined.png` – Combined visualization of all above.

- `input_synthetic_image_region.png` – Synthetic image used for region growing.
- `region_segmented.png` – Final result of region growing.
- `region_combined.png` – Side-by-side input and output for Task 2.

---

### Run Instructions

```bash
python task1_otsu_gaussian_noise.py
python task2_region_growing.py
