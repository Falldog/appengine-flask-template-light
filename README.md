## appengine-flask-template-light
A light template for creating new Python Flask web framework on Google App Engine


## Flask version
0.10.1


## Application Layout
* [Flask - Simple Packages](http://flask.pocoo.org/docs/0.10/patterns/packages/#simple-packages)


## Usage
* clone repo to your local

```
$ git clone https://github.com/Falldog/appengine-flask-template-light.git
```

* install require library to `lib` folder, note that it will install packages into `lib` and jinja2 will installed too

```
$ cd appengine-flask-template-light
$ pip install -r requirements.txt -t lib
```

* run appengine dev server on specific port

```
$ dev_appserver.py --admin_port=8000 --port=8080 .
```

* browse application on [http://localhost:8080](http://localhost:8080)


