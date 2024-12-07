import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import subprocess
import os

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="theshoekeepers"
)
cursor = db.cursor()

def register(username, password, email):
    query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
    values = (username, password, email)

    try:
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Registration successful!")
    except mysql.connector.Error as err:
        messagebox.showwarning("Error", f"Error during registration: {err}")

def back():
     # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the relative path to the register.py script
    register_script_path = os.path.join(current_dir, 'loginex.py')
    
    # Open the register.py script using subprocess
    subprocess.Popen(["python", register_script_path])
    
    # Exit the current script
    exit()


def on_register_click():
    username = entry_username.get()
    password = entry_password.get()
    email = emails.get()

    if username and password:
        register(username, password, email)
    else:
        messagebox.showwarning("Error", "Please enter a username and password.")

# Create the main window
window = tk.Tk()
window.title("Login System")

# Set the frame size
frame_width = 650
frame_height = 400

# Load the background image
bg_image = Image.open("BGIT6.png")

# Resize the background image to fit the frame
bg_image = bg_image.resize((frame_width, frame_height), Image.LANCZOS)


# Convert the resized image to PhotoImage
bg_image = ImageTk.PhotoImage(bg_image)

# Create a canvas widget to add the resized background image
canvas = tk.Canvas(window, width=frame_width, height=frame_height)
canvas.pack()

# Place the resized image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

# Create labels, entry widgets, and buttons
tk.Label(window, text="Email", font=("Comic Sans MS", 10)).place(x=350, y=50)
tk.Label(window, text="Username", font=("Comic Sans MS", 10)).place(x=350, y=100)
tk.Label(window, text="Password", font=("Comic Sans MS", 10)).place(x=350, y=150)

emails = tk.Entry(window, font=("Comic Sans MS", 10))
emails.place(x=440, y=50)

entry_username = tk.Entry(window, font=("Comic Sans MS", 10))
entry_username.place(x=440, y=100)

entry_password = tk.Entry(window, show="*", font=("Comic Sans MS", 10))
entry_password.place(x=440, y=150)

tk.Button(window, text="Register", font=("Comic Sans MS", 10), bg="#e6e6fa", command=on_register_click, compound="top", height=1, width=8).place(x=520, y=250)
tk.Button(window, text="Go Back", font=("Comic Sans MS", 10), bg="#e6e6fa", command=back, compound="top", height=1, width=8).place(x=440, y=250)
# Calculate the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width - frame_width) // 2
y = (screen_height - frame_height) // 2

# Set the geometry of the window
window.geometry(f"{frame_width}x{frame_height}+{x}+{y}")

# Start the Tkinter event loop
window.mainloop()
