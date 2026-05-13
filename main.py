# Project - CURD Operations
from pathlib import Path
def readfileandfolder():

    p = Path("")
    items = list(p.rglob("*"))
    for index, file in enumerate(items):
        print(f"{index + 1} - {file}")

def create_file():
    readfileandfolder()
    file_name = input("enter name of your file : ")
    p = Path(file_name)
    if p.exists():
        print("File already exists")
    else:
        with open (file_name, 'w') as file:
            content = input("enter your file content: ")
            file.write(content)
            print("File Added ! ")  


def read_file():
    readfileandfolder()
    file_name = input("Enter name of your file:")
    p = Path(file_name)
    if p.exists():
        with open(file_name , "r") as file:
            print(file.read())



# 3 updating a file .
def update_file():
    try:
        readfileandfolder()
        file_name = input("enter name of your file: ")
        p = Path(file_name)
        if p.exists():
            print("press 1 to overwrite the content ")
            print("press 2 to append new content ")

            option = int (input("Enter your choice for updating a file:"))
            if option == 1:
                with open(file_name, 'w') as file:
                    content = input(" Enter your content: ")
                    file.write(content)
                    print("CONTENT CHANGED.....")
                         

            elif option == 2:
                with open(file_name,"a") as file:
                    content = input ("enter your content: ")
                    file.write(content)
                    print("CONTENT CHANGED.....")
            else:
                print("INVALID INPUT")
        else:
            print("file does not exists")
    except Exception as e:
        print(e)
            
# 4. file delete
def delete_file():
    readfileandfolder()
    file_name = input("Enter name of your file:")
    p = Path(file_name)
    if p.exists():
        os.remove(p) # os is removing path of that file completely from the system.
        print("File Deleted")
    else:
        print("file does not exists")

#5. Rename file
def rename_file():
    readfileandfolder()
    file_name = input ("enter name of your file :  ")
    p = Path(file_name)
    if p.exists():
        new_file = input("enter new name for your file: ")
        p.rename(new_file)
        print("File Renamed!")
    else:
        print("File Not Found!")

# 6. Create a folder
def create_folder():
    readfileandfolder()
    folder_name = input("Enter name of your folder :  ")
    p = Path(folder_name)
    if p.exists():
        print("Folder Already exists! ")
    else:
        p.mkdir()
        print("Folder created!")

# 7. delete  a folder
def delete_folder():
    readfileandfolder()
    folder_name = input("Enter name of your folder :  ")
    p = Path(folder_name)
    if p.exists():
        p.rmdir()
        print("Folder Already exists! ")
    else:
        
        print("Folder does not exists!")



while True:
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deleting a file")
    print("Press 5 for renaming a file")
    print("Press 6 for creating a folder")
    print("Press 7 for deleting a folder")
    print("Press 0 for breaking a loop")

    option = int(input("enter your choice :  "))
    if option == 1:
        create_file()
    if option == 2:
        read_file()
    if option == 3:
        update_file()
    if option == 4:
        delete_file() 
    if option == 5:
        rename_file()
    if option == 6:
        create_folder()
    if option == 7:
        delete_folder()
    if option == 0:
        break