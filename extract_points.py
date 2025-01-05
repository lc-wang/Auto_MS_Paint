from PIL import Image, ImageOps, ImageFilter
import numpy as np

# Step 1: Load and process the image
image_path = "char-pikachu.png"  # Make sure the image file is in the same directory
image = Image.open(image_path)

# Convert the image to grayscale
grayscale_image = ImageOps.grayscale(image)

# Apply edge detection
edges_image = grayscale_image.filter(ImageFilter.FIND_EDGES)

# Step 2: Extract edge points
edges_array = np.array(edges_image)  # Convert image to numpy array
height, width = edges_array.shape

# Find points where the pixel intensity is greater than a threshold (128)
edge_points = np.argwhere(edges_array > 128)

# Step 3: Scale the points to fit the MS Paint canvas
canvas_width = 400  # Width of MS Paint canvas
canvas_height = 600  # Height of MS Paint canvas
scale_x = 1 # canvas_width / width
scale_y = 1 # canvas_height / height

# Scale the points
scaled_points = [(int(x * scale_x), int(y * scale_y)) for y, x in edge_points]

# Step 4: Save the points to a file
output_file = "pikachu_points.txt"
with open(output_file, "w") as file:
    for point in scaled_points:
        file.write(f"{point[0]},{point[1]}\n")

print(f"Points saved to {output_file}. Total points: {len(scaled_points)}")
