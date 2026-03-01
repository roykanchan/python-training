import os

folders = input("please mention the list of folders:").split()

for folder in folders:
    files = os.listdir(folder)
    print("the files in the foles are")

    for file in files:
        print(file)