from flask import Blueprint, render_template

blue = Blueprint('blueRESource', __name__)



@blue.route('/re_source')
def index():
    title = '精选房源'
    return render_template( 'RESource.html', title=title )