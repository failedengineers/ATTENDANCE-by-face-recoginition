from tkinter import*
from tkinter import Tk
from PIL import Image,ImageTk
from student import student
from developer import dev
from traindata import traindata
import os
import sys

import time






class contact():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x740+0+0")
        self.root.title('HELPDESK')
        #image 1
        img0=Image.open(r"C:\python attendance\tk images\desk.webp")
        img0 = img0.resize((1350, 740), Image.Resampling.LANCZOS)
        self.photoimg0=ImageTk.PhotoImage(img0)
        flbl=Label(self.root,image=self.photoimg0)
        flbl.place(x=0,y=0,width=1350,height=740)
        #contact
        text5=Label(flbl,text="CONTACT US AT ",cursor='hand2',font=("times new roman",10,"bold"),bg="orange",fg="white")
        text5.place(x=0,y=220,width=1350,height=100)
        text6=Label(flbl,text="@GULATISOLUTION05@GMAIL.COM",cursor='hand2',font=("times new roman",10,"bold"),bg="green",fg="white")
        text6.place(x=0,y=330,width=1350,height=100)
        text7=Label(flbl,text="@FOR ANY WORK RELATED QUERIES",cursor='hand2',font=("times new roman",10,"bold"),bg="red",fg="white")
        text7.place(x=0,y=440,width=1350,height=100)


if __name__=="__main__":
    root=Tk()
    obj=contact(root)
    root.mainloop()
