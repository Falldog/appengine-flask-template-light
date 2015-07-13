from flask import Flask

# global app of flask, import application to get app instance
app = Flask(__name__)

import urls
import views
import filters

