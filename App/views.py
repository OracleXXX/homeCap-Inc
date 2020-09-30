from flask import Blueprint, render_template

blue = Blueprint('blueHello', __name__)

@blue.route('/')
def hello():
    return render_template('hello.html')


