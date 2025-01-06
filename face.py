from tkinter import*
from tkinter import Tk
from PIL import Image,ImageTk
from student import student
from developer import dev
from traindata import traindata
from helpdesk import contact
from detector import detector
from attendancerecorded import recorddone

import os
import sys

import time






class facerecogination():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x740+0+0")
        self.root.title('FACE RECOGINATION ATTENDACE SYSTEM')
        #image 1
        img0=Image.open(r"C:\python attendance\tk images\biometric-face-recognition-system-500x500.webp")
        img0 = img0.resize((500, 160), Image.Resampling.LANCZOS)
        self.photoimg0=ImageTk.PhotoImage(img0)
        flbl=Label(self.root,image=self.photoimg0)
        flbl.place(x=0,y=0,width=500,height=160)
        #image2
        img1=Image.open(r"C:\python attendance\tk images\blog-–-462-1.webp")
        img1 = img1.resize((500, 160), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        flbl=Label(self.root,image=self.photoimg1)
        flbl.place(x=500,y=0,width=500,height=160)
        #image3
        img2=Image.open(r"C:\python attendance\tk images\images.jfif")
        img2 = img2.resize((500, 160), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        flbl=Label(self.root,image=self.photoimg2)
        flbl.place(x=1000,y=0,width=500,height=160)
        #image4
        img3=Image.open(r"C:\python attendance\tk images\final.jpg")
        img3 = img3.resize((1350, 740), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bgbl=Label(self.root,image=self.photoimg3)
        bgbl.place(x=0,y=160,width=1350,height=740)

        title=Label(bgbl,text="FACE RECOGINITION ATTENDANCE SYSTEM",font=("times new roman",35,'bold'),bg="white",fg="red")
        title.place(x=0,y=0,width=1350,height=40)
        # Student button
        img4 = Image.open(r"C:\python attendance\tk images\final.jpg")
        img4 = img4.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1= Button(bgbl,command=self.studentbutton ,image=self.photoimg4, cursor="hand2")
        b1.place(x=150, y=90, width=150, height=150)
        text = Button(bgbl, text="Students Details".upper(), font=("times new roman", 10, 'bold'),command=self.studentbutton,bg="darkblue", fg="white")
        text.place(x=150, y=240, width=150, height=40)
        # Face button
        img5 = Image.open(r"C:\python attendance\tk images\student.jpg")
        img5 = img5.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2= Button(bgbl, image=self.photoimg5,command=self.fc, cursor="hand2")
        b2.place(x=400, y=90, width=150, height=150)
        text2 = Button(bgbl, text="Face Recognition".upper(), font=("times new roman", 10, 'bold'),command=self.fc, bg="darkblue", fg="white")
        text2.place(x=400, y=240, width=150, height=40)
        #attendace button
        img6=Image.open(r"C:\python attendance\tk images\attendanceimg.webp")
        img6=img6.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b3=Button(bgbl,image=self.photoimg6,cursor="hand2",command=self.rec)
        b3.place(x=650,y=90,width=150,height=150)
        text3=Button(bgbl,text="ATTENDANCE",font=("times new roman",10,"bold"),bg="darkblue",fg="white",command=self.rec)
        text3.place(x=650,y=240,width=150,height=40)
        #help desk button
        img7=Image.open(r"C:\python attendance\tk images\HELP.jfif")
        img7=img7.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b4=Button(bgbl,image=self.photoimg7,cursor="hand2",command=self.helpdesk)
        b4.place(x=900,y=90,width=150,height=150)
        text4=Button(bgbl,text="HELPDESK",command=self.helpdesk,font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        text4.place(x=900,y=240,width=150,height=40)
        #train data button
        img8=Image.open(r"C:\python attendance\tk images\train data.png")
        img8=img8.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b5=Button(bgbl,image=self.photoimg8,command=self.data,cursor="hand2")
        b5.place(x=150,y=300,width=150,height=150)
        text5=Button(bgbl,text="TRAIN DATA",cursor='hand2',command=self.data,font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        text5.place(x=150,y=450,width=150,height=40)
        #GALLERY
        img9=Image.open(r"C:\python attendance\tk images\photos.jpg")
        img9=img9.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b6=Button(bgbl,image=self.photoimg9,cursor="hand2",command=self.photos)
        b6.place(x=400,y=300,width=150,height=150)
        text6=Button(bgbl,text="PHOTOS",command=self.photos,cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        text6.place(x=400,y=450,width=150,height=40)
        #DEVELOPER BUTTON
        img10=Image.open(r"C:\python attendance\tk images\logo.webp")
        img10=img10.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b7=Button(bgbl,image=self.photoimg10,cursor="hand2",command=self.developerbutton)
        
        b7.place(x=650,y=300,width=150,height=150)
        text7=Button(bgbl,text="DEVELOPER INFO",cursor="hand2",font=("times new roman",10,"bold"),command=self.developerbutton,bg="darkblue",fg="white")
        text7.place(x=650,y=450,width=150,height=40)
        #exit
        img11=Image.open(r"C:\python attendance\tk images\EXIT.png")
        img11=img11.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b8=Button(bgbl,image=self.photoimg11,command=self.exit,cursor="hand2")
        b8.place(x=900,y=300,width=150,height=150)
        text8=Button(bgbl,text="EXIT",font=("times new roman",10,"bold"),cursor="hand2",command=self.exit,bg="darkblue",fg="white")
        text8.place(x=900,y=450,width=150,height=40)
        #exit


#------------------------function buttons0-----------------------------------------
    def studentbutton(self):
        self.working=Toplevel(self.root)
        self.s=student(self.working)
    def developerbutton(self):
        self.m=Toplevel(self.root)
        self.a=dev(self.m)
    def photos(self):
        os.startfile(r"C:\Program Files\Python38\attendance system\data")
    def data(self):
        self.d=Toplevel(self.root)
        self.m=traindata(self.d)

    def exit(self):
        time.sleep(1)
        exit()
    def helpdesk(self):
        self.ll=Toplevel(self.root)
        self.nb=contact(self.ll)
    def fc(self):
        self.fc=Toplevel(self.root)
        self.m=detector(self.fc)

    def rec(self):
        self.ll=Toplevel(self.root)
        self.k=recorddone(self.ll)
        


        
        
        
        
            
        
        
     



if __name__=="__main__":
    root=Tk()
    obj=facerecogination(root)
    root.mainloop()
