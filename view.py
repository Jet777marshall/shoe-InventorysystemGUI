import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
import customtkinter as ctk


def show():
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="theshoekeepers")
        mycursor=mysqldb.cursor()
        mycursor.execute("SELECT SHOE_NUMBER,SHOE_NAME,SHOE_SIZE,QUANTITY FROM record")
        records = mycursor.fetchall()
        print(records)

        for i, (id,stname, course,fee) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id, stname, course, fee))
            mysqldb.close()

root = Tk()
root.geometry("850x550")


# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 850
window_height = 550
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

frame = Frame(root, bg="#9c96b0")
frame.place(relwidth=1, relheight=1)


frame = Frame(root, bg="#9c96b0")
frame.place(relwidth=1, relheight=1)



cols = ('SHOE_NUMBER', 'SHOE_NAME', 'SHOE_SIZE','QUANTITY')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

font1=("Comic Sans MS", 15)

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=20, y=300)

show()

root.mainloop()