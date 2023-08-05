from flask import *
import pymysql
# create a registration (signup) form python code
# route
app=Flask(__name__)
@app.route('/')
def main():
    return 'This is the main route'
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
        return 'Saved Successfully'
    else:
        return render_template('signup.html')
app.run(debug=True)