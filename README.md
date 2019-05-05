# Data-Visualization
This project show the visualization of output variable of the selected dataset. User will be able to select a dataset from available datasets on User Interface. This project was developed with the help of Python 3 and Flask Framework. Webpages are developed with the help of HTML.
# Getting Started
To get started with this project User have to install Python and some libraries on their System.
Some required libraries are - Flask, Bokeh, Pandas, Numpy and Scikit-learn.

## Python
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python supports modules and packages, which encourages program modularity and code reuse.

For downloading Python 3 interpretor [click here](https://www.python.org/downloads/).

Next, install the Python interpreter on your computer.

## Flask
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

## Pandas
Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

To get Started with Pandas, start with the [User Guide](https://pandas.pydata.org/).
To install or Update using pip as follows:

`pip install -U pandas`

## Numpy
NumPy is the fundamental package for scientific computing with Python. It contains among other things:

+ a powerful N-dimensional array object
+ sophisticated (broadcasting) functions
+ tools for integrating C/C++ and Fortran code
+ useful linear algebra, Fourier transform, and random number capabilities

For a quick introduction to NumPy we provide the [NumPy Tutorial](https://www.numpy.org/devdocs/user/quickstart.html). 
To install or Update using pip as follows:

`pip install -U numpy`

## Scikit-learn
Scikit-learn (formerly scikits.learn) is a free software machine learning library for the Python programming language.[3] It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.
To get started using Scikit-learn to make your visualizations, start with the [User Guide](https://scikit-learn.org/stable/).
To install or Update using pip as follows:

`pip install -U scikit-learn`

# Run :

+ Open Command Prompt and go to Project directory using `pip` command

+ Create a virtual environment and activate the virtual environment. For any help visit [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

+ Install required packages of Python using `pip`.

+ Now Run following commands :

    On Windows Platform:

```

    set FLASK_APP = name.py

    set FLASK_DEBUG = True

    flask run

```

For Mac Platform you can take help from [here](http://flask.pocoo.org/docs/1.0/cli/).

Here name is name of flask python file with extension. 

After these command you will se that you server is running.

+ Now you can test you application on given localhost address or `http://localhost:5000/`

# Deployment on Heroku

For deployment on heroku 

+ You need to download the Heroku CLI which will enable us deploy and manage our application. Make sure that heroku is installed on your system, if you want to install then follow this [link](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

+ After installation login into the Heroku Cli by running this command in the terminal.

``` 
 heroku login
```

+ Go to [Heroku](https://www.heroku.com/) then login or signup into heroku.

+ You will be prompted to enter your email address and password. You will only be logged in if these details match the credentials you signed up with on the Heroku platform.

+ We are going to deploy the API application I developed and wrote about in this post, though you can follow along with your own application.

+ Let us start by cloning the application. Open the terminal and paste in this command to clone the application. A gentle reminder that this step will only work if you have [Git](https://git-scm.com/downloads) installed on your computer.

```

git clone https://github.com/kishan77903/Data-Visualization

```

+ Open the folder Data-Visualization with your favorite text editor or IDE. Create a virtual environment and install the dependencies by running. 

```
pip install -r requirements.txt
```

Note: if you are using your own application, make sure you have added a requirements.txt file by running `pip freeze > requirements.txt` so that all the application dependencies are added.

+ ### Adding a Procfile:

    In order for us to successfully deploy any application to Heroku, we must add a Procfile to that application.

    Before we can add a Procfile, we need to first install a web server called Gunicorn. Run the following command within the               application folder.

    ` pip install gunicorn `

    Create a new file with Procfile as the name and do not add any extension. Add this line below.

    `web: gunicorn main_flask:app`

    `web` is used by Heroku to start a web server for the application. The `main_flask`:app specifies the module and application name.       In our application we have the `main_flask` module and our flask application is also called app. If your’s are different you can         change them.

+ We are now ready to deploy our application. In the application folder run:

    `heroku create data-visualization`

   `data-visualization` is the name of the application, this has to be unique across Heroku. So change it to yours otherwise you will be    unable to deploy.

+ The output of that command will be similar to this below. Take note of the application URL because it is where your app lives.

```
    Creating kbucket-api-heroku... done
    https://data-visualization.herokuapp.com/ | https://git.heroku.com/data-visualization.git
```

+ Now We have to push our application to the master branch of the above git URL.

    `git push heroku master `

# Congratulations 

You have successfully deployed your project on heroku. You can now share the link with others to view your Application.
