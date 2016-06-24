
from flask import Flask, jsonify, render_template, request
from flask import Markup
app = Flask(__name__)
import json
import plotly
from plotly.offline import plot

import pandas as p
import numpy as np
import pkg_resources   

@app.route('/hello')
def hello():
    return render_template('basic__plot.html')

@app.route('/', methods=['POST'])
def my_form_post():
    print("Hi ")
    text = request.form['text']
    start_time = request.form['from_time']
    end_time =request.form['to_time']
    start_count = request.form['from_count']
    end_count =request.form['to_count']
    
    if not text:
      return render_template("welcome.html");

    text="datasets/"+text
    light_curve = pkg_resources.resource_stream(__name__,text)
    data = np.loadtxt(light_curve)
    Time = data[0:len(data),0]
    Rate = data[0:len(data),1]
    Error= data[0:len(data),2]
    

    import sys
    import os
    from plotly import session, tools, utils
    import uuid
    import json

   

    trace1 = dict(
            type = 'scatter',
            x=Time,
            y=Rate,
            error_y=dict(
               type='data',
               array=Error,
               visible=True
                )

    )
    
    layout=dict(
                 title='',
                 xaxis=dict(
                     title='Time',
                     range=[start_time,end_time],
                     rangeslider=dict(),
                     titlefont=dict(
                     family='Courier New, monospace',
                     size=18,
                     color='#7f7f7f'
                        )
                 ),
                 yaxis=dict(
                     title='Count Rate',
                     range=[start_count,end_count],
                     titlefont=dict(    
                     family='Courier New, monospace',
                     size=18,
                     #range=[int(start), int(end)],
                     #range=[10,20],
                     color='#7f7f7f'    
                      )
                 )
        )
    fig = dict(data = [trace1], layout = layout)
    my_plot_div=plot(fig, output_type='div')
   # print(my_plot_div)
    return render_template('index.html',
                               div_placeholder= Markup(my_plot_div)
                              )




@app.route('/')
def my_form():
    print("I am here")
    return render_template("welcome.html")



if __name__ == '__main__':
    app.run()