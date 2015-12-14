#!/usr/bin/python
from Tkinter import *

def DrawList():
    plist = ['Liz','Tom','Tina','Bill','Mike']
    for item in plist:
        listb1.insert(END,item);

root = Tk()

listb1 = Listbox(root)
button = Button(root,text='Press it',command=DrawList)

button.pack()
listb1.pack()
root.mainloop()
