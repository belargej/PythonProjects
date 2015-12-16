#!/usr/bin/python
from Tkinter import Tk, BOTH, IntVar, LEFT
from ttk import Frame, Label,Scale,Style

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Scale - Title")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH,expand=1)
        
        scale = Scale(self,from_=0, to=100,
                      command=self.onScale)
        scale.pack(side=LEFT,padx=50)

        self.var = IntVar()
        self.label = Label(self,text=0,textvariable=self.var)
        self.label.pack(side=LEFT)

    def onScale(self,val):
        v = int(float(val))
        self.var.set(v)

def main():
    foor = Tk()
    ex = Example(foor)
    foor.geometry("1000x300+0+250")
    foor.mainloop()

if __name__=='__main__':
    main()

