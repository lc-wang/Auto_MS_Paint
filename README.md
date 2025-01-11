# Auto_MS_Paint

Auto_MS_Paint is a Python-based tool designed to automate the process of drawing in MS Paint. This tool extracts points from an image and reproduces them on the MS Paint canvas. It supports drag-and-drop file functionality and allows users to draw points either sequentially or in random order.

## Features

- **Drag-and-Drop File Support**: Easily drag and drop image and output files into the application.
- **Canvas Area Selection**: Set a specific area on the MS Paint canvas to draw.
- **Point Extraction**: Extract points from an image and save them to an output file.
- **Random Drawing**: Option to draw points in a random order.
- **Sequential Drawing**: Option to draw points in a sequential order.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/lc-wang/Auto_MS_Paint.git
    cd Auto_MS_Paint
    ```

2. **Install Dependencies**:
    Make sure you have Python installed. Then, install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install tkinterdnd2**:
    ```bash
    pip install tkinterdnd2
    ```

## Usage

1. **Run the Application**:
    ```bash
    python gui.py
    ```

2. **Set Image and Output File Paths**:
    - Use the "Browse" button or drag-and-drop files into the respective fields.

3. **Select Canvas Area**:
    - Click on "Set Canvas Area" and select the area on the screen where MS Paint is open.

4. **Extract Points**:
    - Click on "Extract Points" to extract points from the selected image and save them to the output file.

5. **Draw Points**:
    - Click on "Draw Points" to start drawing on the MS Paint canvas. You can choose to draw in random order by checking the "Draw in Random Order" checkbox.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **tkinterdnd2**: For providing drag-and-drop support in Tkinter.
- **pyautogui**: For enabling automation of mouse and keyboard actions.
