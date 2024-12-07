import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
import customtkinter as ctk
import subprocess

def GetValue(event):
    e1.delete("1.0", END)
    e2.delete("1.0", END)
    e3.delete("1.0", END)
    e4.delete("1.0", END)

    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    
    e1.insert("1.0", str(select['SHOE_NUMBER']))
    e2.insert("1.0", select['SHOE_NAME'])
    e3.insert("1.0", select['SHOE_SIZE'])
    e4.insert("1.0", str(select['QUANTITY']))



def Add():
    SHOE_NUMBER = e1.get("1.0", "end-1c")  # Get text from the Text widget
    SHOE_NAME = e2.get("1.0", "end-1c")
    SHOE_SIZE = e3.get("1.0", "end-1c")
    QUANTITY = e4.get("1.0", "end-1c")

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="theshoekeepers")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO  record (SHOE_NUMBER,SHOE_NAME,SHOE_SIZE,QUANTITY) VALUES (%s, %s, %s, %s)"
       val = ( SHOE_NUMBER, SHOE_NAME, SHOE_SIZE, QUANTITY)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Shoe info inserted successfully...")
       e1.delete(1.0, END)
       e2.delete(1.0, END)
       e3.delete(1.0, END)
       e4.delete(1.0, END)
       e1.focus_set()


    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

    finally:
         listBox.delete(*listBox.get_children())
         show()

def update():
    SHOE_NUMBER = e1.get("1.0", "end-1c")  # Get text from the Text widget
    SHOE_NAME = e2.get("1.0", "end-1c")
    SHOE_SIZE = e3.get("1.0", "end-1c")
    QUANTITY = e4.get("1.0", "end-1c")

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="theshoekeepers")
    mycursor = mysqldb.cursor()

    try:
        sql = "UPDATE record SET SHOE_NAME=%s, SHOE_SIZE=%s, QUANTITY=%s WHERE SHOE_NUMBER=%s"
        val = ( SHOE_NUMBER, SHOE_NAME, SHOE_SIZE, QUANTITY)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Updated successfully...")

        # Correct the index to "1.0" for Text widgets
        e1.delete("1.0", END)
        e2.delete("1.0", END)
        e3.delete("1.0", END)
        e4.delete("1.0", END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
    finally:
        listBox.delete(*listBox.get_children())
        show()

def delete():
    SHOE_NUMBER = e1.get("1.0", "end-1c")

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="theshoekeepers")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from record where SHOE_NUMBER = %s"
        val = (SHOE_NUMBER,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleteeeee successfully...")

        # Clear the Text widgets
        e1.delete("1.0", END)
        e2.delete("1.0", END)
        e3.delete("1.0", END)
        e4.delete("1.0", END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
    finally:
        listBox.delete(*listBox.get_children())
        show()


def show():
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="theshoekeepers")
        mycursor=mysqldb.cursor()
        mycursor.execute("SELECT SHOE_NUMBER,SHOE_NAME,SHOE_SIZE,QUANTITY FROM record")
        records = mycursor.fetchall()
        print(records)

        for i, ( SHOE_NUMBER, SHOE_NAME, SHOE_SIZE, QUANTITY) in enumerate(records, start=1):
            listBox.insert("", "end", values=( SHOE_NUMBER, SHOE_NAME, SHOE_SIZE, QUANTITY))
            mysqldb.close()

def clear_text():
    e1.delete("1.0", END)
    e2.delete("1.0", END)
    e3.delete("1.0", END)
    e4.delete("1.0", END)



def log_out():
    root.destroy()  # Close the current window
    subprocess.run(["python", "intro.py"])  # Run intro.py
            

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

global e1
global e2
global e3
global e4

tk.Label(root, text="THE SHOE KEEPERS", fg="black", bg="#e6e6fa", font=("Comic Sans MS", 30)).place(x=250, y=20)
Button(root, text="Log out", command=log_out, bg="#e6e6fa", font=("Comic Sans MS", 10), width=10).place(x=750, y=20)


Button(root, text="Clear", command=clear_text, bg="#e6e6fa", font=("Comic Sans MS", 10), width=10).place(x=10, y=50)
tk.Label(root, text="SHOE NUMBER", bg="#e6e6fa",font=("Comic Sans MS", 10)).place(x=10, y=100)
Label(root, text="SHOE NAME", bg="#e6e6fa",font=("Comic Sans MS", 10)).place(x=10, y=150)
Label(root, text="SHOE_SIZE", bg="#e6e6fa",font=("Comic Sans MS", 10)).place(x=10, y=200)
Label(root, text="QUANTITY", bg="#e6e6fa",font=("Comic Sans MS", 10)).place(x=10, y=250)

e1 = Text(root, height=2, width=20)  
e1.place(x=115, y=100)

e2 = Text(root, height=2, width=20)  
e2.place(x=115, y=150)

e3 = Text(root, height=2, width=20)  
e3.place(x=115, y=200)

e4 = Text(root, height=2, width=20)  
e4.place(x=115, y=250)


add_image = PhotoImage(file="add.png").subsample(3)  # Adjust the subsample factor as needed
update_image = PhotoImage(file="update.png").subsample(3)
delete_image = PhotoImage(file="delete.png").subsample(3)

# Create buttons with images
Button(root,bg="#e6e6fa", command=Add, image=add_image, compound="top", height=150, width=150).place(x=300, y=100)
Button(root,bg="#e6e6fa", command=update, image=update_image, compound="top", height=150, width=150).place(x=470, y=100)
Button(root,bg="#e6e6fa", command=delete, image=delete_image, compound="top", height=150, width=150).place(x= 640, y=100)

cols = ('SHOE_NUMBER', 'SHOE_NAME', 'SHOE_SIZE','QUANTITY')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

font1=("Comic Sans MS", 15)

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=20, y=300)

show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()