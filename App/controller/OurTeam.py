from flask import Blueprint, render_template

blue = Blueprint('blueOurTeam', __name__)



@blue.route('/ourteam')
def index():
    return render_template( 'OurTeam.html' )