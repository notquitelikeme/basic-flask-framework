import pymysql
from flask import *
app=Flask(__name__)
@app.route('/transaction',methods=['POST','GET'])
def transaction():
    if request.method=='POST':
        Name=request.form['Name']
        Email=request.form['Email']
        Phone=request.form['Phone']
        con=pymysql.connect(host='localhost',user='root',password='',database='Mpesa')
        cursor=con.cursor()
        sql='INSERT INTO transactions(Name,Email,Phone) VALUES(%s,%s,%s)'
        cursor.execute(sql,(Name,Email,Phone))
        con.commit()
        return render_template('transaction.html',msg='Details saved successfully')
    else:
        return render_template('transaction.html',msg='Invalid details. Please try again')
app.run(debug=True)