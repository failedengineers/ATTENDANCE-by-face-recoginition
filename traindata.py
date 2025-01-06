from tkinter import*
from PIL import Image,ImageTk
import numpy as np
from tkinter import messagebox,ttk,Tk
import os
import cv2




class traindata():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x740+0+0")
        self.root.title("TRAIN DATA")
        #TEXT
        head=Label(self.root,text="PHOTO SAMPLE TRAINING",font=("times new roman",35,'bold'),bg="white",fg="darkblue")
        head.place(x=0,y=0,width=1350,height=45)
        
        #IMG1
        img0=Image.open(r"C:\python attendance\tk images\train1.jpg")
        img0 = img0.resize((500, 270), Image.Resampling.LANCZOS)
        self.photoimg0=ImageTk.PhotoImage(img0)
        flbl=Label(self.root,image=self.photoimg0)
        flbl.place(x=0,y=48,width=450,height=270)
        #img2
        img1=Image.open(r"C:\python attendance\tk images\train2.jpg")
        img1 = img1.resize((500, 270), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        flbl=Label(self.root,image=self.photoimg1)
        flbl.place(x=450,y=48,width=500,height=270)
        #image3
        img2=Image.open(r"C:\python attendance\tk images\train3.jpg")
        img2 = img2.resize((500, 270), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        flbl=Label(self.root,image=self.photoimg2)
        flbl.place(x=900,y=48,width=500,height=270)
        #button
        but=Button(self.root,text="TRAIN DATA",command=self.training,font=("times new roman",35,'bold'),bg="red",fg="white")
        but.place(x=0,y=270,width=1350,height=100)
        #bglb
        img11=Image.open(r"C:\python attendance\tk images\train4.jpg")
        img11 = img11.resize((1350,400), Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        bg=Label(self.root,image=self.photoimg11)
        bg.place(x=0,y=370,width=1350,height=320)

    def training(self):
        data=(r'C:\Program Files\Python38\attendance system\data')
        path=[os.path.join(data,i)for i in os.listdir(data)]

        faces=[]
        ids=[]
        c=0
        for j in path:
            img=Image.open(j).convert("L")#CONVERT IN GAY SCALE
            imgnp=np.array(img,'uint8')
            base=os.path.basename(j)
            idd=int(base.split(".")[0])
            
            faces.append(imgnp)
            ids.append(idd)
            c += 1
            cv2.imshow("TRAIN DATA",imgnp)
            if cv2.waitKey(1)==13 or imgnp is None:
              
                break
            
                
        ids=np.array(ids)

        #-------------------traing data-----------------
        clf=cv2.face.LBPHFaceRecognizer_create()

        clf.train(faces,ids)
        clf.write("classifertraindata.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo("train data","DATA TRAINED SUCESSULLY",parent=self.root)



            
        


































if __name__=="__main__":
    root=Tk()
    obj=traindata(root)
    root.mainloop()
