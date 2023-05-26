from tkinter import *
from PIL import ImageTk, Image
import os
import ctypes


# Functions for navigating through the images
def show_image(image_no):
    global my_label
    my_label.destroy()
    my_label = Label(frame, image=image_list[image_no - 1])
    my_label.place(relx=0.5, rely=0.5, anchor=CENTER)


def move_forward(move=True):
    global current_image
    if current_image < len(image_list):
        current_image += 1
        show_image(current_image)


def move_backward(move=True):
    global current_image
    if current_image > 1:
        current_image -= 1
        show_image(current_image)


ctypes.windll.shcore.SetProcessDpiAwareness(2)
root = Tk()
root.title('Image Viewer')
root.state("zoomed")
root.configure(bg="black")
frame_width = root.winfo_screenwidth()
frame_height = int(root.winfo_screenheight() // 1.08)
frame = Frame(root, width=frame_width, height=frame_height)
frame.grid(row=0, column=0, sticky="NW")
directory = r"C:\Users\User\PycharmProjects\Viewer"
file_names = os.listdir(directory)
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".ico"]
image_files = [file for file in file_names if os.path.splitext(file)[1].lower() in image_extensions]
image_list = []
for file in image_files:
    image_path = os.path.join(directory, file)
    img = Image.open(image_path)
    if img.size[0] > root.winfo_screenwidth() or img.size[1] > root.winfo_screenheight():
        myheight = int(root.winfo_screenheight() // 1.08)
        hpercent = (myheight / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, myheight), Image.LANCZOS)
        picture = ImageTk.PhotoImage(image=img)
    else:
        img = img.resize((int(img.size[0] / 1.13), int(img.size[1] // 1.08)), Image.LANCZOS)
        picture = ImageTk.PhotoImage(image=img)
    image_list.append(picture)
for_img = ImageTk.PhotoImage(Image.open("forward.png").resize((50, 50)))
back_img = ImageTk.PhotoImage(Image.open("back.png").resize((50, 50)))
# Set the font style and color
font_style = "Arial"
font_size = 24
font_color = "#000"  # font color
label_font = (font_style, font_size)


# Create the label to display the image
current_image = 1
my_label = Label(frame, image=image_list[current_image - 1])
my_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Create hover buttons for forward and backward
forward_button = Button(root, image=for_img, command=lambda: move_forward(move=False), font=label_font,
                        fg=font_color)
forward_button.place(x=frame_width - 55, y=frame_height / 2 - 50)
backward_button = Button(root, image=back_img, command=lambda: move_backward(move=False), font=label_font,
                         fg=font_color)
backward_button.place(x=-5, y=frame_height / 2 - 50)

# Configure hover styles and bindings
forward_button.configure(relief="flat", bd=0)
backward_button.configure(relief="flat", bd=0)

# Bind keyboard events
root.bind("<Right>", lambda event: move_forward(move=True))  # Move forward on right arrow key press
root.bind("<Left>", lambda event: move_backward(move=True))  # Move backward on left arrow key press

root.mainloop()
