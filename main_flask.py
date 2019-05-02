from flask import Flask,render_template,request
from sklearn import datasets
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from bokeh.plotting import figure,output_file
from bokeh.io import save
from bokeh.models import Title
from math import pi
from bokeh.transform import cumsum
from bokeh.palettes import viridis

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/visualize",methods=["GET","POST"])
def visualize():
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
    else :
        data = datasets.load_boston()
        x_label = "Price values"
        y_label = "value Counts"
    df = pd.DataFrame(data.data,columns=data.feature_names)
    df['target'] = pd.Series(data.target) 
    p = figure(plot_width=400, plot_height=400,toolbar_location=None)
    if (len(df['target'].unique().tolist()) > int(0.1 * len(df['target']))):
        hist, edges = np.histogram(data['target'][:], density=True, bins=50)
        p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], line_color="white")
        
        p.add_layout(Title(text=x_label, align="center"), "below")
        p.add_layout(Title(text=y_label, align="center"), "left")
    else:
        value_count = {}
        for each in df['target'].unique():
            value_count[each] = len(df[df['target']==each])
        data_value = pd.Series(value_count).reset_index(name='value').rename(columns={'index':'country'})
        data_value['angle'] = data_value['value']/data_value['value'].sum() * 2*pi
        data_value['color'] = viridis(len(df['target'].unique()))
        p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))
        p.wedge(x=0, y=1, radius=0.4,start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),line_color="white", fill_color='color', legend='country', source=data_value)

    output_file('templates/visual.html',title = "Plot")
    save(p)
    return render_template('visual.html')

if __name__ == '__main_flask__':
    app.run(debug=True)