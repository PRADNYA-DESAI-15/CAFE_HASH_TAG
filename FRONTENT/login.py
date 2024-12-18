from tkinter import *
import mysql.connector
from  tkinter import messagebox
from PIL import ImageTk, Image
import os

conn=mysql.connector.connect(host="localhost",user="root",password="pradnya1512",database="cafe_hash_tag")

if(conn.is_connected()):
    print("connection succesfully")
else:
    print("connection failed")

def login():
    var = box1.get()
    var2 = box2.get()

    cur=conn.cursor(buffered=True)
    sql="select * from sign_up where gmail='"+var+"' and pass='"+var2+"' "
    result=cur.execute(sql)
    conn.commit()
    rows=cur.fetchall()
    if rows:
        messagebox.showinfo("Login Message", "Login Success")
        os.system("home.py")
    else:
        messagebox.showinfo("Login Message","Login failed")

def sign_up():
    os.system("sign_up.py")

def forgot_pass():
    os.system("reset_password.py")




root=Tk()
root.geometry("1366x768+0+0")
root.configure(bg="grey")
root.title("CAFE #_TAG")

image_1=Image.open( "D:\pictures\Saved Pictures\Coffee_Cup_Grain_513119_1366x768.jpg")
bck_end=ImageTk.PhotoImage(image_1)
mainlabel=Label(root,image=bck_end)
mainlabel.place(x=0,y=0)


myframe = Frame(root, bg="lavender", height=400, width=600)
myframe.place(x=400, y=100)

frame2 = Frame(myframe, bg="teal", height=100, width=700)
frame2.place(x=0, y=0)

mainlabel=Label(root,text="CAFE_#_TAG",bg="teal",font=("Action Man Shaded",30,"bold"))
mainlabel.place(x=575,y=110)

mainlabel1=Label(root,text="Gmail  :",bg="lavender",font=("Action Man",15))
mainlabel1.place(x=500,y=240)

box1=Entry(root,font=("Action Man",15))
box1.place(x=650,y=240)

mainlabel2=Label(root,text="Password :",bg="lavender",font=("Action Man",15))
mainlabel2.place(x=500,y=290)

box2=Entry(root,font=("Action Man",15),show="*")
box2.place(x=650,y=290)

B1=Button(root,text="Login",fg="white",bg="green",font=("Action Man",16),command=login)
B1.place(x=550,y=385)

B2=Button(root,text="Sign Up",fg="white",bg="red",font=("Action Man",16),command=sign_up)
B2.place(x=700,y=385)

B3=Button(root,text="Forget Password",fg="black",font=("Action Man",10,"underline"),command=forgot_pass)
B3.place(x=780,y=340)











root.mainloop()
