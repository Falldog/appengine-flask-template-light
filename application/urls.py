from application import app
from application import views

app.add_url_rule('/', 'index', views.index)

