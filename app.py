"""
By Shai Shterzer
November 2025-X
"""

import json
import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('menu.html')

@app.route('/menu/form')
def menu_form():
    return render_template('form_menu.html')

@app.route('/international/adult/form')
def international_adult():
    return render_template("form_international_adult.html")

@app.route('/national/adult/form')
def national_adult():
    return render_template("form_national_adult.html")

@app.route('/international/child/form')
def international_child():
    return render_template("form_international_child.html")

@app.route('/national/child/form')
def national_child():
    return render_template("form_national_child.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/submit', methods=['POST'])
def submit_form():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']

    # Check if file exists
    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
    else:
        data = []

    # Add the new registration
    data.append({'first_name': first_name, 'last_name': last_name, 'age': age})

    # Save all registrations back to the file
    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    return redirect(url_for('menu_form'))


if __name__ == '__main__':
    app.run(debug=True)






