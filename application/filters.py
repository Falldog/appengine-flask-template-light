from application import app

@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]
# app.jinja_env.filters['reverse'] = reverse_filte

