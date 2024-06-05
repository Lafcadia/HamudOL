from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About'

@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")
