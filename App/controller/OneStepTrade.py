from flask import Blueprint, render_template

blue = Blueprint('blueOneStepTrade', __name__)



@blue.route('/onestep/trade')
def index():
    title = '一站式房屋买卖'
    return render_template( 'OneStepTrade.html', title=title )