from flask import Blueprint, render_template

blue = Blueprint('blueOneStepService', __name__)



@blue.route('/onestep/service')
def index():
    title= '一站式房屋管理'
    return render_template( 'OneStepService.html', title=title )