#!/usr/bin/python
from Tkinter import *
bkg = Tk()

list1 = 'Joe Brit Lincoln Newbie'.split()
list2 = 'Sam Crissi DP Cathy Tommy Bean Catherine Billy'.split()
list2b = Listbox(bkg)
list1b = Listbox(bkg)
for item in list1:
    list1b.insert(0,item)

for item in list2:
    list2b.insert(0,item)

list1b.pack()
list2b.pack()
bkg.mainloop()
