from flask import Flask, render_template,request
import pymysql

app = Flask(__name__)

# Database connection
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='#Ka402522',
                             database='user_registration',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    try:
        with connection.cursor() as cursor:
            # Insert user data into database
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, email, password))
            connection.commit()
            return 'Registration successful!'
    except Exception as e:
        return 'Error: ' + str(e)

@app.route('/users')
def users():
    try:
        with connection.cursor() as cursor:
            # Fetch all users from the database
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            users = cursor.fetchall()
            return render_template('users.html', users=users)
    except Exception as e:
        return 'Error: ' + str(e)

if __name__ == '__main__':
    app.run(debug=True)
