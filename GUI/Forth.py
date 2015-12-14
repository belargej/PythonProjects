#!/usr/bin/python
from Tkinter import *
from random import *

def Rand1_10():
    ran=uniform(1,10)
    print ran

def GoWork():
    sum=3*5
    print sum

window = Tk()

butt = Button(window,text='Random',command=Rand1_10)
butt2 = Button(window,text='Sum',command=GoWork)

butt.pack()
butt2.pack()
window.mainloop()

