# flask is a framework that allows access to flask python features
# from flask import* (everything)
from flask import *
import pymysql
#routing
app=Flask(__name__)
@app.route('/')
def hello():
    return 'Hello there, we are python developers'

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