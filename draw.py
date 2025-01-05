import pyautogui
import time

# Get position of canvas in MS Paint 
print("Move to the top-left corner of the canvas and press Enter.")
input()
top_left = pyautogui.position()
print(f"Top-left corner: {top_left}")

print("Move to the bottom-right corner of the canvas and press Enter.")
input()
bottom_right = pyautogui.position()
print(f"Bottom-right corner: {bottom_right}")

canvas_x, canvas_y = top_left
canvas_width = bottom_right[0] - canvas_x
canvas_height = bottom_right[1] - canvas_y
print(f"Canvas area: ({canvas_x}, {canvas_y}, {canvas_width}, {canvas_height})")

# Load points from a file which is created by extract_points.py
def load_points(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            x, y = map(int, line.strip().split(","))
            points.append((x, y))
    return points

points_file = "pikachu_points.txt"
points = load_points(points_file)

# Assume points are scaled for a default canvas (800x600). Scale to the located canvas size
default_width, default_height = 800, 600
scale_x = canvas_width / default_width
scale_y = canvas_height / default_height

scaled_points = [
    (int(canvas_x + x * scale_x), int(canvas_y + y * scale_y)) for x, y in points
]

print("Drawing will start in 5 seconds. Switch to MS Paint.")
time.sleep(5)

pyautogui.moveTo(scaled_points[0][0], scaled_points[0][1])

# Draw the points
for i in range(1, len(scaled_points)):
    prev_x, prev_y = scaled_points[i - 1]
    curr_x, curr_y = scaled_points[i]

    # If the distance between points is small, draw; otherwise, lift the "pen"
    if abs(curr_x - prev_x) <= 2 and abs(curr_y - prev_y) <= 2:
        pyautogui.dragTo(curr_x, curr_y, duration=0.01, button="left")
    else:
        pyautogui.moveTo(curr_x, curr_y, duration=0.01)

print("Drawing completed!")
