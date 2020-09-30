from flask import Blueprint, render_template

blue = Blueprint('blueContactUs', __name__)



@blue.route('/contactus')
def index():
    return render_template( 'ContactUs.html' )