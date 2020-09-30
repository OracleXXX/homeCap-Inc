from flask import Flask
from flask_script import Manager

from App.views import blue as hello
from App.controller.Index import blue as index
from App.controller.ContactUs import blue as contact_us
from App.controller.OneStepService import blue as one_step_serveice
from App.controller.OneStepTrade import blue as one_step_trade
from App.controller.OurTeam import blue as our_team
from App.controller.RESource import blue as RE_source
from App.controller.PersonalLoan import blue as personal_loan
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.register_blueprint(blueprint=hello)
app.register_blueprint(blueprint=index)
app.register_blueprint(blueprint=contact_us)
app.register_blueprint(blueprint=one_step_serveice)
app.register_blueprint(blueprint=one_step_trade)
app.register_blueprint(blueprint=our_team)
app.register_blueprint(blueprint=RE_source)
app.register_blueprint(blueprint=personal_loan)
bootstrap = Bootstrap(app=app)

manager = Manager(app=app)


if __name__ == '__main__':
    manager.run()