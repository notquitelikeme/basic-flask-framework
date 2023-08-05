import pymysql
from flask import *
app=Flask(__name__)
@app.route('/fetch')
def all():
    # connect to the database
    con=pymysql.connect(host='localhost',user='root',password='',database='booking_git')
    # create cursor to execute sql query
    cursor=con.cursor()
    cursor.execute('SELECT * FROM booking1')
    # fetch all the records in the table
    rows=cursor.fetchall()
    return render_template('fetch.html',rows=rows)
app.run(debug=True)
