import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import time
from PIL import Image, ImageFilter, ImageGrab
from extract_points import extract_points
from draw import draw_points
from pynput import mouse


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MS Paint Automation")
        self.create_widgets()
        self.top_left = None
        self.bottom_right = None

    def create_widgets(self):
        # Image Path
        tk.Label(self.root, text="Image Path:").grid(row=0, column=0, padx=10, pady=5)
        self.image_path_entry = tk.Entry(self.root, width=40)
        self.image_path_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_image).grid(
            row=0, column=2, padx=10, pady=5
        )

        # Output File Path
        tk.Label(self.root, text="Output File:").grid(row=1, column=0, padx=10, pady=5)
        self.output_file_entry = tk.Entry(self.root, width=40)
        self.output_file_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_output).grid(
            row=1, column=2, padx=10, pady=5
        )

        # Set Canvas Area
        tk.Button(self.root, text="Set Canvas Area", command=self.set_canvas_area).grid(
            row=2, column=0, columnspan=3, pady=10
        )

        # Extract Points Button
        tk.Button(self.root, text="Extract Points", command=self.extract_points).grid(
            row=3, column=0, columnspan=3, pady=10
        )

        # Draw Points Button
        tk.Button(self.root, text="Draw Points", command=self.draw_points).grid(
            row=4, column=0, columnspan=3, pady=10
        )

    def browse_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if file_path:
            self.image_path_entry.delete(0, tk.END)
            self.image_path_entry.insert(0, file_path)

    def browse_output(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")]
        )
        if file_path:
            self.output_file_entry.delete(0, tk.END)
            self.output_file_entry.insert(0, file_path)

    def set_canvas_area(self):
        self.top_left = None
        self.bottom_right = None

        def on_button_press(event):
            self.top_left = (event.x_root, event.y_root)

        def on_button_release(event):
            self.bottom_right = (event.x_root, event.y_root)
            self.canvas_area_selected()
            capture_window.destroy()

        # Create a transparent fullscreen window to capture mouse events
        capture_window = tk.Toplevel(self.root)
        capture_window.attributes("-fullscreen", True)
        capture_window.attributes("-alpha", 0.3)  # Make it semi-transparent
        capture_window.bind("<ButtonPress-1>", on_button_press)
        capture_window.bind("<ButtonRelease-1>", on_button_release)

        capture_window.mainloop()

    def canvas_area_selected(self):
        if self.top_left and self.bottom_right:
            self.calculate_canvas_size()
            messagebox.showinfo(
                "Instruction",
                f"Canvas area set: ({self.canvas_x}, {self.canvas_y}, {self.canvas_width}, {self.canvas_height})",
            )
        else:
            messagebox.showerror(
                "Error", "Failed to capture canvas area. Please try again."
            )

    def calculate_canvas_size(self):
        if self.top_left and self.bottom_right:
            self.canvas_x, self.canvas_y = self.top_left
            bottom_right_x, bottom_right_y = self.bottom_right
            self.canvas_width = bottom_right_x - self.canvas_x
            self.canvas_height = bottom_right_y - self.canvas_y
            messagebox.showinfo(
                "Instruction",
                f"Canvas area set: ({self.canvas_x}, {self.canvas_y}, {self.canvas_width}, {self.canvas_height})",
            )

    def extract_points(self):
        image_path = self.image_path_entry.get().strip()
        output_file = self.output_file_entry.get().strip()

        if not image_path or not output_file:
            messagebox.showerror(
                "Error", "Please provide valid image and output file paths."
            )
            return

        if not hasattr(self, "canvas_width") or not hasattr(self, "canvas_height"):
            messagebox.showerror(
                "Error", "Canvas area not set. Please set the canvas area first."
            )
            return

        try:
            extract_points(
                image_path, output_file, self.canvas_width, self.canvas_height
            )
            messagebox.showinfo(
                "Success", f"Points extracted and saved to {output_file}."
            )
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def draw_points(self):
        output_file = self.output_file_entry.get().strip()

        if not hasattr(self, "canvas_x") or not hasattr(self, "canvas_y"):
            messagebox.showerror(
                "Error", "Canvas area not set. Please set the canvas area first."
            )
            return

        try:
            draw_points(output_file, self.canvas_x, self.canvas_y)
            messagebox.showinfo("Success", "Drawing completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
