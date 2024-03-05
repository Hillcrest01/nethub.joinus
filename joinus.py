from flask import Flask, render_template, request, app
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Kulundeng.Jamach.1'
app.config['MYSQL_DB'] = 'nethub'

mysql = MySQL(app)

@app.route('/', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        userDetails = request.form
        username = userDetails['username']
        email = userDetails['email']
        phone = userDetails['phone']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, email, phone, password) VALUES(%s, %s, %s, %s)",(username, email, phone, password))
        mysql.connection.commit()
        cur.close()
        return render_template('home.html')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)