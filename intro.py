import tkinter as tk
from tkinter import PhotoImage
import subprocess
import os

def create_picture_frame(root, image_path, frame_width, frame_height, callback):
    # Load the image
    original_image = PhotoImage(file=image_path)

    # Resize the image to fit the frame size
    resized_image = original_image.subsample(
        original_image.width() // frame_width, 
        original_image.height() // frame_height
    )

    # Create a label to display the resized image
    image_label = tk.Label(root, image=resized_image, bd=10, relief="ridge")
    image_label.photo = resized_image  # Keep a reference to the image to prevent it from being garbage collected
    image_label.pack()

    # Bind the callback function to the label
    image_label.bind("<Button-1>", callback)

# Callback function to be executed when the image is clicked
def on_image_click(event):
     # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the relative path to the register.py script
    register_script_path = os.path.join(current_dir, 'loginex.py')
    
    # Open the register.py script using subprocess
    subprocess.Popen(["python", register_script_path])
    
    # Exit the current script
    exit()

# Create the main window
root = tk.Tk()
root.title("Picture Frame Example")

tk.Label(root, text="USERNAME", font=("Comic Sans MS", 10)).place(x=100, y=200)
tk.Label(root, text="PASSWORD", font=("Comic Sans MS", 10)).place(x=100, y=250)



# Specify the path to your image file
image_path = "logointro.png"

# Set the frame size
frame_width = 850
frame_height = 425

# Create the picture frame with the resized image and bind the callback
create_picture_frame(root, image_path, frame_width, frame_height, on_image_click)



# Start the Tkinter event loop
root.mainloop()
