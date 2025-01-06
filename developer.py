from tkinter import*
from tkinter import Tk
from PIL import Image,ImageTk

class dev():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x740+0+0")
        self.root.title('HELPDESK')
        #image bg
        img3=Image.open(r"C:\python attendance\tk images\logo.webp")
        img3 = img3.resize((1320, 700), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bglb=Label(self.root,image=self.photoimg3)
        bglb.place(x=0,y=0,width=1350,height=740)
        title=Label(bglb,text="HI MY NAME IS KALASH!!!",font=("times new roman", 35, 'bold'), bg="white", fg="darkviolet")
        title.place(x=0,y=200,width=1350,height=45)
        header=Label(bglb,text="CONTACT ME AT @gulatikalash05@gmail.com , @THESANSKARIIGULATII",font=("times new roman", 25, 'bold'), bg="white", fg="red")
        header.place(x=0,y=300,width=1350,height=45)
        final=Label(bglb,text=" FOR WORK RELATED QUERIES",font=("times new roman", 35, 'bold'), bg="white", fg="yellow")
        final.place(x=0,y=400,width=1350,height=45)



if __name__=="__main__":
    root=Tk()
    obj=dev(root)
    root.mainloop()
