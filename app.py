from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import numpy as np
import mysql.connector
from sklearn.cluster import KMeans as kmeans
from sklearn.preprocessing import StandardScaler as scaler
import bcrypt
import pickle
import matplotlib.pyplot as plt
import io

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database connection configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'nithin'
DB_NAME = 'bookmytrain'

# Database connection helper function
def query_db(query, args=(), one=False):
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cur = conn.cursor(dictionary=True)
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# Home route
@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Simulate a query for demonstration purposes (replace with actual database query logic)
        user = query_db("SELECT * FROM Users WHERE username = %s", (email), one=True)

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            session['email'] = user['email']
            return redirect(url_for('home'))
        else:
            # Pass error message to the template
            return render_template('login.html', message="Invalid Username or Password", is_error=True)

    # Render the login page without a message
    return render_template('login.html', message=None, is_error=False)


# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']

        # Hash password
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert user into database
        conn = mysql.connector.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
        )
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Users (username, email,phone_number, password_hash) VALUES (%s, %s, %s,%s)",
                (username, email,phone, password_hash.decode('utf-8')),
            )
            conn.commit()
            conn.close()
            return render_template('signup.html', message="Signup successful! Login here", is_error=False)
        except mysql.connector.Error as err:
            conn.close()
            return render_template('signup.html', message=f"Error: {err}", is_error=True)

    return render_template('signup.html')


# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
# Route to display profile page
@app.route('/profile', methods=['GET'])
def profile():
    # Check if the user is logged in
    if 'username' not in session:
        return redirect(url_for('login'))

    # Fetch user details from the database
    username = session['username']
    user_details = query_db("SELECT * FROM Users WHERE username = %s", (username,), one=True)

    if user_details:
        return render_template('profile.html', user_details=user_details)
    else:
        return "User details not found.", 404

# Route to handle editing preferences

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
