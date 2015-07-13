from flask import redirect
from functools import wraps
from google.appengine.api import users


def login_required(func, redirect_url='/'):
    @wraps(func)
    def new_func(*argv, **argd):
        user = users.get_current_user()
        if user:
            return func(*argv, **argd)
        else:
            return redirect(users.create_login_url(redirect_url))
    return new_func

