from flask import Blueprint, render_template

blue = Blueprint('blueRESource', __name__)



@blue.route('/re_source')
def index():
    return render_template( 'RESource.html' )