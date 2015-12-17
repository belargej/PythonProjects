#!/usr/bin/python
from Tkinter import Tk, BOTH
from ttk import Frame, Button
import tkMessageBox as mbox #**

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initUI()

    def initUI(self):
        self.parent.title("Message Boxes")
        self.pack()
        
        error = Button(self,text="ERROR",command=self.onError)
        error.grid(padx=5,pady=5)
        warning = Button(self,text="Warning",command=self.onWarn)
        warning.grid(padx=5,pady=5)
        quest = Button(self,text="Question",command=self.onQuest)
        quest.grid(padx=5,pady=5)
        inform = Button(self,text="Information",command=self.onInfo)
        inform.grid(padx=5,pady=5)

    def onError(self):
        mbox.showerror("Error", "Could not open file.")

    def onWarn(self):
        mbox.showwarning("Warning","Deprecated function call.")

    def onQuest(self):
        mbox.askquestion("Question","Are you quitting?")

    def onInfo(self):
        mbox.showinfo("Information","Download completed, I guess")

def main():
    root = Tk()
    ex = Example(root)
    root.geometry("300x300+150+150")
    root.mainloop()

if __name__=='__main__':
    main()
