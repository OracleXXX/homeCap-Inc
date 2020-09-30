from flask import Blueprint, render_template

blue = Blueprint('blueOurTeam', __name__)



@blue.route('/ourteam')
def index():
    title='团队背景'
    return render_template( 'OurTeam.html', title=title )