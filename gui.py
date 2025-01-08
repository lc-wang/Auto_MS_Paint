import tkinter as tk
from tkinter import filedialog, messagebox
from extract_points import extract_points
from draw import get_canvas_area, draw_points

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MS Paint Automation")
        self.create_widgets()

    def create_widgets(self):
        # Image Path
        tk.Label(self.root, text="Image Path:").grid(row=0, column=0, padx=10, pady=5)
        self.image_path_entry = tk.Entry(self.root, width=40)
        self.image_path_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_image).grid(row=0, column=2, padx=10, pady=5)

        # Output File Path
        tk.Label(self.root, text="Output File:").grid(row=1, column=0, padx=10, pady=5)
        self.output_file_entry = tk.Entry(self.root, width=40)
        self.output_file_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_output).grid(row=1, column=2, padx=10, pady=5)

        # Canvas Width
        tk.Label(self.root, text="Canvas Width:").grid(row=2, column=0, padx=10, pady=5)
        self.canvas_width_entry = tk.Entry(self.root, width=10)
        self.canvas_width_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.canvas_width_entry.insert(0, "800")

        # Canvas Height
        tk.Label(self.root, text="Canvas Height:").grid(row=3, column=0, padx=10, pady=5)
        self.canvas_height_entry = tk.Entry(self.root, width=10)
        self.canvas_height_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.canvas_height_entry.insert(0, "600")

        # Top Margin
        tk.Label(self.root, text="Top Margin:").grid(row=4, column=0, padx=10, pady=5)
        self.top_margin_entry = tk.Entry(self.root, width=10)
        self.top_margin_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.top_margin_entry.insert(0, "260")

        # Side Margin
        tk.Label(self.root, text="Side Margin:").grid(row=5, column=0, padx=10, pady=5)
        self.side_margin_entry = tk.Entry(self.root, width=10)
        self.side_margin_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        self.side_margin_entry.insert(0, "1000")

        # Bottom Margin
        tk.Label(self.root, text="Bottom Margin:").grid(row=6, column=0, padx=10, pady=5)
        self.bottom_margin_entry = tk.Entry(self.root, width=10)
        self.bottom_margin_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        self.bottom_margin_entry.insert(0, "100")

        # Extract Points Button
        tk.Button(self.root, text="Extract Points", command=self.extract_points).grid(row=7, column=0, columnspan=3, pady=10)

        # Draw Points Button
        tk.Button(self.root, text="Draw Points", command=self.draw_points).grid(row=8, column=0, columnspan=3, pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path_entry.insert(0, file_path)

    def browse_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.output_file_entry.insert(0, file_path)

    def extract_points(self):
        image_path = self.image_path_entry.get().strip()
        output_file = self.output_file_entry.get().strip()
        canvas_width = int(self.canvas_width_entry.get().strip())
        canvas_height = int(self.canvas_height_entry.get().strip())

        if not image_path or not output_file:
            messagebox.showerror("Error", "Please provide valid image and output file paths.")
            return

        try:
            extract_points(image_path, output_file, canvas_width, canvas_height)
            messagebox.showinfo("Success", f"Points extracted and saved to {output_file}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def draw_points(self):
        output_file = self.output_file_entry.get().strip()
        
        try:
            top_margin = int(self.top_margin_entry.get().strip())
            side_margin = int(self.side_margin_entry.get().strip())
            bottom_margin = int(self.bottom_margin_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Invalid margin values.")
            return

        screen_width, screen_height = pyautogui.size()
        canvas_x = side_margin
        canvas_y = top_margin
        canvas_width = screen_width - 2 * side_margin
        canvas_height = screen_height - top_margin - bottom_margin

        try:
            draw_points(output_file, canvas_x, canvas_y)
            messagebox.showinfo("Success", "Drawing completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()