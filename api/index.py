'''
My python app
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    '''Home route'''
    return render_template('hello.html')

@app.route('/about')
def about():
    '''About page'''
    return 'hullabulla'
