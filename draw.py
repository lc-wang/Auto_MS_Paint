import pyautogui
import time


def get_canvas_area():
    """
    Manually or automatically determines the canvas area for MS Paint.

    Returns:
        tuple: (canvas_x, canvas_y, canvas_width, canvas_height)
    """
    # Define margins for MS Paint UI
    top_margin = 260    # Top menu
    side_margin = 1000  # Side toolbar
    bottom_margin = 100 # Bottom status bar

    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Define the canvas area with margins
    canvas_x = side_margin
    canvas_y = top_margin
    canvas_width = screen_width - 2 * side_margin
    canvas_height = screen_height - top_margin - bottom_margin

    return canvas_x, canvas_y, canvas_width, canvas_height


def read_points(input_file, canvas_x, canvas_y):
    """
    Reads points from a file and offsets them by the canvas position.

    Args:
        input_file (str): Path to the input points file.
        canvas_x (int): X-coordinate of the canvas's top-left corner.
        canvas_y (int): Y-coordinate of the canvas's top-left corner.

    Returns:
        list: Points adjusted to the canvas position as (x, y) tuples.
    """
    adjusted_points = []

    # Read and adjust points
    with open(input_file, "r") as infile:
        for line in infile:
            x, y = map(int, line.strip().split(","))
            adjusted_x = x + canvas_x
            adjusted_y = y + canvas_y
            adjusted_points.append((adjusted_x, adjusted_y))

    return adjusted_points


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

    # Get the canvas area
    canvas_x, canvas_y, canvas_width, canvas_height = get_canvas_area()
    print(f"Canvas area detected: ({canvas_x}, {canvas_y}, {canvas_width}, {canvas_height})")

    # Read and adjust points to match the canvas position
    points = read_points(input_file, canvas_x, canvas_y)
    print(f"Total points to draw: {len(points)}")

    # Draw the points
    draw_points(points)
