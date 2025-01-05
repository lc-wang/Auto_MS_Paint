import pyautogui
import time

def scale_points(input_file, canvas_x, canvas_y, canvas_width, canvas_height, original_width, original_height):
    """
    Scales points to fit the specified canvas area.

    Args:
        input_file (str): Path to the input points file.
        canvas_x (int): X-coordinate of the top-left corner of the canvas.
        canvas_y (int): Y-coordinate of the top-left corner of the canvas.
        canvas_width (int): Width of the canvas.
        canvas_height (int): Height of the canvas.
        original_width (int): Original width of the drawing.
        original_height (int): Original height of the drawing.

    Returns:
        list: Scaled points as (x, y) tuples.
    """
    # Calculate scaling factors
    scale_x = canvas_width / original_width
    scale_y = canvas_height / original_height

    scaled_points = []

    # Read and scale points
    with open(input_file, "r") as infile:
        for line in infile:
            x, y = map(int, line.strip().split(","))
            scaled_x = int(x * scale_x) + canvas_x
            scaled_y = int(y * scale_y) + canvas_y
            scaled_points.append((scaled_x, scaled_y))

    return scaled_points


def get_canvas_area():
    """
    Manually or automatically determines the canvas area for MS Paint.

    Returns:
        tuple: (canvas_x, canvas_y, canvas_width, canvas_height)
    """
    # Define margins for MS Paint UI
    top_margin = 260    # Top menu
    side_margin = 1000   # Side toolbar
    bottom_margin = 100 # Bottom status bar

    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Define the canvas area with margins
    canvas_x = side_margin
    canvas_y = top_margin
    canvas_width = screen_width - 2 * side_margin
    canvas_height = screen_height - top_margin - bottom_margin

    return canvas_x, canvas_y, canvas_width, canvas_height


def draw_points(points):
    """
    Draws the given points using PyAutoGUI.

    Args:
        points (list): List of (x, y) tuples to draw.
    """
    print("Starting to draw in 5 seconds. Switch to MS Paint...")
    time.sleep(5)

    # Start drawing
    pyautogui.moveTo(points[0][0], points[0][1])

    # Draw the points
    for i in range(1, len(points)):
        prev_x, prev_y = points[i - 1]
        curr_x, curr_y = points[i]
        # If the distance between points is small, draw; otherwise, lift the "pen"
        if abs(curr_x - prev_x) <= 2 and abs(curr_y - prev_y) <= 2:
            pyautogui.dragTo(curr_x, curr_y, duration=0.01, button="left")
        else:
            pyautogui.moveTo(curr_x, curr_y, duration=0.01)


# Main execution
if __name__ == "__main__":
    input_file = "pikachu_points.txt"  # Input points file
    original_width = 800  # Original width of the drawing
    original_height = 600  # Original height of the drawing

    # Get the canvas area
    canvas_x, canvas_y, canvas_width, canvas_height = get_canvas_area()
    print(f"Canvas area detected: ({canvas_x}, {canvas_y}, {canvas_width}, {canvas_height})")

    # Scale points to fit the canvas
    scaled_points = scale_points(
        input_file, canvas_x, canvas_y, canvas_width, canvas_height, original_width, original_height
    )
    print(f"Total points to draw: {len(scaled_points)}")

    # Draw the scaled points
    draw_points(scaled_points)
