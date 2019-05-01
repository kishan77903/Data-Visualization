from flask import Flask,render_template,request
from sklearn import datasets
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/visualize")
def visualize():
    return render_template("visualize.html")

@app.route("/selectfeatures",methods=["GET","POST"])
def selectfeatures():
    filename=request.form['option']
    if filename == 'breastcancer':
        t = 'breastcancer'
    elif filename == 'iris':
        t='iris'
    elif filename == 'diabetes':
        t='diabetes'
    elif filename == 'digits':
        t='digits'
    elif filename == 'linnerud':
        t = 'linnerud'
    elif filename == 'wine':
        t='wine'
    else :
        t='houseprices'
    return t
    

if __name__ == '__main_flask__':
    app.run(debug=True)