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

create table order_details
(
customer_ID int(20) primary key,
place nvarchar(20),
Order1 nvarchar(200),
total_payment nvarchar(20)
);

create table payment_details
(
customer_ID int(20) primary key,
customer_name nvarchar(50),
total_payment nvarchar(20),
payment_method nvarchar(50)
);
