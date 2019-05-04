from flask import Flask,render_template,request
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import os


app = Flask(__name__, static_folder = "static")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/visualize",methods=["GET","POST"])
def visualize():
    
    try:
        filename=request.form['option']
        if filename == 'breastcancer':
            data = datasets.load_breast_cancer()
            x_label = "Classes"
            y_label = "Count"
        elif filename == 'iris':
            data = datasets.load_iris()
            x_label = "Classes"
            y_label = "Count"
        elif filename == 'diabetes':
            data = datasets.load_diabetes()
            x_label = "quantitative measure of disease progression one year after baseline"
            y_label = "Count"
        elif filename == 'wine':
            data = datasets.load_wine()
            x_label = "Classes"
            y_label = "Count"
        elif filename == "houseprice" :
            data = datasets.load_boston()
            x_label = "Price values"
            y_label = "value Counts"

        df = pd.DataFrame(data.data,columns=data.feature_names)
        df['target'] = pd.Series(data.target)
    except:
        file = request.files['csvfile']
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        filename_path = os.path.join(THIS_FOLDER, "data.csv")
        file.save(filename_path)
        df = pd.read_csv(filename_path, encoding='cp1252')
        df['target'] = df[df.columns[len(df.columns)-1]]
        x_label = "Counts"
        y_label = df.columns[len(df.columns)-1]
    plt.clf()
    if (len(df['target'].unique().tolist()) > int(0.1 * len(df['target']))):    
        fig = plt.hist(df['target'])
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title("Histogram of Output variable for selected Dataset")
    else:
        value_count = {}
        for each in df['target'].unique():
            value_count[each] = len(df[df['target']==each])
        fig = plt.pie(value_count.values(),labels=value_count.keys(), autopct='%1.1f%%')
        plt.title("Pie Chart of Output Classes for selected Dataset")
    os.remove("static/Visual.jpg")
    plt.savefig("static/Visual.jpg");
    return render_template("visualize.html")

    

if __name__ == '__main_flask__':
    app.run(debug=True)
