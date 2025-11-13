from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('menu.html')

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

@app.route('/submit')
def submit():
    return render_template("submit.html")

if __name__ == '__main__':
    app.run(debug=True)






