#!/usr/bin/python
from Tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initGUI()

    def initGUI(self):
        self.parent.title("Open Chrome")
        self.pack(fill=BOTH, expand=1)

        self.btn = Button(self,text="Open Chrome",
                          command=self.openChrome)
        self.btn.place(x=30,y=30)


    def openChrome(self):
        driver=webdriver.Chrome()
        driver.get("http://www.google.com")

def main():
    root = Tk()
    Wind = GUI(root)
    root.geometry("300x150+300+300")
    root.mainloop()
    
if __name__=='__main__':
    main()
