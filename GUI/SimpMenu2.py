#!/usr/bin/python
from Tkinter import *

class Menu2(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initGUI()

    def initGUI(self):
        self.parent.title("Submenu exercise")
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        subMenu = Menu(fileMenu)
        subMenu.add_command(label="Say Hello",command=self.sayHi)
        subMenu.add_command(label="Say Whats up",command=self.sayWU)
        subMenu.add_command(label="Say Bye",command=self.sayBye)
        fileMenu.add_cascade(label="Sayings",menu=subMenu,underline=0)
        
        fileMenu.add_separator()
        
        fileMenu.add_command(label="Exit",underline=0,command=self.onExit)
        menubar.add_cascade(label="File",underline=0,menu=fileMenu)

    def sayHi(self):
        print("Hi!")
    def sayWU(self):
        print("Nope, get out of here")
    def sayBye(self):
        print("Good Riddance")
    def onExit(self):
        self.sayBye()
        self.quit()

def main():

    root = Tk()
    root.geometry("150x150+50+50")
    ex=Menu2(root)
    root.mainloop()

if __name__=='__main__':
    main()


        
        
