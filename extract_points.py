from PIL import Image, ImageOps, ImageFilter
import numpy as np

def extract_points(image_path, output_file, canvas_width, canvas_height):
    """
    Extracts edge points from an image and saves them to a file.

    Args:
        image_path (str): Path to the input image.
        output_file (str): Path to the output file to save points.
        canvas_width (int): Width of the canvas.
        canvas_height (int): Height of the canvas.
    """
    # Load and process the image
    image = Image.open(image_path)

    # Convert to grayscale
    grayscale_image = ImageOps.grayscale(image)

    # Apply edge detection
    edges_image = grayscale_image.filter(ImageFilter.FIND_EDGES)

    # Convert edges to numpy array
    edges_array = np.array(edges_image)
    height, width = edges_array.shape

    # Extract edge points
    edge_points = np.argwhere(edges_array > 128)

    # Scale points to fit canvas
    scale_x = canvas_width / width
    scale_y = canvas_height / height
    scaled_points = [(int(x * scale_x), int(y * scale_y)) for y, x in edge_points]

    # Save points to file
    with open(output_file, "w") as file:
        for point in scaled_points:
            file.write(f"{point[0]},{point[1]}\n")

    print(f"Points extracted and saved to {output_file}. Total points: {len(scaled_points)}")
