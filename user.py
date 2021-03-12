from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
import math,random
import pymysql
from datetime import date

class Bill_App:
    def __init__(self,root,id):
        self.root=root
        self.root.geometry("1600x800+0+0")
        self.root.iconbitmap('../IMS/icons/Iconinv.ico')
        self.root.title("Inventory Management")
        title=Label(self.root,text="Inventory Management System",bd=5,relief=SOLID,fg="white",bg="red2",font=("times new roman",40,"bold"))
        title.pack(side=TOP,fill=X)
        self.bg= ImageTk.PhotoImage(Image.open("../IMS/icons/bg.jpg"))
        bg= Label(self.root,image=self.bg)
        bg.place(x=0,y=72,relwidth=1,relheight=1)
        self.ttotal = ImageTk.PhotoImage(file="../IMS/icons/total.png")
        self.Gen_bill=ImageTk.PhotoImage(file="../IMS/icons/bill.png")
        self.Clear_b=ImageTk.PhotoImage(file="../IMS/icons/clear.png")
        self.inventory_b=ImageTk.PhotoImage(file="../IMS/icons/inventory.png")
        self.exit_b=ImageTk.PhotoImage(file="../IMS/icons/exit.png")
        self.search_b=ImageTk.PhotoImage(file="../IMS/icons/search.png")
        self.add_b=ImageTk.PhotoImage(file="../IMS/icons/addc.png")
        self.mybills=ImageTk.PhotoImage(file="../IMS/icons/mybills.png")
        self.total_entry=DoubleVar()
        self.tax_entry=DoubleVar()
        self.grand_total=DoubleVar()
        self.customer_pay=DoubleVar()
        self.search_item_no=StringVar()
        self.search_item_no.set("")

        self.item_no=StringVar()
        self.item_name=StringVar()
        self.item_price=IntVar()
        self.item_quantity=IntVar()
        self.item_quantity.set(1)
        
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s",(id))
        rows=cur.fetchall()
        for row in rows:
            fn=row[1]
            ln=row[2]
            name=f'{fn} {ln}'
            con.commit()
        con.close()
        self.c_name=StringVar()
        self.c_name.set(name)
                
        self.username=StringVar()
        self.bill_no=IntVar()
        self.search_bill=StringVar()
        
        self.username.set(id)
        self.bill_no.set(int(random.randint(1000,9999)))
        
        F1=LabelFrame(self.root,bd=5,relief=GROOVE, text="Customer Details",font=("times new roman",15,"bold"),fg="Black",bg="white")
        F1.place(x=0,y=75,relwidth=1,height=80)

        cname_lbl=Label(F1,bg="red2",fg="white",text="Customer Name:",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=2)
        cname_txt=Entry(F1,textvariable=self.c_name,width=20,font="arial 15",bd=3,relief=SUNKEN,state=DISABLED).grid(row=0,column=1,pady=2,padx=10)

        uname_lbl=Label(F1,bg="red2",fg="white",text="Username:",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        uname_txt=Entry(F1,textvariable=self.username,width=20,font="arial 15",bd=3,relief=SUNKEN,state=DISABLED).grid(row=0,column=3,pady=2,padx=10)

        bill_btn=Button(F1,image=self.mybills,width=113,height=25,bg="red2",text="Search",bd=3,font="arial 15 bold").grid(row=0,column=4,padx=20,pady=2)

        F2=LabelFrame(self.root,bd=5,relief=GROOVE, text="Search Items",font=("times new roman",15,"bold"),fg="Black",bg="white")
        F2.place(x=20,y=170,width=330,height=450)

        self.search_name= StringVar()

        item_no_lbl=Label(F2,text="Item Name.",font=("times new roman",16,"bold"),bg="red2",fg="white").grid(row=0,column=0,padx=0,pady=10,sticky="w")
        combo_search=ttk.Combobox(F2,textvariable=self.search_name,width=15 ,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=self.combo_value()
        combo_search.grid(row=0,column=1, padx=20,pady=10)

        search_no_btn=Button(F2,image=self.search_b,command=self.search_item,bg="red2",text="Search",fg="white",pady=10,width=120,bd=3,font="arial 15 bold").grid(row=1,column=1,padx=15,pady=5)
        
        F2A=LabelFrame(self.root,bd=5,relief=GROOVE,font=("times new roman",15,"bold"),bg="white")
        F2A.place(x=110,y=370,width=140,height=80)

        btn_inventory=Button(F2A,image=self.inventory_b,command=self.Inventory,width=80,height=65,font=("Arial",7,"bold"),compound=TOP,pady=6,bg="red2",fg="black",bd=3).place(x=10,y=10,width=50,height=50)
        Exit_btn=Button(F2A,image=self.exit_b,command=self.exit,width=80,height=65,font=("Arial",7,"bold"),compound=TOP,pady=6,bg="red2",fg="black",bd=3).place(x=70,y=10,width=50,height=50)

        F3=LabelFrame(self.root,bd=5,relief=GROOVE, text="Item Details",font=("times new roman",15,"bold"),fg="Black",bg="white")
        F3.place(x=370,y=170,width=350,height=450)

        g1_lbl=Label(F3,text="Item No:",font=("times new roman",16,"bold"),bg="red2",fg="white").grid(row=0,column=0,padx=0,pady=10,sticky="w")
        g1_txt=Label(F3,textvariable=self.item_no,font=("times new roman",16,"bold"),width=15,bg="Lightgray",fg="black").grid(row=0,column=1,padx=10,pady=10,stick="w")

        g2_lbl=Label(F3,text="Item Name:",font=("times new roman",16,"bold"),bg="red2",fg="white").grid(row=1,column=0,padx=0,pady=10,sticky="w")
        g2_txt=Label(F3,textvariable=self.item_name,font=("times new roman",16,"bold"),width=15,bg="Lightgray",fg="black").grid(row=1,column=1,padx=10,pady=10,stick="w")

        g3_lbl=Label(F3,text="Price (in Rs):",font=("times new roman",16,"bold"),bg="red2",fg="white").grid(row=2,column=0,padx=0,pady=10,sticky="w")
        g3_txt=Label(F3,textvariable=self.item_price,font=("times new roman",16,"bold"),width=15,bg="Lightgray",fg="black").grid(row=2,column=1,padx=10,pady=10,stick="w")

        item_qty_lbl=Label(F3,text="Item Quantity.",font=("times new roman",16,"bold"),bg="red2",fg="white").grid(row=3,column=0,padx=0,pady=10,sticky="w")
        item_qty_txt=Entry(F3,width=10,textvariable=self.item_quantity,font=("times new roman",16,"bold"),bd=3,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


        addcart=Button(F3,image=self.add_b,command=self.add_item,bg="red2",fg="white",pady=15,width=120,bd=3,font="arial 15 bold").grid(row=4,column=1,padx=5,pady=5)

        F4=LabelFrame(self.root,bd=5,relief=GROOVE, text="Shopping Cart",font=("times new roman",16,"bold"),fg="Black",bg="White")
        F4.place(x=740,y=170,width=400,height=450)

        scroll_x=Scrollbar(F4,orient=HORIZONTAL)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
        self.Stock_Table=ttk.Treeview(F4, column=("item_no","item_name","qty","price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Stock_Table.xview)
        scroll_y.config(command=self.Stock_Table.yview)

        self.Stock_Table.heading("item_no",text="Item No")
        self.Stock_Table.heading("item_name",text="Item Name")
        self.Stock_Table.heading("qty",text="Qty")
        self.Stock_Table.heading("price",text="Price")
        self.Stock_Table['show']='headings'
        self.Stock_Table.column("item_no",width=30)
        self.Stock_Table.column("item_name",width=140)
        self.Stock_Table.column("qty",width=10)
        self.Stock_Table.column("price",width=20)
        self.Stock_Table.pack(fill=BOTH,expand=1)
        self.Stock_Table.bind("<ButtonRelease-1>",self.table_click)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=("Arial", 12))
        style.configure("Treeview.Heading", font=("Times new roman", 14, "bold"))

        F5=LabelFrame(self.root,bd=5,relief=GROOVE)
        F5.place(x=1160,y=170,width=350,height=450)
        bill_title=Label(F5,text="Bill Area",font=("arial",15, "bold"), bd=3, bg="red2", relief=GROOVE).pack(fill=X)

        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)

        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        F6=LabelFrame(self.root,bd=5,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),bg="White",fg="Black")
        F6.place(x=0,y=640,relwidth=1,height=140)

        Totallbl = Label(F6,text="Total Bill:", font=("Times",14,"bold"),bg="red2",fg="white")
        Totallbl.grid(row=0,column=0,padx=10,pady=5,sticky="w")
        TotalEntry = Entry(F6,width=10, textvariable= self.total_entry,font=("Times",14,"bold"), bd=3, relief=SUNKEN,state=DISABLED)
        TotalEntry.grid(row=0,column=1,padx=10,pady=5)

        GSTlbl = Label(F6,text="GST:", font=("Times",14,"bold"),bg="red2",fg="white")
        GSTlbl.grid(row=1,column=0,padx=10,pady=5,sticky="w")
        GSTEntry = Entry(F6,width=10,textvariable=self.tax_entry,font=("Times",14,"bold"), bd=3, relief=SUNKEN,state=DISABLED)
        GSTEntry.grid(row=1,column=1,padx=10,pady=5)

        GrandTotallbl = Label(F6,text="Grand Total:", font=("Times",14,"bold"),bg="red2",fg="white")
        GrandTotallbl.grid(row=0,column=2,padx=10,pady=5,sticky="w")
        GrandTotalEntry = Entry(F6,width=10,textvariable=self.grand_total,font=("Times",14,"bold"), bd=3, relief=SUNKEN,state=DISABLED)
        GrandTotalEntry.grid(row=0,column=3,padx=10,pady=5)

        CPaylbl = Label(F6,text="Customer Pay:", font=("Times",14,"bold"),bg="red2",fg="white")
        CPaylbl.grid(row=1,column=2,padx=10,pady=5,sticky="w")
        CPayEntry = Entry(F6,width=10, font=("Times",14,"bold"),textvariable=self.customer_pay,bd=3, relief=SUNKEN,state=DISABLED)
        CPayEntry.grid(row=1,column=3,padx=10,pady=5)

        btn_F=Frame(F6,bd=3,bg="white",relief=GROOVE)
        btn_F.place(x=725,width=420,height=50)

        total_btn=Button(btn_F,image=self.ttotal,command=self.total,bg="red2",text="Total",fg="white",pady=6,width=100,height=30,bd=3)
        total_btn.grid(row=0,column=0,padx=6,pady=2)
       
        GBill_btn=Button(btn_F,image=self.Gen_bill,bg="red2",text="Generate Bill",fg="white",pady=6,width=150,height=30,bd=3)
        GBill_btn.grid(row=0,column=1,padx=6,pady=2)

        Clear_btn=Button(btn_F,image=self.Clear_b,command=self.clear,bg="red2",text="Clear",fg="white",pady=6,width=100,height=30,bd=3)
        Clear_btn.grid(row=0,column=2,padx=6,pady=2)
        

    def search_item(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute(f"SELECT * FROM inventory WHERE product_name='{self.search_name.get()}'")
        rows=cur.fetchall()
        if len(rows)==0:
            messagebox.showinfo("Alert","Choose an item!")
        else:
            for row in rows:
                self.item_no.set(row[0])
                self.item_name.set(row[1])
                self.item_price.set(row[3])
        con.commit()
        con.close()


    def add_item(self):
        if(self.item_no.get()==""):
            messagebox.showinfo("Alert","Choose an item.")
        else:
            con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
            cur=con.cursor()
            cur.execute(f"SELECT * from inventory where product_name='{self.search_name.get()}'")
            rows=cur.fetchall()
            available_quantity=rows[0][2]

            listOfEntriesInTreeView=self.Stock_Table.get_children()
            for each in listOfEntriesInTreeView:
                new_quantity=int(self.item_quantity.get())
                if new_quantity<available_quantity or new_quantity==available_quantity:
                    new_item=(self.item_no.get(),self.item_name.get(),new_quantity,self.item_price.get()*new_quantity)
                    self.Stock_Table.insert('',END, values=new_item)
                    return
                else:
                    messagebox.showinfo("Alert","Available quantity is less.")
                    return
                    
            if int(self.item_quantity.get())<available_quantity or int(self.item_quantity.get())==available_quantity:
                new_item=(self.item_no.get(),self.item_name.get(),self.item_quantity.get(),self.item_price.get()*self.item_quantity.get())
                self.Stock_Table.insert('',END, values=new_item)
        
            con.close()
        self.total()
        
        


    def total(self):
        ftotal=0
        listOfEntriesInTreeView=self.Stock_Table.get_children()
        for each in listOfEntriesInTreeView:
            ftotal=ftotal+int(self.Stock_Table.item(each)['values'][3])
        tax = 0.18*ftotal
        gtotal = ftotal + tax
        cust=gtotal-0.02*gtotal
        self.total_entry.set(ftotal)
        self.tax_entry.set(tax)
        self.grand_total.set(gtotal)
        self.customer_pay.set(cust)



    def cart_items(self):
        listOfEntriesInTreeView=self.Stock_Table.get_children()
        i=0
        for each in listOfEntriesInTreeView:
            i=i+1
        return (i)


    def table_click(self,ev):
        cursor_row=self.Stock_Table.focus()
        contents=self.Stock_Table.item(cursor_row)
        row=contents['values']
        self.item_no.set(row[0])
        self.item_name.set(row[1])
        self.item_quantity.set("1")
        self.item_price.set(row[3])


    def clear(self):
        self.Stock_Table.delete(*self.Stock_Table.get_children())
        self.item_no.set("")
        self.item_name.set("")
        self.item_price.set(0)
        self.item_quantity.set(1)
        self.bill_no.set(int(random.randint(1000,9999)))
        self.total_entry.set("")
        self.tax_entry.set("")
        self.grand_total.set("")
        self.customer_pay.set("")
        


    
    def Inventory(self):
        self.root2=Toplevel()
        self.root2.geometry("480x470+10+200")

        self.table_frame=Frame(self.root2,bd=4,relief=RIDGE,bg="ivory")
        self.table_frame.place(x=10,y=10,width=460,height=450)
        
        scroll_x=Scrollbar(self.table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
        self.invent_table=ttk.Treeview(self.table_frame,columns=("PRODUCT ID","PRODUCT NAME","PRICE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.invent_table.xview)
        scroll_y.config(command=self.invent_table.yview)
        self.invent_table.heading("PRODUCT ID",text="PRODUCT ID:")
        self.invent_table.heading("PRODUCT NAME",text="PRODUCT NAME:")
        self.invent_table.heading("PRICE",text="PRICE:")
        self.invent_table['show']='headings'
        self.invent_table.column("PRODUCT ID",width=50)
        self.invent_table.column("PRODUCT NAME",width=200)
        self.invent_table.column("PRICE",width=30)
        self.invent_table.pack(fill=BOTH,expand=1)
        self.invent_table.bind("<ButtonRelease-1>",self.get_cursor)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=("Arial", 12))
        style.configure("Treeview.Heading", font=("Times new roman", 14, "bold"))
        self.fetch_data()


    def fetch_data(self): 
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("SELECT product_id,product_name,product_price from inventory")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.invent_table.delete(*self.invent_table.get_children())
            for row in rows:
                self.invent_table.insert('',END,values=row)
                con.commit()
        con.close()


    def get_cursor(self,ev):
        cursor_row=self.invent_table.focus()
        content=self.invent_table.item(cursor_row)
        row=content['values']
        self.item_no.set(row[0])
        self.item_name.set(row[1])
        self.item_quantity.set("1")
        self.item_price.set(row[2])


    def combo_value(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("SELECT product_name from inventory")
        result = []

        for row in cur.fetchall():
            result.append(row[0])

        return result


    def exit(self):
        mes= messagebox.askyesno("Notification","Do You want to logout?")    
        if mes > 0:
            self.root.destroy()
            import login


def run_user(id):
    root=Tk()
    obb=Bill_App(root,id)
    root.mainloop()

    