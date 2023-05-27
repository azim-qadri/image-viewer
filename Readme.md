# Python Tkinter Image Viewer

This is a simple image viewer created using Python and Tkinter. It allows you to view and navigate through a collection of images.

## Features

- Displays images in a fullscreen window
- Supports navigation through images using arrow keys and on-screen buttons
- Resizes images to fit the screen while maintaining aspect ratio
- Supports common image formats such as JPG, JPEG, PNG, GIF, and ICO

## Prerequisites

- Python 3.x
- Tkinter library
- PIL (Python Imaging Library) library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/azim-qadri/image-viewer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd image-viewer
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open a terminal or command prompt.

2. Navigate to the project directory.

3. Run the following command to start the image viewer:

   ```bash
   python image_viewer.py
   ```

4. The image viewer window will open in fullscreen mode.

5. Use the right arrow key or click the forward button to navigate to the next image.

6. Use the left arrow key or click the backward button to navigate to the previous image.

7. Press the Escape key or close the window to exit the image viewer.

## Customization

- To change the directory containing the images, modify the `directory` variable in the code. Replace the path `"C:\Users\User\PycharmProjects\Viewer"` with the desired directory path.

- To change the forward and backward buttons' images, replace the `"forward.png"` and `"back.png"` files with your own button images. Make sure to maintain the same file names and file formats.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The Tkinter library: [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)
- The PIL (Python Imaging Library) library: [https://pillow.readthedocs.io/en/stable/](https://pillow.readthedocs.io/en/stable/)

Feel free to modify and enhance this image viewer according to your needs. Happy viewing!