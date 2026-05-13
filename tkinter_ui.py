from tkinter import *
from tkinter import messagebox
from pathlib import Path
import os

root = Tk()
root.title("CRUD Operations")
root.geometry("600x500")

# Functions

def create_file():
    file_name = entry1.get()
    content = text_area.get("1.0", END)

    p = Path(file_name)

    if p.exists():
        messagebox.showerror("Error", "File already exists")
    else:
        with open(file_name, "w") as file:
            file.write(content)

        messagebox.showinfo("Success", "File created")


def read_file():
    file_name = entry1.get()

    p = Path(file_name)

    if p.exists():
        with open(file_name, "r") as file:
            data = file.read()

        text_area.delete("1.0", END)
        text_area.insert(END, data)

    else:
        messagebox.showerror("Error", "File does not exist")


def update_file():
    file_name = entry1.get()
    content = text_area.get("1.0", END)

    p = Path(file_name)

    if p.exists():

        with open(file_name, "w") as file:
            file.write(content)

        messagebox.showinfo("Success", "File updated")

    else:
        messagebox.showerror("Error", "File does not exist")


def delete_file():
    file_name = entry1.get()

    p = Path(file_name)

    if p.exists():
        os.remove(p)

        messagebox.showinfo("Success", "File deleted")

    else:
        messagebox.showerror("Error", "File does not exist")


def rename_file():
    old_name = entry1.get()
    new_name = entry2.get()

    p = Path(old_name)

    if p.exists():
        p.rename(new_name)

        messagebox.showinfo("Success", "File renamed")

    else:
        messagebox.showerror("Error", "File not found")


def create_folder():
    folder_name = entry1.get()

    p = Path(folder_name)

    if p.exists():
        messagebox.showerror("Error", "Folder already exists")

    else:
        p.mkdir()

        messagebox.showinfo("Success", "Folder created")


def delete_folder():
    folder_name = entry1.get()

    p = Path(folder_name)

    if p.exists():
        p.rmdir()

        messagebox.showinfo("Success", "Folder deleted")

    else:
        messagebox.showerror("Error", "Folder not found")


# UI

Label(root, text="File/Folder Name").pack()

entry1 = Entry(root, width=50)
entry1.pack(pady=5)

Label(root, text="New File Name (Rename)").pack()

entry2 = Entry(root, width=50)
entry2.pack(pady=5)

Label(root, text="Content").pack()

text_area = Text(root, height=15, width=60)
text_area.pack(pady=10)

# Buttons

Button(root, text="Create File", width=20, command=create_file).pack(pady=2)

Button(root, text="Read File", width=20, command=read_file).pack(pady=2)

Button(root, text="Update File", width=20, command=update_file).pack(pady=2)

Button(root, text="Delete File", width=20, command=delete_file).pack(pady=2)

Button(root, text="Rename File", width=20, command=rename_file).pack(pady=2)

Button(root, text="Create Folder", width=20, command=create_folder).pack(pady=2)

Button(root, text="Delete Folder", width=20, command=delete_folder).pack(pady=2)

root.mainloop()