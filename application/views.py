from flask import render_template

from application import app
from application.decorators import login_required

@login_required
def index():
    return render_template('index.html', msg="Hello World!")

