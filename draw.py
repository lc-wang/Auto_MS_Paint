import pyautogui
import time

def get_canvas_area():
    """
    Prompts the user for margin values to determine the canvas area for MS Paint.

    Returns:
        tuple: (canvas_x, canvas_y, canvas_width, canvas_height)
    """
    try:
        top_margin = int(input("Enter the top margin (default: 260): ").strip() or "260")
        side_margin = int(input("Enter the side margin (default: 1000): ").strip() or "1000")
        bottom_margin = int(input("Enter the bottom margin (default: 100): ").strip() or "100")
    except ValueError:
        print("Invalid input. Using default margin values: top=260, side=1000, bottom=100.")
        top_margin, side_margin, bottom_margin = 260, 1000, 100

    screen_width, screen_height = pyautogui.size()
    canvas_x = side_margin
    canvas_y = top_margin
    canvas_width = screen_width - 2 * side_margin
    canvas_height = screen_height - top_margin - bottom_margin

    return canvas_x, canvas_y, canvas_width, canvas_height


def draw_points(input_file, canvas_x, canvas_y):
    """
    Draws points from a file using PyAutoGUI.

    Args:
        input_file (str): Path to the points file.
        canvas_x (int): X-coordinate of the canvas's top-left corner.
        canvas_y (int): Y-coordinate of the canvas's top-left corner.
    """
    adjusted_points = []
    with open(input_file, "r") as infile:
        for line in infile:
            x, y = map(int, line.strip().split(","))
            adjusted_x = x + canvas_x
            adjusted_y = y + canvas_y
            adjusted_points.append((adjusted_x, adjusted_y))

    print("Starting to draw in 5 seconds. Switch to MS Paint...")
    time.sleep(5)

    pyautogui.moveTo(adjusted_points[0][0], adjusted_points[0][1])
    for i in range(1, len(adjusted_points)):
        prev_x, prev_y = adjusted_points[i - 1]
        curr_x, curr_y = adjusted_points[i]
        if abs(curr_x - prev_x) <= 2 and abs(curr_y - prev_y) <= 2:
            pyautogui.dragTo(curr_x, curr_y, duration=0.01, button="left")
        else:
            pyautogui.moveTo(curr_x, curr_y, duration=0.01)
