from flask import render_template, Blueprint

site = Blueprint('site', __name__)

@site.route('/')
def home():
    return render_template('home.html')