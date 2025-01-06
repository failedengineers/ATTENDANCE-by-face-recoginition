from tkinter import*
from tkinter import Tk
from PIL import Image,ImageTk
from PIL import Image,ImageTk
from tkinter import messagebox,ttk,Tk
import cv2
import mysql.connector
import csv


class detector():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x740+0+0")
        self.root.title('FACE DETECTOR')
        #image 1
        img0=Image.open(r"C:\python attendance\tk images\detector.jpg")
        img0 = img0.resize((675, 740), Image.Resampling.LANCZOS)
        self.photoimg0=ImageTk.PhotoImage(img0)
        flbl=Label(self.root,image=self.photoimg0)
        flbl.place(x=675,y=0,width=675,height=740)

        #image 2
        img1=Image.open(r"C:\python attendance\tk images\dect.jpg")
        img1 = img1.resize((675, 740), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        flbl=Label(self.root,image=self.photoimg1)
        flbl.place(x=0,y=0,width=675,height=740)
        up=Button(self.root,text="FACE DETECTOR",font=("times new roman",36,'bold'),bg="white",fg="red",command=self.det)
        up.place(x=0,y=350,width=1350,height=70)
        do=Button(self.root,text="BACK",font=("times new roman",15,'bold'),bg="white",fg="blue",command=self.back)
        do.place(x=1240,y=40,width=100,height=40)
    #--------------------------------------------attendance by face recoginition---------------------------------
    def back(self):
        self.root.destroy()
        
    def det(self):
        def draw_bound(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                idd,predict=clf.predict(gray[y:y+h,x:x+w])
                confidence=int(100*(1-predict/300))
                conn= mysql.connector.connect(host="localhost", user="root", password="aman", database="attendance")
                cur = conn.cursor()
                cur.execute("select name from details where roll="+str(idd))
                n=cur.fetchone()
                n = n[0] if n else None

                cur.execute("select dep from details where roll="+str(idd))
                d=cur.fetchone()
                d = d[0] if n else None
                

                
                    
                
                
                cur.execute("select roll from details where roll="+str(idd))
                r=cur.fetchone()
                r= r[0] if n else None

                if confidence>77 and n and d and r:
                    cv2.putText(img,f"ROLL {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"DEP {d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"NAME {n}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"UNKNOWN FACE",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            return coord
            #--------------------------------------------attendance by face recoginition---------------------------------
       

            
        def recog(img,clf,faceCascade):
            
            coord=draw_bound(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        facecasade=cv2.CascadeClassifier(r'C:\Program Files\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r'C:\Program Files\Python38\attendance system\classifertraindata.xml')

        video=cv2.VideoCapture(0)
        while True:
            ret,img=video.read()
            img=recog(img,clf,facecasade)
            cv2.imshow("FACE RECOGINITION",img)
            if cv2.waitKey(1)==13:
                 break
        video.release()
        cv2.destroyAllWindows()

                    
                    


        
    


        

if __name__=="__main__":
    root=Tk()
    obj=detector(root)
    root.mainloop()
