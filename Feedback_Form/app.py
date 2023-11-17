from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os
# import csv

current_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        
        fname = request.form['fname']
        lname = request.form['lname']
        country = request.form['country']
        email = request.form['email']
        feedback_type = request.form['feedbacktype']
        feedback = request.form['feedback']
        
        # Store data in sqlite3
        connection = sqlite3.connect(current_dir+"\Feedback.db")
        cursor = connection.cursor()
        query2 = "INSERT INTO feedback VALUES('{fname}','{lname}','{email}','{country}','{feedback_type}','{feedback}')"
        cursor.execute(query2)
        connection.commit()
        
        # Store data in csv file
        # with open('feedback.csv','a') as f:
        #     f.write(f"'Name': {name}, 'Country': {country}, 'Email': {email}, 'feedback'={feedback}\n")
        
        return render_template('submitted.html', 
                               fname = fname, 
                               lname = lname, 
                               country = country, 
                               email = email, 
                               feedback_type = feedback_type, 
                               feedback = feedback)
    else: 
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)