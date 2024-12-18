from tkinter import *
import mysql.connector
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

tree= ttk.Treeview(root,column=('C1','C2','C3'),show="headings")
tree.column("#1",width=150)
tree.heading("#1",text="Menu Name")

tree.column("#2",width=150)
tree.heading("#2",text="Category")

tree.column("#3",width=150)
tree.heading("#3",text="Menu Price")

tree.place(x=450,y=170)

mainlabel=Label(root,text="MENU  CARD ",bg="yellow",font=("Action Man Shaded",30,"bold"))
mainlabel.place(x=550,y=25)

mainlabel=Label(root,text="Customer_ID :" , bg="black",fg="white",font=("Action Man",15))
mainlabel.place(x=750,y=120)

box1=Entry(root ,font=("Action Man",15))
box1.place(x=880,y=120)

B1=Button(root,text=" SHOW INFO  ",fg="white",bg="black",font=("Action Man",12,"underline"))
B1.place(x=1100,y=120)

B2=Button(root,text="  EXIT  ",fg="white",bg="black",command=Exit,font=("Action Man",12,"underline"))
B2.place(x=1250,y=120)

root.mainloop()