import streamlit as st
from pathlib import Path
import os

st.title("📁 File & Folder CRUD Operations")

# Show files and folders
def show_items():
    p = Path(".")
    items = list(p.rglob("*"))

    st.subheader("Available Files & Folders")

    if items:
        for index, item in enumerate(items):
            st.write(f"{index + 1} - {item}")
    else:
        st.write("No files or folders found")


menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    ]
)

show_items()

# CREATE FILE
if menu == "Create File":
    st.header("Create File")

    file_name = st.text_input("Enter file name")

    content = st.text_area("Enter file content")

    if st.button("Create File"):
        p = Path(file_name)

        if p.exists():
            st.error("File already exists")
        else:
            with open(file_name, "w") as file:
                file.write(content)

            st.success("File created successfully")


# READ FILE
elif menu == "Read File":
    st.header("Read File")

    file_name = st.text_input("Enter file name")

    if st.button("Read File"):
        p = Path(file_name)

        if p.exists():
            with open(file_name, "r") as file:
                st.text(file.read())
        else:
            st.error("File does not exist")


# UPDATE FILE
elif menu == "Update File":
    st.header("Update File")

    file_name = st.text_input("Enter file name")

    update_type = st.radio(
        "Choose update type",
        ["Overwrite", "Append"]
    )

    content = st.text_area("Enter content")

    if st.button("Update File"):
        p = Path(file_name)

        if p.exists():

            if update_type == "Overwrite":
                mode = "w"
            else:
                mode = "a"

            with open(file_name, mode) as file:
                file.write(content)

            st.success("File updated successfully")

        else:
            st.error("File does not exist")


# DELETE FILE
elif menu == "Delete File":
    st.header("Delete File")

    file_name = st.text_input("Enter file name")

    if st.button("Delete File"):
        p = Path(file_name)

        if p.exists():
            os.remove(p)
            st.success("File deleted successfully")
        else:
            st.error("File does not exist")


# RENAME FILE
elif menu == "Rename File":
    st.header("Rename File")

    file_name = st.text_input("Old file name")

    new_name = st.text_input("New file name")

    if st.button("Rename File"):
        p = Path(file_name)

        if p.exists():
            p.rename(new_name)
            st.success("File renamed successfully")
        else:
            st.error("File not found")


# CREATE FOLDER
elif menu == "Create Folder":
    st.header("Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):
        p = Path(folder_name)

        if p.exists():
            st.error("Folder already exists")
        else:
            p.mkdir()
            st.success("Folder created successfully")


# DELETE FOLDER
elif menu == "Delete Folder":
    st.header("Delete Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):
        p = Path(folder_name)

        if p.exists():
            p.rmdir()
            st.success("Folder deleted successfully")
        else:
            st.error("Folder does not exist")