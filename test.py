import os

folders = input("please mention the list of folders:").split()

for folder in folders:
    try:
       files = os.listdir(folder)
    except FileNotFoundError:
       print("Provide a valid folder name")
       continue
   
    print("the files in the folder - " + folder)

    for file in files:
        print(file)