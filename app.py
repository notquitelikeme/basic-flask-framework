import pymysql
def insert():
    Destination='Kisumu'
    Departure='Busia'
    Date='2022-10-14'
    Time='11:00 am'
    # connect the python file with the database(table)
    con=pymysql.connect(host='localhost',user='root',password='',database='booking_git')
    cursor=con.cursor()
    sql='INSERT INTO booking1 (Destination,Departure,Date,Time) VALUES(%s,%s,%s,%s)'
    cursor.execute(sql,(Destination,Departure,Date,Time))
    con.commit()
    print("Saved Successfully")
insert()
def insert():
    Destination='Isiolo'
    Departure='Mombasa'
    Date='2022-08-24'
    Time='5:30 am'
    # connect the python file with the database(table)
    con=pymysql.connect(host='localhost',user='root',password='',database='booking_git')
    cursor=con.cursor()
    sql='INSERT INTO booking1 (Destination,Departure,Date,Time) VALUES(%s,%s,%s,%s)'
    cursor.execute(sql,(Destination,Departure,Date,Time))
    con.commit()
    print("Saved Successfully")
insert()
def insert():
    Destination='TransNzoia'
    Departure='Lamu'
    Date='2022-1-25'
    Time='6:00 am'
    # connect the python file with the database(table)
    con=pymysql.connect(host='localhost',user='root',password='',database='booking_git')
    cursor=con.cursor()
    sql='INSERT INTO booking1 (Destination,Departure,Date,Time) VALUES(%s,%s,%s,%s)'
    cursor.execute(sql,(Destination,Departure,Date,Time))
    con.commit()
    print("Saved Successfully")
insert()