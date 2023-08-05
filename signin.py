import pymysql
from flask import *
# create the main app
app=Flask(__name__)
@app.route('/')
def main():
    return render_template('new.html')
# create route for signin
@app.route('/signup', methods=['POST','GET'])
def signup():
    # if statement to check form conditions
    if request.method=='POST':
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        phone=request.form['phone']
        id_no=request.form['id_no']
        # connect to the database
        con=pymysql.connect(host='localhost',user='root',password='',database='booking_git')
        cursor=con.cursor()
        sql='INSERT INTO Registration(fname,lname,email,phone,id_no) VALUES(%s,%s,%s,%s,%s)'
        cursor.execute(sql,(fname,lname,email,phone,id_no))
        con.commit()
        return render_template('signin.html',msg='Saved Successfully')
    else:
        return render_template('signup.html',msg='Invalid details. Please try again')
@app.route('/signin', methods=['POST','GET'])
# create a function
def signin():
    # if statements to check form conditions
    if request.method=='POST':
        email=request.form['email']
        id_no=request.form['id_no']
        # connect to the database
        con=pymysql.connect(host='localhost',user='root',password='',database='booking_git')
        # define the cursor
        cursor=con.cursor()
        cursor.execute('SELECT * FROM Registration WHERE email=%s and id_no=%s', (email,id_no))
        # if statement to check whether the details match
        if cursor.rowcount==0:
            return render_template('signin.html', msg='could not be found')
            # test another condition
        elif cursor.rowcount==1:
            return redirect('/save')
        else:
            return render_template('signin.html',msg='An error has occured!: Invalid Login Details')
    else:
        return render_template('signin.html')
@app.route('/save', methods=['POST','GET'])
def save():
    # if statement to check if the following actions are met
    if request.method =='POST':
        Destination=request.form['Destination']
        Departure=request.form['Departure']
        Date=request.form['Date']
        Time=request.form['Time']
        # connect to server and database
        con=pymysql.connect(host='localhost',user='root',password='',database='booking_git')
        cursor=con.cursor()
        sql='INSERT INTO booking1 (Destination,Departure,Date,Time) VALUES(%s,%s,%s,%s)'
        cursor.execute(sql,(Destination,Departure,Date,Time))
        con.commit()
        return render_template('add.html',msg='Saved Successfully')
    else:
        return render_template('add.html')
app.run(debug=True)