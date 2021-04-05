# Inventory Management System
Inventory Management software in Tkinter library in python  This is GUI based inventory management software implemented in tkinter library of python. Database file is attached along with this repository that contains all the necessary tables and columns for this project.
unctionalities implemented:

Stock Management: This is used to add the new items that are brought in the inventory. It can also be used to update the existing items that are available in inventory. e.g, sometimes quantities of the products needs to be modified. Delete functionality is also provided to remove the items that are discontinued or not brought due to any reason.
Billing Section: Billing section is also there that would create the invoice and save it in .txt format in IMS folder. It is used to create an invoice using item no. Customer name and customer phone number are mandatory part to generate invoice that would have invoice id as a random number between 1000 and 9999.
Pre-Requisites:
Make sure you have latest python version installed on your system.
Make sure you have install the required libraries using these commands-
1. pip install pymysql
2. pip install mysql-connector-python
3. pip install prettytable
4. pip install tkcalendar

Make sure you have mysql database with mysql-connector-python installed on your system along with phpMyadmin to access database graphically.
Steps to run:

Create a database named 'ims' in phpmyadmin and now import inventory.sql file that is provided in this repository.

Important Note:- My mysql username is root and password is root and hostname is localhost. So, Make sure you make changes in code according to your own username, password and hostname in all python files which otherwise would generate an error.
Somethings to be kept in mind:
1)First of all setup the xammp,php my admin in your pc and add the database their first by creatin the database with same name in local host and then import the downloaded sql file in it
2)Download all packages mentioned above at start of all files
3)Keep all files in single folder,save it

Then just double click login.py or run it through command prompt.