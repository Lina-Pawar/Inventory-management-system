from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from PIL import Image,ImageTk
import math,random



class Customer:
    def __init__(self,root,id):
        self.root = root
        self.root.title("----INVENTORY MANAGEMENT----")
        self.root.geometry("1600x800+0+0")
        self.root.iconbitmap('D:/IMS/icons/Iconinv.ico')
        bg_color="white"
        title=Label(self.root,text="INVENTORY MANAGEMENT SYSTEM",bd=5,relief=SOLID,fg="white",bg="red2",font=("times new roman",40,"bold"))
        title.pack(side=TOP,fill=X)
        self.bg= ImageTk.PhotoImage(Image.open("D:/IMS/icons/bglogin.jpg"))
        bg= Label(self.root,image=self.bg)
        bg.place(x=0,y=72,relwidth=1,relheight=1)
        admin=Label(self.root, text="admin@ims", fg="white",bg="red2",font=("times new roman",14,"bold"))
        admin.place(x=50,y=200,width=200,height=30)

def run_admin(id):
    root=Tk() 
    obj=Customer(root,id)
    print(id)
    root.mainloop()
