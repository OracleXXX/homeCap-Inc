from flask import Blueprint, render_template

blue = Blueprint('bluePersonalLoan', __name__)



@blue.route('/personalloan')
def index():
    title='房屋个人贷款'
    return render_template( 'PersonalLoan.html', title=title )