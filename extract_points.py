from PIL import Image, ImageOps, ImageFilter
import numpy as np

def main():
    # Step 1: Get user inputs
    image_path = input("Enter the path to the Pikachu image (default: char-pikachu.png): ").strip() or "char-pikachu.png"
    output_file = input("Enter the output file path (default: pikachu_points.txt): ").strip() or "pikachu_points.txt"

    try:
        canvas_width = int(input("Enter the MS Paint canvas width (default: 800): ").strip() or "800")
        canvas_height = int(input("Enter the MS Paint canvas height (default: 600): ").strip() or "600")
    except ValueError:
        print("Invalid input for canvas dimensions. Using default values: width=800, height=600.")
        canvas_width, canvas_height = 800, 600

    print("\n--- User Inputs ---")
    print(f"Image Path: {image_path}")
    print(f"Output File: {output_file}")
    print(f"Canvas Dimensions: {canvas_width}x{canvas_height}")
    print("-------------------\n")

    # Step 2: Load and process the image
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: File not found at {image_path}. Please check the path and try again.")
        return

    # Convert the image to grayscale
    grayscale_image = ImageOps.grayscale(image)

    # Apply edge detection
    edges_image = grayscale_image.filter(ImageFilter.FIND_EDGES)

    # Step 3: Extract edge points
    edges_array = np.array(edges_image)  # Convert image to numpy array
    height, width = edges_array.shape

    # Find points where the pixel intensity is greater than a threshold (128)
    edge_points = np.argwhere(edges_array > 128)

    # Step 4: Scale the points to fit the MS Paint canvas
    scale_x = canvas_width / width
    scale_y = canvas_height / height

    # Scale the points
    scaled_points = [(int(x * scale_x), int(y * scale_y)) for y, x in edge_points]

    # Step 5: Save the points to a file
    with open(output_file, "w") as file:
        for point in scaled_points:
            file.write(f"{point[0]},{point[1]}\n")

    print(f"Points saved to {output_file}. Total points: {len(scaled_points)}")

if __name__ == "__main__":
    main()
