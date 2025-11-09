from tkinter import *

root = Tk()
root.title('Number pad')
root.geometry('250x300')

nums = [[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]

for r,row in enumerate(nums):
    for c,n in enumerate(row):
        Label(root,text=n,bg="#F90000",relief=SUNKEN,borderwidth=1).grid(row=r,column=c,sticky="nsew")
for i in range(3):root.columnconfigure(i,weight=1)
for i in range(4):root.rowconfigure(i,weight = 1)       

root.mainloop()
