from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Homepage!"

@app.route('/about')
def about():
    return "This is the About Page."

@app.route('/contact')
def contact():
    return "Contact us at: info@example.com."

if __name__ == '__main__':
    app.run(debug=True)



