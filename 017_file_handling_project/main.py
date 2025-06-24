from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting the file")

check = int(input("please tell your response: "))

def createFile():
    try:
        readfileandfolder()
        name = input("please tell your file name:- ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("what you want to write in this file: ")
                fs.write(data)
    
            print(f"FILE CREATED SUCCESSFULLY")
        else:
            print("This false already exist")
    except Exception as err:
        print(f"An error occurred as {err}")


def readFile():
    try:
        readfileandfolder()
        name = input("which file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            
            print("Readed successfully!")
        else:
            print("the file doesnot exist")
    except Exception as err:
        print("An error occured as ", err)

def updateFile():
    try:
        readfileandfolder()
        name = input("Enter the file which file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file")
            print("press 2 for overwriting the data in your file")
            print("press 3 for appending some content of the file.")

            res = int(input("tell your response: "))

            if res == 1:
                name2 = input("Tell new name for file: ")
                p2 = Path(name2)
                p.rename(p2)
            
            if res == 2:
                with open(p, 'w') as fs:
                    data = input("Tell what you want to write, this will overwrite the data: ")
                    fs.write(data)
            
            if res == 3:
                with open(p, 'w') as fs:
                    data = input("Tell what you want to append: ")
                    fs.write(" " + data)
    except Exception as err:
        print("An error occured as ", err)


def deleteFile():
    try:
        readfileandfolder()
        name = input("Enter the name of file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)

            print("filr removed successfully")
        else:
            print("No such file exists")
    except Exception as err:
        print("An error occured as ", err)




if check == 1:
    createFile()

if check == 2:
    readFile()

if check == 3:
    updateFile()

if check == 4:
    deleteFile()