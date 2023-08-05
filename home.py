import pymysql
def home():
    # variables assign values
    # create a table inside booking_git
    # vehicles;
    # vehicle_id(primary key, AI); vehicle name, date of manufacture, owner
    # create a python program that saves records into the table
    Vehicle_Name='Subaru'
    Date_of_Manufactue='2006-04-08'
    Owner='Erick'
    con=pymysql.connect(host='localhost',user='root',password='',database='booking_git')
    cursor=con.cursor()
    sql='INSERT INTO Vehicles (Vehicle_Name,Date_of_Manufacture,Owner) VALUES(%s,%s,%s)'
    cursor.execute(sql,(Vehicle_Name,Date_of_Manufactue,Owner))
    con.commit()
    print('Saved Successfully')
home()
def home():
    Vehicle_Name='Toyota'
    Date_of_Manufactue='2008-02-18'
    Owner='Michael'
    con=pymysql.connect(host='localhost',user='root',password='',database='booking_git')
    cursor=con.cursor()
    sql='INSERT INTO Vehicles (Vehicle_Name,Date_of_Manufacture,Owner) VALUES(%s,%s,%s)'
    cursor.execute(sql,(Vehicle_Name,Date_of_Manufactue,Owner))
    con.commit()
    print('Saved Successfully')
home()
def home():
    Vehicle_Name='Nissan'
    Date_of_Manufactue='2010-12-04'
    Owner='Catherine'
    con=pymysql.connect(host='localhost',user='root',password='',database='booking_git')
    cursor=con.cursor()
    sql='INSERT INTO Vehicles (Vehicle_Name,Date_of_Manufacture,Owner) VALUES(%s,%s,%s)'
    cursor.execute(sql,(Vehicle_Name,Date_of_Manufactue,Owner))
    con.commit()
    print('Saved Successfully')
home()
def home():
    Vehicle_Name='Mitsubishi'
    Date_of_Manufactue='2002-05-11'
    Owner='George'
    con=pymysql.connect(host='localhost',user='root',password='',database='booking_git')
    cursor=con.cursor()
    sql='INSERT INTO Vehicles (Vehicle_Name,Date_of_Manufacture,Owner) VALUES(%s,%s,%s)'
    cursor.execute(sql,(Vehicle_Name,Date_of_Manufactue,Owner))
    con.commit()
    print('Saved Successfully')
home()