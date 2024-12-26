from tkinter import *
import mysql.connector
import os
from PIL import ImageTk, Image


conn=mysql.connector.connect(host="localhost",user="root",password="pradnya1512",database="cafe_hash_tag")
if(conn.is_connected()):
    print("connection succesfully")
else:
    print("connection failed")

def login():
    os.system("login.py")

def sign_up():
    os.system("sign_up.py")

def reset():
    os.system("reset_password.py")

def customer():
    os.system("costomer_details.py")

def customer1():
    os.system("costomer.py")


def pay():
    os.system("payment_details.py")

def pay1():
    os.system("payment.py")

def menu():
    os.system("menu.py")

def menu1():
    os.system("menu_card.py")


root=Tk()

image_1=Image.open("D:\pictures\Saved Pictures\istockphoto-1303583671-170667a.jpg")
bck_end=ImageTk.PhotoImage(image_1)
lbl=Label(root,image=bck_end)
lbl.place(x=450,y=250)

root.geometry("1366x768+0+0")
root.configure(bg="black")
root.title("CAFE #_TAG")

myframe1 = Frame(root, bg="sky blue", height=60, width=1366)
myframe1.place(x=0, y=0)

myframe2 = Frame(root, bg="sky blue", height=50, width=1366)
myframe2.place(x=0, y=85)

mainlabel=Label(root,text="HOME PAGE" , bg="sky blue",fg="black",font=("Action Man shaded",28))
mainlabel.place(x=580,y=0)

mainlabel1=Label(root,text="The Stylish " , bg="black",fg="white",font=("Arial Black",32))
mainlabel1.place(x=100,y=185)

mainlabel2=Label(root,text="COFFEE" , bg="black",fg="#ff661a",font=("Arial Black",32))
mainlabel2.place(x=100,y=245)

mainlabel3=Label(root,text="CAFE CRUSH" , bg="black",fg="white",font=("Action Man shaded",28))
mainlabel3.place(x=580,y=80)

mainlabel4=Label(root,text=" A cup of coffee lasts \n only a moment, but \n it is that moment that \n  makes your day better." , bg="black",fg="white",font=("Harlow Solid Italic",20))
mainlabel4.place(x=100,y=350)

B1=Button(root,text="Login",fg="white",bg="black",font=("Action Man",13) ,width="23",command=login)
B1.place(x=1090,y=250)

B2=Button(root,text="Sign Up",fg="white",bg="black",font=("Action Man",13),width="23",command=sign_up)
B2.place(x=1090,y=290)

B3=Button(root,text="Customer Details",fg="white",bg="black",font=("Action Man",13),width="23",command=customer)
B3.place(x=1090,y=330)

B7=Button(root,text="Customer Info",fg="white",bg="black",font=("Action Man",13),width="23",command=customer1)
B7.place(x=1090,y=370)

B5=Button(root,text="Payment Details",fg="white",bg="black",font=("Action Man",13),width="23",command=pay)
B5.place(x=1090,y=410)

B10=Button(root,text="Payment Info",fg="white",bg="black",font=("Action Man",13),width="23",command=pay1)
B10.place(x=1090,y=450)

B6=Button(root,text="Menu Card",fg="white",bg="black",font=("Action Man",13),width="23",command=menu)
B6.place(x=1090,y=490)

B9=Button(root,text="Menu Info",fg="white",bg="black",font=("Action Man",13),width="23",command=menu1)
B9.place(x=1090,y=530)



root.mainloop()