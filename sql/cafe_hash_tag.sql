create database cafe_hash_tag;
use cafe_hash_tag;

create table sign_up
(
customer_name nvarchar(100),
contact nvarchar(10),
gmail nvarchar(50) primary key,
pass nvarchar(8)
);
 


create table costomer_details
(
customer_ID int(20) primary key,
firstname nvarchar (100),
lastname nvarchar (100),
Contact bigInt(10),
Address nvarchar(100),
ID_proof nvarchar(20),
ID_No nvarchar(20),
Gender nvarchar(20),
date1 nvarchar(20),
time1 nvarchar(20)
);


create table Orders(
	Order_ID int(20) primary key,
    Price int(20)
);
alter table Orders add column Customer_ID int ;

create table Final_Order(
	Order_ID int primary key,
    Price int 
);
alter table Final_Order add column Customer_ID int ;
alter table final_order add column Customer_Name varchar(250);
alter table final_order add column Customer_Surname varchar(250);




create table payment_details
(
customer_ID int(20) primary key,
customer_name nvarchar(50),
total_payment nvarchar(20),
payment_method nvarchar(50)
);

