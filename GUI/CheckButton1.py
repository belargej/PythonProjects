#!/usr/bin/python
from Tkinter import Tk, Frame, Checkbutton
from Tkinter import BooleanVar,BOTH

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("CheckButton")
        self.pack(fill=BOTH,expand=True)
        self.var = BooleanVar()
        self.var.set(False)
        
        chbt = Checkbutton(self,text="Show Title",
                           variable=self.var,command=self.onClick)
        #chbt.select()
        chbt.place(x=50,y=50)

    def onClick(self):
        if self.var.get() == True:
            self.master.title("CheckButton")
        else:
            self.master.title("NOT!!")
    
def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app=Example(root)
    root.mainloop()

if __name__=='__main__':
    main()
