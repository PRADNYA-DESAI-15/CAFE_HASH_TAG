from tkinter import *
import mysql.connector
from  tkinter import messagebox
from tkinter import ttk
import os
from PIL import ImageTk, Image

conn=mysql.connector.connect(host="localhost",user="root",password="pradnya1512",database="cafe_hash_tag")
if(conn.is_connected()):
    print("connection succesfully")
else:
    print("connection failed")

def Exit():
    os.system("Home_Page")


def search():
    ID=box1.get()
    print(ID)
    cur=conn.cursor(buffered=True)
    sql="select * from payment_details where Menu Name='"+ID+"' "
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
        messagebox.search("table info","no recorders with given name")


root=Tk()
root.geometry("1366x768+0+0")
root.configure(bg="sky blue")
root.title("CAFE #_TAG")

image_1=Image.open( "D:\pictures\Saved Pictures\Coffee_Cup_Grain_513119_1366x768.jpg")
bck_end=ImageTk.PhotoImage(image_1)
mainlabel=Label(root,image=bck_end)
mainlabel.place(x=0,y=0)

frame2 = Frame(root, bg="yellow", height=100, width=1366)
frame2.place(x=0, y=0)

tree= ttk.Treeview(root,column=('C1','C2','C3','C4'),show="headings")
tree.column("#1",width=150)
tree.heading("#1",text="Customer_ID")

tree.column("#2",width=150)
tree.heading("#2",text="Customer_Name")

tree.column("#3",width=150)
tree.heading("#3",text="Total Payment")

tree.column("#4",width=150)
tree.heading("#4",text="Payment_Method")
tree.place(x=370,y=170)

cur=conn.cursor(buffered=True)
sql="select * from payment_details"
result=cur.execute(sql)
conn.commit()
rows=cur.fetchall()
for row in rows:
    print(row)
    tree.insert("", END, value=row)

mainlabel=Label(root,text="PAYMENT  DETAILS",bg="yellow",font=("Action Man Shaded",30,"bold"))
mainlabel.place(x=480,y=22)

mainlabel=Label(root,text="Customer_ID :" , bg="black",fg="white",font=("Action Man",15))
mainlabel.place(x=750,y=120)

box1=Entry(root ,font=("Action Man",15))
box1.place(x=880,y=120)



B1=Button(root,text=" SEARCH   ",fg="white",bg="black",font=("Action Man",12,"underline"))
B1.place(x=1100,y=120)

B2=Button(root,text="  EXIT  ",fg="white",bg="black",command=Exit,font=("Action Man",12,"underline"))
B2.place(x=1250,y=120)

root.mainloop()