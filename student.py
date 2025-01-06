import os
from tkinter import messagebox,ttk
from tkinter import*
import mysql.connector
from PIL import Image,ImageTk
import cv2
file=r'C:\Program Files\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'
class student():
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1350x740+0+0")
        self.root.title('student details')
        #varivables
        self.vardep = StringVar()
        self.varcourse = StringVar()
        self.varyear = StringVar()
        self.varsem = StringVar()
        self.varroll =StringVar()
        self.varname = StringVar()
        self.vardiv = StringVar()
        self.varemail = StringVar()
        self.varphone =StringVar()
        self.varteacher = StringVar()
        self.varc=StringVar()
        self.varselect=StringVar()
        self.varid=StringVar()
        

        #image 1
        img0=Image.open(r"C:\python attendance\tk images\student1.jpg")
        img0 = img0.resize((500, 160), Image.Resampling.LANCZOS)
        self.photoimg0=ImageTk.PhotoImage(img0)
        flbl=Label(self.root,image=self.photoimg0)
        flbl.place(x=0,y=0,width=500,height=160)
        #image2
        img1=Image.open(r"C:\python attendance\tk images\student2.jpg")
        img1 = img1.resize((500, 160), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        flbl=Label(self.root,image=self.photoimg1)
        flbl.place(x=500,y=0,width=500,height=160)
        #image3
        img2=Image.open(r"C:\python attendance\tk images\student3.webp")
        img2 = img2.resize((500, 160), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        flbl=Label(self.root,image=self.photoimg2)
        flbl.place(x=1000,y=0,width=500,height=160)
        #bg
        img3=Image.open(r"C:\python attendance\tk images\final.jpg")
        img3 = img3.resize((1320, 700), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bglb=Label(self.root,image=self.photoimg3)
        bglb.place(x=0,y=160,width=1350,height=740)
        title=Label(bglb,text="student details",font=("times new roman", 35, 'bold'), bg="white", fg="red")
        title.place(x=0,y=0,width=1350,height=45)
        #frame
        main=Frame(bglb,bd=2,bg="white")
        main.place(x=0,y=50,width=1350,height=700)
        #left
        left=LabelFrame(main,bd=2,text="STUDENT DETAILS",relief=RIDGE,font=("times new roman", 12, 'bold'),bg="white")
        left.place(x=10,y=5,width=650,height=470)
        #current
        current=LabelFrame(left,bd=2,text="STUDENT DETAILS",relief=RIDGE,font=("times new roman", 10, 'bold'),bg="white")
        current.place(x=5,y=0,width=600,height=200)
        #department
        department=Label(current,bd=2,text="DEPARTMENT",relief=RIDGE,font=("times new roman", 10, 'bold'),bg="white")
        department.grid(row=0,column=0,padx=10,pady=1)
        combobox=ttk.Combobox(current,font=("times new roman", 10, 'bold'),textvariable=self.vardep,width=17,state="readonly")
        combobox["values"]=("select department","CSE","CIVIL","ECE","MECHANICAL")
        combobox.current(0)
        combobox.grid(row=0,column=1,padx=10,pady=1)
        #course
        course=Label(current,bd=2,text="CURRENT YEAR",relief=RIDGE,font=("times new roman", 10, 'bold'),bg="white")
        course.grid(row=0,column=2,padx=10,pady=1)
        course_combo=ttk.Combobox(current,font=("times new roman", 10, 'bold'),textvariable=self.varcourse,width=17,state="readonly")
        course_combo["values"]=("select current year","1st","2nd","3rd","4th")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10,pady=1)
        #year
        year=Label(current,bd=2,text="BATCH",relief=RIDGE,font=("times new roman", 10, 'bold'),bg="white")
        year.grid(row=2,column=0,padx=5,pady=60)
        year_combo=ttk.Combobox(current,font=("times new roman", 10, 'bold'),textvariable=self.varyear,width=17,state="readonly")
        year_combo["values"]=("select year","2020-2024","2021-2025","2022-2026","2023-2027","2024-2028")
        year_combo.current(0)
        year_combo.grid(row=2,column=1,padx=1,pady=60)
        #semester
        semester=Label(current,text="SEMESTER",font=("times new roman",10,"bold"),bg="white",relief=RIDGE)
        semester.grid(row=2,column=2,padx=10,pady=60)
        semestercombo=ttk.Combobox(current,font=("times new roman",10,"bold"),textvariable=self.varsem,width=17,state="readonly")
        semestercombo["values"]=("select semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        semestercombo.current(0)
        semestercombo.grid(row=2,column=3,padx=10,pady=60)
        #student class info
        current=LabelFrame(left,bd=2,text="student class info".upper(),relief=RIDGE,font=("times new roman", 10, 'bold'),bg="white")
        current.place(x=5,y=210,width=630,height=220)
        #roll no
        idd=Label(current,bd=2,text="roll no".upper(),relief=RIDGE,font=("times new roman", 10, 'bold'),bg="white")
        idd.grid(row=0,column=0,padx=10,pady=5)
        idd_combo=ttk.Entry(current,font=("times new roman", 10, 'bold'),textvariable=self.varroll,width=17)
        idd_combo.grid(row=0,column=1,padx=10,pady=5)
        #name
        name=Label(current,bd=2,text="STUDENT NAME",relief=RIDGE,font=("times new roman", 10, 'bold'),bg="white")
        name.grid(row=0,column=2,padx=10,pady=5)
        name_combo=ttk.Entry(current,font=("times new roman", 10, 'bold'),textvariable=self.varname,width=17)
        name_combo.grid(row=0,column=3,padx=10,pady=5)
        #class division
        idd=Label(current,bd=2,text="CLASS DIVISION",relief=RIDGE,font=("times new roman", 10, 'bold'),bg="white")
        idd.grid(row=1,column=0,padx=10,pady=5)
        idd_combo=ttk.Combobox(current,font=("times new roman", 10, 'bold'),textvariable=self.vardiv,width=17,state="readonly")
        idd_combo['values']=('SELECT DIV',"A","B","C")
        idd_combo.current(0)
        idd_combo.grid(row=1,column=1,padx=10,pady=5)
        #TEACHER NAME
        roll=Label(current,bd=2,text="TEACHER NAME",relief=RIDGE,font=("times new roman", 10, 'bold'),bg="white")
        roll.grid(row=1,column=2,padx=10,pady=5)
        roll_combo=ttk.Entry(current,font=("times new roman", 10, 'bold'),textvariable=self.varteacher,width=17)
        roll_combo.grid(row=1,column=3,padx=10,pady=5)
        
        #EMAIL
        email=Label(current,bd=2,text="EMAIL",relief=RIDGE,font=("times new roman", 10, 'bold'),bg="white")
        email.grid(row=3,column=0,padx=10,pady=5)
        email_combo=ttk.Entry(current,font=("times new roman", 10, 'bold'),textvariable=self.varemail,width=17)
        email_combo.grid(row=3,column=1,padx=10,pady=5)
        #PHN NUM
        phn=Label(current,bd=2,text="PHONE NO",relief=RIDGE,font=("times new roman", 10, 'bold'),bg="white")
        phn.grid(row=3,column=2,padx=10,pady=5)
        phn_combo=ttk.Entry(current,font=("times new roman", 10, 'bold'),textvariable=self.varphone,width=17)
        phn_combo.grid(row=3,column=3,padx=10,pady=5)
        # take radioBUTTONS
        self.varradio=StringVar()
        va=self.varradio
        
        button1=ttk.Radiobutton(current,text="take photo sample".upper(),variable=self.varradio,value="Yes")
        button1.grid(row=4,column=0,padx=10,pady=5)
        #not take radio button
        button2=ttk.Radiobutton(current,text="NO photo sample".upper(),variable=self.varradio,value="No")
        button2.grid(row=4,column=1,padx=5,pady=3)
        # Save button
        b1 = Button(current, text="Save", font=("times new roman", 10, 'bold'),command=self.add_data, bg="darkblue", fg="white", width=20)
        b1.grid(row=5, column=0, padx=5, pady=5)
        # Update button
        b2 = Button(current, text="Update", font=("times new roman", 10, 'bold'),command=self.update, bg="darkblue", fg="white", width=20)
        b2.grid(row=5, column=1, padx=5, pady=5)
        # Delete button
        b3 = Button(current, text="Delete", font=("times new roman", 10, 'bold'),command=self.delete, bg="darkblue", fg="white", width=20)
        b3.grid(row=5, column=2, padx=5, pady=5)
        # Reset button
        b4 = Button(current, text="Reset", font=("times new roman", 10, 'bold'),command=self.reset, bg="darkblue", fg="white", width=20)
        b4.grid(row=5, column=3, padx=5, pady=5)
        # Take Photo Sample button
        b5 = Button(current, text="Take Photo Sample", command=self.generatedata,font=("times new roman", 10, 'bold'), bg="darkblue", fg="white", width=30)
        b5.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        #update photo sample
        b6= Button(current, text="Update Photo Sample",command=self.generatedata, font=("times new roman", 10, 'bold'), bg="darkblue", fg="white", width=30)
        b6.grid(row=6, column=1, columnspan=4, padx=5, pady=5)
        #right
        right=LabelFrame(main,bd=2,text="STUDENT DETAILS",relief=RIDGE,font=("times new roman", 12, 'bold'),bg="white")
        right.place(x=670,y=5,width=650,height=470)
        #search
        search=LabelFrame(right,text="SEARCH SYSTEM",relief=RIDGE,font=("times new roman", 12, 'bold'),bg="white")
        search.place(x=4,y=20,width=640,height=70)
        #searchby
        s=Label(search,text="search by:".upper(),font=("times new roman",8, 'bold'),fg="black")
        s.grid(row=0,column=0,padx=4)
        #more
        combobox=ttk.Combobox(search,font=("times new roman", 10, 'bold'),textvariable=self.varselect,width=17,state="readonly")
        combobox["values"]=("select".upper(),"ROLL NO",'NAME')
        combobox.current(0)
        combobox.grid(row=0,column=1,padx=4)
        c=ttk.Entry(search,font=("times new roman", 10, 'bold'),textvariable=self.varc,width=17)
        c.grid(row=0,column=2,padx=4)
        #search button
        bu=Button(search,text="search",font=("times new roman", 10, 'bold'),command=self.search,width=15,bg="darkblue",fg="white")
        bu.grid(row=0,column=3,padx=4)
        #show all
        but=Button(search,text="Show All",font=("times new roman", 10, 'bold'),width=15,bg="darkblue",fg="white")
        #
        t = LabelFrame(right, bd=2, text="STUDENT DETAILS", relief=RIDGE, font=("times new roman", 10, 'bold'), bg="white")
        t.place(x=4, y=100, width=640, height=310)

        # Scrollbars
        scrollx = ttk.Scrollbar(t, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)
        
        scrolly = ttk.Scrollbar(t, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        # Treeview
        self.student = ttk.Treeview(t, column=("dep", "course", "year", "sem", "roll", "name", "div", "teacher", "email", "phone", "photo"))
        self.student.heading("dep", text="DEPARTMENT")
        self.student.heading("course", text="COURSE")
        self.student.heading("year", text="YEAR")
        self.student.heading("sem", text="SEMESTER")
        self.student.heading("roll", text="ROLL NO")
        self.student.heading("name", text="NAME")
        self.student.heading("div", text="DIVISION")
        self.student.heading("teacher", text="TEACHER NAME")
        self.student.heading("email", text="EMAIL")
        self.student.heading("phone", text="PHONE NO")
        
        self.student["show"] = "headings"
        
        # Adjust column widths
        for col in ("dep", "course", "year", "sem", "roll", "name", "div", "teacher", "email", "phone"):
            self.student.column(col, width=100)
        
        # Add the scrollbars to the Treeview
        self.student.config(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.config(command=self.student.xview)
        scrolly.config(command=self.student.yview)

        # Pack the Treeview
        self.student.pack(fill=BOTH, expand=1)
        self.student.bind("<ButtonRelease>",self.getcursor)
        self.fetall()
    

        
#--------------------------------missing field func-----------------------------------------
    

    def add_data(self):
        if (self.vardep.get() == "select department" or self.vardiv.get() == "SELECT DIV" or not self.varradio.get() or self.varcourse.get() == "select current year" or self.varyear.get() == "select year" or self.varsem.get() == "select semester" or self.varname.get() == "" or self.varemail.get() == "" or self.varteacher.get() == "" or self.varphone.get() == "" or self.varroll.get() == "" ):
            
            messagebox.showerror('ERROR', "ALL FIELDS ARE REQUIRED", parent=self.root)
        else:
            try:
                conn= mysql.connector.connect(
                    host="localhost", user="root", password="aman", database="attendance"
                )
                cur = conn.cursor()
                query = """INSERT INTO details (dep, course, year, sem, roll, name, `div`, email, phone, teachername)
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                val = (
                    self.vardep.get(), self.varcourse.get(), self.varyear.get(), self.varsem.get(),
                    self.varroll.get(), self.varname.get(), self.vardiv.get(), self.varemail.get(),
                    self.varphone.get(), self.varteacher.get())
                cur.execute(query,val)
                conn.commit()
                self.fetall()
                conn.close()
                
            
                messagebox.showinfo('Success', 'Data stored successfully', parent=self.root)
            except Exception as e:
                
                # Display error message if something goes wrong
                messagebox.showerror("Error", f"ERROR DUE TO {e}", parent=self.root)

    def fetall(self,rows=None):
        if rows is None:
            conn= mysql.connector.connect(host="localhost", user="root", password="aman", database="attendance")
            cur = conn.cursor()
            cur.execute("select * from details")
            rows=cur.fetchall()
            cur.close()
            conn.close()
            
        if len(rows)!=0:
            self.student.delete(*self.student.get_children())
            for i in rows:
                self.student.insert('',END,values=i)
             
        conn.close()
    def getcursor(self,event=''):
        cursor=self.student.focus()
        content=self.student.item(cursor)
        data=content['values']
        if data and len(data) >= 10:
            
            self.vardep.set(data[0])
            self.varcourse.set(data[1])
            self.varyear.set(data[2])
            self.varsem.set(data[3])
            self.varroll.set(data[4])
            self.varname.set(data[5])
            self.vardiv.set(data[6])
            self.varemail.set(data[7])
            self.varphone.set(data[8])
            self.varteacher.set(data[9])
        else:
            print("Incomplete or empty data:", data)
        #--------------------update---------------------------------------
    def update(self):
        if (self.vardep.get() == "select department" or self.vardiv.get() == "SELECT DIV" or not self.varradio.get() or self.varcourse.get() == "select current year" or self.varyear.get() == "select year" or self.varsem.get() == "select semester" or self.varname.get() == "" or self.varemail.get() == "" or self.varteacher.get() == "" or self.varphone.get() == "" or self.varroll.get() == "" ):
            messagebox.showerror('ERROR', "ALL FIELDS ARE REQUIRED", parent=self.root)
            
            
        else:
            a=0
            
            try:
                update=messagebox.askyesno("Update"," Do you want to update details",parent=self.root)
                if update>0:
                    conn= mysql.connector.connect(host="localhost", user="root", password="aman", database="attendance")
                    cur = conn.cursor()
                    query = "UPDATE details SET dep=%s, course=%s, year=%s, sem=%s, roll=%s, name=%s, `div`=%s, email=%s, phone=%s, teachername=%s WHERE roll=%s"
                    val = (
                        self.vardep.get(),
                        self.varcourse.get(),
                        self.varyear.get(),
                        self.varsem.get(),
                        self.varroll.get(),
                        self.varname.get(),
                        self.vardiv.get(),
                        self.varemail.get(),
                        self.varphone.get(),
                        self.varteacher.get(),
                        self.varroll.get(),  # Assuming roll is unique
                        )
                    cur.execute(query,val)
                    conn.commit()
                    self.fetall()
                    conn.close()
                    messagebox.showinfo('updation',"DATA UPDATED SUCESSFULLY",parent=self.root)
                else:
                    if not update:
                        messagebox.showinfo("UPDATION","DATA not updated as your wish")
            except Exception as es:
                messagebox.showerror("Error", f"ERROR DUE TO {es}", parent=self.root)

    def delete(self):
        if (self.vardep.get() == "select department" or self.vardiv.get() == "SELECT DIV" or self.varcourse.get() == "select current year" or self.varyear.get() == "select year" or self.varsem.get() == "select semester" or self.varname.get() == "" or self.varemail.get() == "" or self.varteacher.get() == "" or self.varphone.get() == "" or self.varroll.get() == "" ):
            messagebox.showerror('ERROR', "ALL FIELDS ARE REQUIRED", parent=self.root)
        else:
            a=0
            try:
                delete=messagebox.askyesno("Delete"," ARE YOU SURE U WANT TO DELETE  DETAILS",parent=self.root)
                if delete>0:
                    conn= mysql.connector.connect(host="localhost", user="root", password="aman", database="attendance")
                    cur = conn.cursor()
                    qury="delete from details where roll= %s"
                    valu=(self.varroll.get(),)
                    cur.execute(qury,valu)
                    for i in range(1,104):
                        try:
                            os.remove(f"C:\\Program Files\\Python38\\attendance system\\data\\{valu[0]}.{i}.jpg")
                        except:
                            pass
                        
                else:
                    
                    if not delete:
                        return
                conn.commit()
                self.fetall()
                conn.close()
                messagebox.showinfo("DELETED",'SUCCESFULLY DATA DELETED',parent=self.root)
            except Exception as emm:
                messagebox.showerror("ERROR","DUE TO",{emm},parent=self.root)
    def reset(self):
        self.vardep.set("select department")
        self.varcourse.set("select current year")
        self.varyear.set("select year")
        self.varsem.set("select semester")
        self.varroll.set("")
        self.varname.set("")
        self.vardiv.set("")
        self.varemail.set("")
        self.varphone.set("")
        self.varteacher.set("")
        self.varradio.set("")
    #search
    def search(self):
        if self.varselect.get() == "select" or self.varc.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="aman", database="attendance"
                )
                cur = conn.cursor()

                if self.varselect.get() == "ROLL NO":
                    query = "SELECT * FROM details WHERE roll = %s"
                    val = (self.varc.get(),)
                elif self.varselect.get() == "NAME":
                    query = "SELECT * FROM details WHERE name LIKE %s"
                    val = ('%' + self.varc.get() + '%',)

                cur.execute(query, val)
                rows = cur.fetchall()
                if len(rows) > 0:
                    self.student.delete(*self.student.get_children())
                    for i in rows:
                        self.student.insert('', END, values=i)
                else:
                    messagebox.showinfo("No Data", "No record found!", parent=self.root)
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"ERROR DUE TO {e}", parent=self.root)
    # update photo sample
    def generatedata(self):

        if (self.vardep.get() == "select department" or 
            self.vardiv.get() == "SELECT DIV" or 
            not self.varradio.get() or 
            self.varcourse.get() == "select current year" or 
            self.varyear.get() == "select year" or 
            self.varsem.get() == "select semester" or 
            self.varname.get() == "" or 
            self.varemail.get() == "" or 
            self.varteacher.get() == "" or 
            self.varphone.get() == "" or 
            self.varroll.get() == ""):

            messagebox.showerror('ERROR', "ALL FIELDS ARE REQUIRED", parent=self.root)
            return  # Exit the function if validation fails

        try:
            update=messagebox.askyesno("Update"," Do you want to update details",parent=self.root)
            if update:
                conn = mysql.connector.connect(host="localhost", user="root", password="aman", database="attendance")
                cur = conn.cursor()
                cur.execute("SELECT * FROM details")
                idd=0
                roll= self.varroll.get()
                data = cur.fetchall()
                query = """UPDATE details 
                           SET dep=%s, course=%s, year=%s, sem=%s, roll=%s, name=%s, `div`=%s, email=%s, phone=%s, teachername=%s 
                           WHERE roll=%s"""
                val = (
                    self.vardep.get(),
                    self.varcourse.get(),
                    self.varyear.get(),
                    self.varsem.get(),
                    self.varroll.get(),
                    self.varname.get(),
                    self.vardiv.get(),
                    self.varemail.get(),
                    self.varphone.get(),
                    self.varteacher.get(),
                    roll
                )
                
                cur.execute(query, val)
                conn.commit()
                self.fetall()
                self.reset()
                conn.close()

                # Load Haar cascade for face detection
                face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def crop(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        facecropped = img[y:y+h, x:x+w]
                        return facecropped
                    return None

                cap = cv2.VideoCapture(0)
                imgid = 0
                while True:
                    ret, myframe = cap.read()
                    if crop(myframe) is not None:
                        imgid += 1
                        face_cropped = cv2.resize(crop(myframe), (450, 450))
                        face_cropped = cv2.cvtColor(face_cropped, cv2.COLOR_BGR2GRAY)
                        filepath = f"data/{roll}.{imgid}.jpg" 
                        
                        
                        cv2.imwrite(filepath, face_cropped)
                        cv2.putText(face_cropped, str(imgid), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face_cropped)

                    if cv2.waitKey(1) == 13 or imgid == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("RESULT", 'DATA SET COMPLETED SUCCESSFULLY')
        
        except Exception as e:
            messagebox.showerror("Error", f"ERROR DUE TO {e}", parent=self.root)

                

                
                    
                    
            
            

                
                    
                     
                        

                    

                    
                    

        

                
                
                
                
                
                
        
        
        

         
        
                
        

if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()
