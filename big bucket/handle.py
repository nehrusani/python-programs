import os
import shutil

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def go(source,destination):
    shutil.copy(source,destination)

i = input("enter your file please: ")
j = input("please enter the sea path: ")
k = input("please enter your location : ")

testy = find(i, j)
go(testy, k)
