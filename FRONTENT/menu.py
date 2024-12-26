from tkinter import *
import mysql.connector
from  tkinter import messagebox
import os
from PIL import ImageTk, Image


conn=mysql.connector.connect(host="localhost",user="root",password="pradnya1512",database="cafe_hash_tag")
if(conn.is_connected()):
    print("connection succesfully")
else:
    print("connection failed")

def update():
    m_name=box1.get()
    category=box2.get()
    m_price=box3.get()

    cur = conn.cursor()
    sql = "insert into menu_details(menu_name,category,menu_price) values ('" + m_name + "','" + category + "','" + m_price + "' );"
    result = cur.execute(sql)
    messagebox.showinfo("Success", "Data inserted successfully")
    conn.commit()
    cur.close()



def search():
    m_name=box1.get()
    print(m_name)
    cur=conn.cursor(buffered=True)
    sql="select * Menu_card where Menu Name='"+m_name+"' "


def Exit():
    os.system("login.py")


root=Tk()
root.geometry("1366x768+0+0")
root.configure(bg="sky blue")
root.title("CAFE #_TAG")

image_1=Image.open( "D:\pictures\Saved Pictures\Coffee_Cup_Grain_513119_1366x768.jpg")
bck_end=ImageTk.PhotoImage(image_1)
mainlabel=Label(root,image=bck_end)
mainlabel.place(x=0,y=0)

myframe = Frame(root, bg="black", height=400, width=600)
myframe.place(x=400, y=70)

frame2 = Frame(myframe, bg="yellow", height=100, width=600)
frame2.place(x=0, y=0)

mainlabel=Label(root,text="Menu Details",bg="yellow",font=("Action Man Shaded",30,"bold"))
mainlabel.place(x=530,y=85)

mainlabel1=Label(root,text="Menu Name         :",fg="white",bg="black",font=("Action Man",15))
mainlabel1.place(x=500,y=230)
box1=Entry(root,font=("Action Man",15))
box1.place(x=700,y=230)

mainlabel2=Label(root,text="Category          :",fg="white",bg="black",font=("Action Man",15))
mainlabel2.place(x=500,y=280)
box2=Entry(root,font=("Action Man",15))
box2.place(x=700,y=280)

mainlabel3=Label(root,text="Menu Price        :",fg="white",bg="black",font=("Action Man",15))
mainlabel3.place(x=500,y=330)
box3=Entry(root,font=("Action Man",15))
box3.place(x=700,y=330)

B3=Button(root,text="Search",fg="white",bg="black",font=("Action Man",16),command=update)
B3.place(x=500,y=400)

B1=Button(root,text="Update",fg="white",bg="black",font=("Action Man",16),command=update)
B1.place(x=620,y=400)

B2=Button(root,text="Clear",fg="white",bg="black",font=("Action Man",16),command=Exit)
B2.place(x=740,y=400)

B4=Button(root,text="Save",fg="white",bg="black",font=("Action Man",16),command=update)
B4.place(x=860,y=400)












root.mainloop()
