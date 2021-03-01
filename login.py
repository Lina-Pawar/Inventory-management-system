from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import pymysql

class User_Login:
    def __init__(self,root):
        self.root = root
        self.root.title('Inventory Management')
        self.root.geometry("1600x800+0+0")
        title=Label(self.root,text="INVENTORY MANAGEMENT",bd=10,relief=SOLID,fg="tomato",bg="navy",font=("times new roman",40,"bold"))
        title.pack(side=TOP,fill=X)
        
        self.bg= ImageTk.PhotoImage(Image.open("../IMS/icons/bglogin.jpg"))
        bg= Label(self.root,image=self.bg)
        bg.place(x=0,y=0,relwidth=1,relheight=1)
        self.login_b=ImageTk.PhotoImage(Image.open("../IMS/icons/button_login.png"))
        self.regs_b=ImageTk.PhotoImage(Image.open("../IMS/icons/button_register.png"))
        self.pass_b=ImageTk.PhotoImage(Image.open("../IMS/icons/button_forgot_password.png"))
        self.titlebg=ImageTk.PhotoImage(Image.open("../IMS/icons/title.png"))
        self.passbg=ImageTk.PhotoImage(Image.open("../IMS/icons/bgpass.png"))
        self.user_name = StringVar()
        self.usr_pass = StringVar()
        self.usr_type = StringVar()
        self.logo= ImageTk.PhotoImage(Image.open("../IMS/icons/logo.jpg"))
        logo= Label(self.root,image=self.logo)
        logo.place(x=400,y=130,width=100,height=100)
        ims= Label(self.root,text="Inventory Management System",font =("Times New Roman",35),image=self.titlebg)
        ims.place(x=520,y=130,width=680,height=100)
        self.login_frame = LabelFrame(self.root, text="LOGIN", bg = "white", font =("Times New Roman",22))
        self.login_frame.place(x = 400, y = 260, height = 350, width = 780)
        
        login_type = Label(self.login_frame, text = "   Login as : ",bg = "tomato", font =("Times New Roman",18)).grid(row = 0, column = 0,padx = 10, pady = 15,sticky="w")

        self.login_as = ttk.Combobox(self.login_frame,textvariable = self.usr_type, font =("Times New Roman",18), width = 47,state = "readonly" , justify = "center")
        self.login_as['values']=("User","Admin")
        self.login_as.grid(row = 0, column = 1,padx = 10, pady = 15,sticky="w")
        self.login_as.current(0)

        login_id = Label(self.login_frame, text = " Username : ",bg = "tomato", font =("Times New Roman",18)).grid(row = 1, column = 0,padx = 10, pady = 15,sticky="w")

        self.login_iden = Entry(self.login_frame, textvariable = self.user_name,bd="3",width = 48,bg = "LightGray", font =("Times New Roman",18))
        self.login_iden.grid(row = 1, column = 1,padx = 10, pady = 15,sticky="w")

        login_pass = Label(self.login_frame, text = "  Password : ",bg = "tomato", font =("Times New Roman",18)).grid(row = 2, column = 0,padx = 10, pady = 15,sticky="w")

        self.login_passen = Entry(self.login_frame,textvariable =self.usr_pass ,show="*",bd="3", width = 48,bg = "LightGray", font =("Times New Roman",18))
        self.login_passen.grid(row = 2, column = 1,padx = 10, pady = 15,sticky="w")

        self.login_button = Button(self.login_frame, image=self.login_b, font =("Impact",14),bd=3,bg="red2", command = self.ureg_login)
        self.login_button.place(x=305, y = 230, width = 200, height = 50)

        self.forgot = Button(self.login_frame,image=self.pass_b,bg="tomato",fg="Blue",font =("Ar Delaney",16),bd=3, command = self.ureg_forgotpass)
        self.forgot.place(x=50, y = 230, width = 230, height = 50)

        self.register_button = Button(self.login_frame,image=self.regs_b, font =("Colonna MT",13),bd=3,bg="red2",fg="Blue", command= self.register)
        self.register_button.place(x=530, y =230, width = 200, height = 50)

    def new_password(self):
        if self.usrnew_iden.get() =="" or self.answeren.get() =="" or self.usrnew_passen.get() =="" or self.security_combo.get()=="Select":
            messagebox.showerror("Error","All fields are mandatory",parent = self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",passwd="root",database="ims")
                cur =con.cursor()
                cur.execute("SELECT * FROM USERS WHERE mail_id = %s",self.usrnew_iden.get())
                rows = cur.fetchall()
                if rows == NONE:
                    messagebox.showerror("Error","Invalid Credentials",parent = self.root)
                else:
                    update = "UPDATE USERS SET password=%s WHERE mail_id = %s  "
                    value = (self.usrnew_passen.get(),self.usrnew_iden.get())
                    cur.execute(update,value)
                    messagebox.showinfo("Success","Password changed successfully!",parent = self.root2)
                    self.root.destroy()
                    import login
                    con.commit()

                con.commit()
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"{es}",parent = self.root2)
                self.usrnew_iden.delete(0,END)
                self.answeren.delete(0,END)
                self.usrnew_passen.delete(0,END)
    
    def ureg_login(self):
        if self.user_name.get() =="" or self.usr_pass.get() =="":
            messagebox.showerror("Error","All fields are mandatory",parent = self.root)
        else:
            if self.usr_type.get() == "Admin":
                if self.user_name.get()=="admin@ims" and self.usr_pass.get() =="admin_ims123":
                    self.root.destroy()
                    import admin
                    admin.run_admin(self.user_name.get())
                else:
                    messagebox.showerror("Error","Incorrect login details!",parent = self.root)
                    self.usr_pass.set('')
                    self.user_name.set('')
            else:
                con = mysql.connector.connect(host="localhost",user="root",passwd="root",database="ims")
                cur = con.cursor(buffered=True)
                select = "SELECT * FROM USERS WHERE username = %s and password = %s"
                value = (self.user_name.get(),self.usr_pass.get())
                cur.execute(select,value)
                rows = cur.fetchone()
                if rows == NONE:
                    messagebox.showerror("Error","Incorrect login details!",parent = self.root)
                    self.usr_pass.set('')
                    self.user_name.set('')
                else:
                    self.root.destroy()
                    import buyer
                    buyer.run_buyer(self.user_name.get())
                   
                con.commit()
                con.close()
         
    
    def ureg_forgotpass(self):
        
        self.root2 = Toplevel()
        self.root2.geometry("1600x800+0+0")
        self.root2.config(bg="white")
        self.root2.focus_force()
        self.root2.grab_set()
        self.back= ImageTk.PhotoImage(Image.open("../IMS/icons/bglogin.jpg"))
        back= Label(self.root2,image=self.back)
        back.place(x=0,y=0,relwidth=1,relheight=1)
        self.update_btn=ImageTk.PhotoImage(Image.open("../IMS/icons/button_update_pw.png"))
        self.email_id= StringVar()
        self.question=StringVar()
        self.answer= StringVar()
        self.new_pass= StringVar()
        self.logo2= ImageTk.PhotoImage(Image.open("../IMS/icons/logo.jpg"))
        logo2= Label(self.root2,image=self.logo2)
        logo2.place(x=400,y=130,width=100,height=100)
        ims2= Label(self.root2,text="Inventory Management System",font =("Times New Roman",35),image=self.titlebg)
        ims2.place(x=520,y=130,width=680,height=100)
        self.root2 = LabelFrame(self.root2, text="RECOVER PASSWORD", bg = "white", font =("Times New Roman",22))
        self.root2.place(x = 400, y = 260, height = 380, width = 780)

        usrnew_id = Label(self.root2, text = "         Email id       :",bg = "tomato", font =("Times New Roman",18)).grid(row = 0, column = 0,padx = 10, pady = 15,sticky="w")

        self.usrnew_iden = Entry(self.root2, textvariable = self.email_id,bd="3",width = 43,bg = "LightGray", font =("Times New Roman",18))
        self.usrnew_iden.grid(row = 0, column = 1,padx = 10, pady = 15,sticky="w")
        
        security = Label(self.root2, text = " Security question :",bg = "tomato", font =("Times New Roman",18)).grid(row = 1, column = 0,padx = 10, pady = 15,sticky="w")

        self.security_combo = ttk.Combobox(self.root2,textvariable = self.question, font =("Times New Roman",18), width = 41,state = "readonly" , justify = "center")
        self.security_combo['values']=("Select","Your favourite book","Your favourite movie","Your best friend")
        self.security_combo.grid(row = 1, column = 1,padx = 10, pady = 15,sticky="w")
        self.security_combo.current(0)

        answer = Label(self.root2, text = "        Answer         :",bg = "tomato", font =("Times New Roman",18)).grid(row = 2, column = 0,padx = 10, pady = 15,sticky="w")

        self.answeren = Entry(self.root2, textvariable = self.answer,bd="3",width = 43,bg = "LightGray", font =("Times New Roman",18))
        self.answeren.grid(row = 2, column = 1,padx = 10, pady = 15,sticky="w")

        usrnew_pass = Label(self.root2, text = "   New Password   :",bg = "tomato", font =("Times New Roman",18)).grid(row = 3, column = 0,padx = 10, pady = 15,sticky="w")

        self.usrnew_passen = Entry(self.root2, textvariable = self.new_pass,bd="3",width = 43,bg = "LightGray", font =("Times New Roman",18))
        self.usrnew_passen.grid(row = 3, column = 1,padx = 10, pady = 15,sticky="w")
        
        #self.new_pass = Button(self.root2, image=self.login_b, font =("Impact",14),bd="0", command = self.new_password)
        #self.new_pass = Button(self.root2, text  = "Update Password", bd="0",bg="Red", fg="White",font =("Times New Roman",18,"bold"), command = self.new_password)
        #self.new_pass.place(x=305, y = 280, width = 200, height = 42)
        self.new_pass = Button(self.root2, image=self.update_btn, font =("Impact",14),bd=3,bg="red2", command = self.new_password)
        self.new_pass.place(x=305, y = 280, width = 200, height = 42)

       

        

    def register(self):
        self.root.destroy()
        import register

root = Tk()
obj = User_Login(root)
root.mainloop()
