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

    # Resize the image to fit the canvas while maintaining the aspect ratio
    image_width, image_height = edges_image.size
    aspect_ratio = image_width / image_height
    if canvas_width / canvas_height > aspect_ratio:
        new_height = canvas_height
        new_width = int(new_height * aspect_ratio)
    else:
        new_width = canvas_width
        new_height = int(new_width / aspect_ratio)

    resized_image = edges_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Convert edges to numpy array
    edges_array = np.array(resized_image)
    height, width = edges_array.shape

    # Extract edge points
    edge_points = np.argwhere(edges_array > 128)

    # Center the image on the canvas
    offset_x = (canvas_width - new_width) // 2
    offset_y = (canvas_height - new_height) // 2
    centered_points = [(x + offset_x, y + offset_y) for y, x in edge_points]

    # Save points to file
    with open(output_file, "w") as file:
        for point in centered_points:
            file.write(f"{point[0]},{point[1]}\n")

    print(f"Points extracted and saved to {output_file}. Total points: {len(centered_points)}")