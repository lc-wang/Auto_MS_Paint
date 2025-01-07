from extract_points import extract_points
from draw import get_canvas_area, draw_points

if __name__ == "__main__":
    print("Welcome to the Pikachu Drawing Script!")
    
    # Step 1: Extract Edge Points
    print("\nStep 1: Extract edge points from an image.")
    image_path = input("Enter the path to the image file (default: char-pikachu.png): ").strip() or "char-pikachu.png"
    output_file = input("Enter the output points file name (default: pikachu_points.txt): ").strip() or "pikachu_points.txt"
    canvas_width = int(input("Enter the canvas width (default: 800): ").strip() or "800")
    canvas_height = int(input("Enter the canvas height (default: 600): ").strip() or "600")

    # Extract points using the function from extract_points.py
    extract_points(image_path, output_file, canvas_width, canvas_height)
    print(f"Points extracted and saved to {output_file}.")

    # Step 2: Get Canvas Area
    print("\nStep 2: Detect canvas area in MS Paint.")
    canvas_x, canvas_y, canvas_width, canvas_height = get_canvas_area()
    print(f"Canvas area detected: ({canvas_x}, {canvas_y}, {canvas_width}, {canvas_height})")

    # Step 3: Draw the Points
    print("\nStep 3: Draw the points in MS Paint.")
    draw_points(output_file, canvas_x, canvas_y)
    print("Drawing completed!")
