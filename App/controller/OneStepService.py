from flask import Blueprint, render_template

blue = Blueprint('blueOneStepService', __name__)



@blue.route('/onestep/service')
def index():
    return render_template( 'OneStepService.html' )