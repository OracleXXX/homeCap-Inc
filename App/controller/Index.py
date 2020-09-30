from flask import Blueprint, render_template

blue = Blueprint( 'blueIndex', __name__ )


@blue.route( '/index', methods = ['GET', 'POST'] )
def index():
    title = '主页'
    return render_template( 'index.html', title=title )
