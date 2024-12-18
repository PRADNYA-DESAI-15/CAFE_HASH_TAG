create database cafe;
use cafe;
create table COSTOMER_DETAILS
(
Customer_ID int primary key,
Name_of_Customer nvarchar (100),
Contact bigInt(10),
Address nvarchar(100),
Aadhar_Card_No nvarchar(12)
);

create table order_details
(
Customer_ID int primary key,
Order_Place nvarchar(50),
Order_Price nvarchar(5),
Total_Payment nvarchar(5),
ID_Proof nvarchar(50),
ID_No nvarchar(20)
);

create table Payment_details
(
Customer_ID int primary key,
Total_Amount nvarchar(10)
);







