import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np
import pandas as pd

df = pd.read_excel('IPL2008.xls')

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id='scatter-chart',
        figure = {
            'data': [
                     {'x':df.Runs, 'y':df.Balls , 'type':'line', 'name': 'sr'},
                 ],

        'layout': go.Layout(
            title = 'Plots of ipl datasets',
            xaxis = {'title':'Runs'},
            yaxis = {'title':'Balls'}
            )
         }
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)


