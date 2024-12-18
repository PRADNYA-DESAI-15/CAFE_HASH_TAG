from tkinter import *
import mysql.connector
from tkinter import ttk
import os
from PIL import ImageTk, Image
from tkinter import messagebox

conn=mysql.connector.connect(host="localhost",user="root",password="pradnya1512",database="cafe_hash_tag")
if(conn.is_connected()):
    print("connection succesfully")
else:
    print("connection failed")

def Exit():
    os.system("home.py")

def search():
    ID=box1.get()
    print(ID)
    cur=conn.cursor(buffered=True)
    sql="select * from  customer_details where Customer_ID='"+ID+"' "
    result = cur.execute(sql)
    conn.commit()
    rows=cur.fetchall()

    for item in tree.get_children():
        tree.delete(item)

    if rows:
        for row in rows:
            print(row)
            tree.insert("",END ,value=row)

    else:
        messagebox.showinfo("table info","no recorders with given name")


root=Tk()
root.geometry("1366x768+0+0")
root.title("CAFE #_TAG")

image_1=Image.open( "D:\pictures\Saved Pictures\Coffee_Cup_Grain_513119_1366x768.jpg")
bck_end=ImageTk.PhotoImage(image_1)
mainlabel=Label(root,image=bck_end)
mainlabel.place(x=0,y=0)

frame2 = Frame(root, bg="yellow", height=100, width=1366)
frame2.place(x=0, y=0)

mainlabel=Label(root,text="CUSTOMER  DETAILS",bg="yellow",font=("Action Man Shaded",30,"bold"))
mainlabel.place(x=480,y=25)

tree= ttk.Treeview(root,column=('C1','C2','C3','C4','C5','C6','C7','C8','C9','C10'),show="headings")
tree.column("#1",width=100)
tree.heading("#1",text="Customer_ID")


tree.column("#2",width=100)
tree.heading("#2",text="First_Name")

tree.column("#3",width=100)
tree.heading("#3",text="Last_Name")

tree.column("#4",width=100)
tree.heading("#4",text="Contact")

tree.column("#5",width=100)
tree.heading("#5",text="Address")

tree.column("#6",width=100)
tree.heading("#6",text="Gender")

tree.column("#7",width=100)
tree.heading("#7",text="ID_Proof")

tree.column("#8",width=100)
tree.heading("#8",text="ID_No")

tree.column("#9",width=100)
tree.heading("#9",text="Date")

tree.column("#10",width=100)
tree.heading("#10",text="Time")

tree.place(x=150,y=170)

cur=conn.cursor(buffered=True)
sql="select * from customer_details"
result=cur.execute(sql)
conn.commit()
rows=cur.fetchall()
for row in rows:
    print(row)
    tree.insert("", END, value=row)

mainlabel=Label(root,text="Customer_ID :" , bg="black",fg="white",font=("Action Man",15))
mainlabel.place(x=750,y=120)

box1=Entry(root,font=("Action Man",15))
box1.place(x=880,y=120)

B1=Button(root,text=" SEARCH  ",fg="white",bg="black",font=("Action Man",12,"underline"),command=search)
B1.place(x=1100,y=120)

B2=Button(root,text="  EXIT  ",fg="white",bg="black",command=Exit,font=("Action Man",12,"underline"))
B2.place(x=1250,y=120)

root.mainloop()