from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import pymysql
toggle=True
class User_Login:
    def __init__(self,root):
        self.root = root
        self.root.title('Inventory Management')
        self.root.geometry("1600x800+0+0")
        title=Label(self.root,text="INVENTORY MANAGEMENT",bd=10,relief=SOLID,fg="tomato",bg="navy",font=("times new roman",40,"bold"))
        title.pack(side=TOP,fill=X)
        self.bg= ImageTk.PhotoImage(Image.open("../IMS/icons/bg.jpg"))
        bg= Label(self.root,image=self.bg)
        bg.place(x=0,y=0,relwidth=1,relheight=1)
        self.titlebg=ImageTk.PhotoImage(Image.open("../IMS/icons/title.png"))
        self.eye=ImageTk.PhotoImage(Image.open("../IMS/icons/eye.png"))
        self.user_name = StringVar()
        self.usr_pass = StringVar()
        self.usr_type = StringVar()
        self.logo= ImageTk.PhotoImage(Image.open("../IMS/icons/logo.png"))
        logo= Label(self.root,image=self.logo)
        logo.place(x=1010,y=260,width=320,height=320)
        ims= Label(self.root,image=self.titlebg)
        ims.place(x=440,y=140,width=700,height=100)
        self.login_frame = LabelFrame(self.root, text="LOGIN", bg = "white", font =("Times New Roman",22))
        self.login_frame.place(x = 240, y = 270, height = 300, width = 750)
        login_id = Label(self.login_frame, text = " Username : ",bg = "tomato", font =("Times New Roman",18)).grid(row = 0, column = 0,padx = 10, pady = 15,sticky="w")
        self.login_iden = Entry(self.login_frame, textvariable = self.user_name,bd=3,width = 45,bg = "LightGray", font =("Times New Roman",18))
        self.login_iden.grid(row = 0, column = 1,padx = 10, pady = 15,sticky="w")
        login_pass = Label(self.login_frame, text = "  Password : ",bg = "tomato", font =("Times New Roman",18)).grid(row = 1, column = 0,padx = 10, pady = 15,sticky="w")
        self.login_passen = Entry(self.login_frame,textvariable =self.usr_pass ,show="*",bd=3, width = 45,bg = "LightGray", font =("Times New Roman",18))
        self.login_passen.grid(row = 1, column = 1,padx = 10, pady = 15,sticky="w")
        self.showpw = Button(self.login_frame, image=self.eye, font =("Times New Roman",20,"bold"),bd=2,bg="lightgray", command = self.show_pw)
        self.showpw.place(x=670, y = 81, width = 33, height = 30)
        self.login_button = Button(self.login_frame,text="Login", font =("Times New Roman",20,"bold"),bd=3,bg="red2",fg="White", command = self.ureg_login)
        self.login_button.place(x=160, y = 150, width = 200, height = 50)
        self.forgot = Button(self.login_frame,text="Forgot Password?",bg="tomato",fg="Black",font =("Times New Roman",12,"bold"),bd=3, command = self.ureg_forgotpass)
        self.forgot.place(x=160, y = 210, width = 420, height = 30)
        self.register_button = Button(self.login_frame,text="Register",font =("Times New Roman",20,"bold"),bd=3,bg="red2",fg="White",command= self.register)
        self.register_button.place(x=380, y =150, width = 200, height = 50)
        
    def new_password(self):
        if self.mail.get() =="" or self.ans.get() =="" or self.password.get() =="" or self.ques.get()=="Select":
            messagebox.showerror("Error","All fields are mandatory",parent = self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",passwd="root",database="ims")
                cur =con.cursor()
                cur.execute("SELECT * FROM USERS WHERE mail_id = %s and que= %s and answer= %s",(self.mail.get(), self.ques.get(), self.ans.get()))
                rows = cur.fetchone()
                if rows == None:
                    messagebox.showerror("Error","Incorrect information!",parent = self.root2)
                else:
                    update = "UPDATE USERS SET password= %s WHERE mail_id = %s"
                    value = (self.password.get(),self.mail.get())
                    cur.execute(update,value)
                    messagebox.showinfo("Success","Password changed successfully!",parent = self.root2)
                    self.root2.destroy()

                con.commit()
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"{es}",parent = self.root2)
                self.mail.delete(0,END)
                self.ans.delete(0,END)
                self.password.delete(0,END)
    
    def show_pw(self):
        global toggle
        if toggle:
            self.login_passen.config(show="")
            toggle=False
        else:
            self.login_passen.config(show="*")
            toggle=True

    def ureg_login(self):
        if self.user_name.get() =="" or self.usr_pass.get() =="":
            messagebox.showerror("Error","All fields are mandatory",parent = self.root)
        elif self.user_name.get()=="admin@ims" and self.usr_pass.get() =="admin_ims123":
            self.root.destroy()
            import admin
            admin.run_admin(self.user_name.get())
        else:
            con = mysql.connector.connect(host="localhost",user="root",passwd="root",database="ims")
            cur = con.cursor(buffered=True)
            select = "SELECT * FROM USERS WHERE username = %s and password = %s"
            value = (self.user_name.get(),self.usr_pass.get())
            cur.execute(select,value)
            rows = cur.fetchone()
            if rows == None:
                messagebox.showerror("Error","Incorrect login details!",parent = self.root)
                self.usr_pass.set('')
                self.user_name.set('')
            else:
                self.root.destroy()
                import user
                user.run_user(self.user_name.get())
               
            con.commit()
            con.close()  
    
    def ureg_forgotpass(self):
        self.root2 = Toplevel()
        self.root2.geometry("1600x800+0+0")
        self.root2.config(bg="white")
        self.root2.focus_force()
        self.root2.grab_set()
        bgupdate= Label(self.root2,image=self.bg)
        bgupdate.place(x=0,y=0,relwidth=1,relheight=1)
        self.email_id= StringVar()
        self.question=StringVar()
        self.answer= StringVar()
        self.new_pass= StringVar()
        
        self.root2_frame = LabelFrame(self.root2, text="RECOVER PASSWORD", bg = "white", font =("Times New Roman",22))
        self.root2_frame.place(x = 400, y = 200, height = 380, width = 780)

        usrnew_id = Label(self.root2_frame, text = "         Email id       :",bg = "tomato", font =("Times New Roman",18)).grid(row = 0, column = 0,padx = 10, pady = 15,sticky="w")
        self.mail = Entry(self.root2_frame, textvariable = self.email_id,bd=3,width = 43,bg = "LightGray", font =("Times New Roman",18))
        self.mail.grid(row = 0, column = 1,padx = 10, pady = 15,sticky="w")
        security = Label(self.root2_frame, text = " Security question :",bg = "tomato", font =("Times New Roman",18)).grid(row = 1, column = 0,padx = 10, pady = 15,sticky="w")
        self.ques = ttk.Combobox(self.root2_frame,textvariable = self.question, font =("Times New Roman",18), width = 41,state = "readonly" , justify = "center")
        self.ques['values']=("Select","Your favourite book","Your favourite movie","Your best friend")
        self.ques.grid(row = 1, column = 1,padx = 10, pady = 15,sticky="w")
        self.ques.current(0)
        answer = Label(self.root2_frame, text = "        Answer         :",bg = "tomato", font =("Times New Roman",18)).grid(row = 2, column = 0,padx = 10, pady = 15,sticky="w")
        self.ans = Entry(self.root2_frame, textvariable = self.answer,bd=3,width = 43,bg = "LightGray", font =("Times New Roman",18))
        self.ans.grid(row = 2, column = 1,padx = 10, pady = 15,sticky="w")
        usrnew_pass = Label(self.root2_frame, text = "   New Password   :",bg = "tomato", font =("Times New Roman",18)).grid(row = 3, column = 0,padx = 10, pady = 15,sticky="w")
        self.password = Entry(self.root2_frame, textvariable = self.new_pass,bd=3,width = 43,bg = "LightGray", font =("Times New Roman",18))
        self.password.grid(row = 3, column = 1,padx = 10, pady = 15,sticky="w")
        self.new_pass = Button(self.root2_frame, text="Update Password",bd=3,bg="red2",fg="white",font =("Times New Roman",18, "bold"), command = self.new_password)
        self.new_pass.place(x=305, y = 280, width = 200, height = 42)
        self.back_btn = Button(self.root2, text  = "<BACK", font =("Arial",18),bd=3,bg="White",fg="Red", command= self.back)
        self.back_btn.place(x=0, y = 0, width = 150, height = 50)
          
    def back(self):
        self.root2.destroy()
        
    def register(self):
        self.root.destroy()
        import register

root = Tk()
obj = User_Login(root)
root.mainloop()
