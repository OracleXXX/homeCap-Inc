from flask import Blueprint, render_template

blue = Blueprint('blueContactUs', __name__)



@blue.route('/contactus')
def index():
    title = '联系我们'
    return render_template( 'ContactUs.html', title=title)