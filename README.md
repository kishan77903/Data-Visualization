# Data-Visualization
This project show the visualization of output variable of the selected dataset. User will be able to select a dataset from available datasets on User Interface. This project was developed with the help of Python 3 and Flask Framework. Webpages are developed with the help of HTML.
# Getting Started
To get started with this project User have to install Python and some libraries on their System.
Some required libraries are - Flask, Bokeh, Pandas, Numpy and Scikit-learn.

# Python
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python supports modules and packages, which encourages program modularity and code reuse.

For downloading Python 3 interpretor [click here](https://www.python.org/downloads/).

Next, install the Python interpreter on your computer.

# Flask
Flask is a micro web framework powered by Python. Its API is fairly small, making it easy to learn and simple to use. Flask is a lightweight [WSGI](https://wsgi.readthedocs.io/en/latest/) web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around [Werkzeug](https://www.palletsprojects.com/p/werkzeug/) and [Jinja](https://www.palletsprojects.com/p/jinja/) and has become one of the most popular Python web application frameworks.

Flask can be installed or updated by [pip](https://pip.pypa.io/en/stable/quickstart/):

`pip install -U Flask`

To get Started with Flask, start with the [User Guide](http://flask.pocoo.org/docs/0.12/) or [Video tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH).

Simple example of Flask is shown below:

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
```
Run the file on Windows command Prompt as follows:

```
$ set FLASK_APP=hello.py flask run
 * Serving Flask app "hello"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

# Bokeh
Bokeh is an interactive visualization library that targets modern web browsers for presentation. Its goal is to provide elegant, concise construction of versatile graphics, and to extend this capability with high-performance interactivity over very large or streaming datasets. Bokeh can help anyone who would like to quickly and easily create interactive plots, dashboards, and data applications.

To get started using Bokeh to make your visualizations, start with the [User Guide](https://bokeh.pydata.org/en/latest/docs/user_guide.html#userguide).
To install or Update using pip as follows:

`pip install -U bokeh`

# Pandas
Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

To get Started with Pandas, start with the [User Guide](https://pandas.pydata.org/).
To install or Update using pip as follows:

`pip install -U pandas`

# Numpy
NumPy is the fundamental package for scientific computing with Python. It contains among other things:

+ a powerful N-dimensional array object
+ sophisticated (broadcasting) functions
+ tools for integrating C/C++ and Fortran code
+ useful linear algebra, Fourier transform, and random number capabilities

For a quick introduction to NumPy we provide the [NumPy Tutorial](https://www.numpy.org/devdocs/user/quickstart.html). 
To install or Update using pip as follows:

`pip install -U numpy`

# Scikit-learn
Scikit-learn (formerly scikits.learn) is a free software machine learning library for the Python programming language.[3] It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.
To get started using Scikit-learn to make your visualizations, start with the [User Guide](https://scikit-learn.org/stable/).
To install or Update using pip as follows:

`pip install -U scikit-learn`
