from flask import Blueprint, render_template

blue = Blueprint('blueOneStepTrade', __name__)



@blue.route('/onestep/trade')
def index():
    return render_template( 'OneStepTrade.html' )