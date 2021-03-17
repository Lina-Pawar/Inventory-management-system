from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector

class User_Register:
    def __init__(self,root):
        self.root = root
        self.root.title('Inventory Management')
        self.root.geometry("1600x800+0+0")
        self.root.iconbitmap('../IMS/icons/Iconinv.ico')
        self.bg= ImageTk.PhotoImage(Image.open("../IMS/icons/bgregister.png"))
        bg= Label(self.root,image=self.bg)
        bg.place(x=0,y=0,relwidth=1,relheight=1)
        self.login_b=ImageTk.PhotoImage(Image.open("../IMS/icons/button_login.png"))
        self.regs_b=ImageTk.PhotoImage(Image.open("../IMS/icons/button_register.png"))
        self.imslogo=ImageTk.PhotoImage(Image.open("../IMS/icons/logo2.png"))
        logo= Label(self.root,image=self.imslogo)
        logo.place(x=80,y=200,width=320,height=320)

        def login():
            self.root.destroy()
            import login

        def unew_login():
            if self.fname.get() =="" or self.lname.get()=="" or self.mail.get()=="" or self.ans.get()=="" or self.password.get()=="" or self.usrnew_passcnen.get()=="" or self.username.get()=="":
                messagebox.showerror("Error","All fields are mandatory",parent = self.root)
            elif self.password.get() != self.usrnew_passcnen.get():
                messagebox.showerror("Error","Password does not match",parent = self.root)
            else:
                try:
                    con = mysql.connector.connect(host="localhost",user="root",passwd="root",database="ims")
                    cur = con.cursor(buffered=True)
                    select = "SELECT mail_id FROM USERS"
                    cur.execute(select)
                    for (mail_id) in cur:
                        if self.mail.get() == mail_id:
                            messagebox.showerror("Error","User already exists",parent = self.root)
                        else:
                            login_insert = "INSERT INTO users (f_name , l_name, contact, mail_id , que , answer , password, username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                            keys = (self.fname.get(),
                                    self.lname.get(),
                                    self.contact.get(),
                                    self.mail.get(),
                                    self.ques.get(),
                                    self.ans.get(),
                                    self.password.get(),
                                    self.username.get()
                                    )
                            cur.execute(login_insert,keys)
                            con.commit()
                            con.close()
                            messagebox.showinfo("Success","Registration successful",parent = self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Error due to {es}",parent = self.root)
                self.root.destroy()
                import login                                  


        self.usrn_frame = LabelFrame(self.root, text ="REGISTER", padx = 10, pady = 10, font =("Arial",20),bg="White")
        self.usrn_frame.place(x=650, y=85, height = 580, width = 700)
        usrnew_1st = Label(self.usrn_frame, text = "First Name     : ",font =("Arial",16),bg="Firebrick2", fg="White").grid(row = 1, column = 0, padx = 10, pady = 10)
        self.fname = Entry(self.usrn_frame, width = 40, bg = "White", font =("Arial",16))
        self.fname.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.fname.bind('<KeyPress>', self.char_validate)
        usrnew_last = Label(self.usrn_frame, text = "Last Name     : ",font =("Arial",16),bg="Firebrick2", fg="White").grid(row = 2, column = 0, padx = 10, pady = 10)
        self.lname = Entry(self.usrn_frame, width = 40, bg = "White", font =("Arial",16))
        self.lname.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.lname.bind('<KeyPress>', self.char_validate)
        usrnew_contact = Label(self.usrn_frame, text = "Contact No.    : ", font =("Arial",16),bg="Firebrick2", fg="White").grid(row = 3, column = 0, padx = 10, pady = 10)
        self.contact = Entry(self.usrn_frame, width = 40, bg = "White", font =("Arial",16))
        self.contact.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.contact.bind('<KeyPress>', self.num_validate)        
        usrnew_id = Label(self.usrn_frame, text = "E-mail id         : ", font =("Arial",16),bg="Firebrick2", fg="White").grid(row = 4, column = 0, padx = 10, pady = 10)
        self.mail = Entry(self.usrn_frame, width = 40, bg = "White", font =("Arial",16))
        self.mail.grid(row = 4, column = 1, padx = 10, pady = 10)
        security = Label(self.usrn_frame, text = "Security Ques : ", font =("Arial",16),bg="Firebrick2", fg="White").grid(row = 5, column = 0, padx = 10, pady = 10)
        self.ques = ttk.Combobox(self.usrn_frame, font =("Arial",16), state = "readonly" , width = 39, justify = "center")
        self.ques['values']=("Select","Your favourite book","Your favourite movie","Your best friend")
        self.ques.grid(row = 5, column = 1, padx = 10, pady = 10 )
        self.ques.current(0)
        answer = Label(self.usrn_frame, text = "Answer           : ", font =("Arial",16),bg="Firebrick2", fg="White").grid(row = 6, column = 0, padx = 10, pady = 10)
        self.ans = Entry(self.usrn_frame, width = 40, bg = "White", font =("Arial",16))
        self.ans.grid(row = 6, column = 1, padx = 10, pady = 10)
        usrnew_pass = Label(self.usrn_frame, text = "Password       : ", font =("Arial",16),bg="Firebrick2", fg="White").grid(row = 7, column = 0, padx = 10, pady = 10)
        self.password = Entry(self.usrn_frame,show = "*", width = 40, bg = "White", font =("Arial",16))
        self.password.grid(row = 7, column = 1, padx = 10, pady = 10)
        usrnew_passcn = Label(self.usrn_frame, text = "Confirm Pass : ", font =("Arial",16),bg="Firebrick2", fg="White").grid(row = 8, column = 0, padx = 10, pady = 10)
        self.usrnew_passcnen = Entry(self.usrn_frame,show = "*", width = 40, bg = "White", font =("Arial",16))
        self.usrnew_passcnen.grid(row = 8, column = 1, padx = 10, pady = 10)
        usrnew_uname = Label(self.usrn_frame, text = "Username      : ", font =("Arial",16),bg="Firebrick2", fg="White").grid(row = 9, column = 0, padx = 10, pady = 10)
        self.username = Entry(self.usrn_frame, width = 40, bg = "White", font =("Arial",16))
        self.username.grid(row = 9, column = 1, padx = 10, pady = 10)
        self.register = Button (self.usrn_frame, image=self.regs_b, command = unew_login, font = ("Arial",18),bd=3,bg="red2")
        self.register.place(x=210, y=460, height = 50, width = 250)
        self.login = Button(self.root, image=self.login_b, command = login, font = ("Arial",18),bd=3,bg="red2")
        self.login.place(x=120, y=590, height = 50, width = 250)
        
    def num_validate(self,event):
        if event.keysym == 'Tab':
            return
        if event.keysym == 'BackSpace':
            return
        widget = event.widget  
        entry = widget.get()
        x = widget.index(INSERT)
        if not event.char.isdigit() or x > 9:
            widget.bell()
            return 'break'
        else: 
            widget.delete(x)   

    def char_validate(self,event):
        if event.keysym == 'Tab':
            return
        if event.keysym == 'BackSpace':
            return
        widget = event.widget  
        entry = widget.get()
        x = widget.index(INSERT)
        if not event.char.isalpha():
            widget.bell()
            return 'break'
        else: 
            widget.delete(x)

root = Tk()
obj = User_Register(root)
root.mainloop()
