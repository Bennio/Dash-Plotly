import pandas_datareader.data as web
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies  import Input, Output

app = dash.Dash()

app.layout = html.Div([

    html.H3('ipl dataset'),

    html.Dropdown(
        id='my-dropdown',
        options = [
            {'label':'bat', 'value':''},
            {'label':'bat', 'value':''},
            {'label':'bat', 'value':''},
            ],
        value=''
        ),

    dcc.Graph(id='my-graph')

    ])

@app.react('my-graph', ['my-dropdown'])

def update_graph(dropdown_properties):
    selected_values = dropdown_properties['value']

    df = pd.read_excel('IPL2008.xls')

    return {
        'figure':go.Figure(
            data=[
                scatter(
                    x=df.Runs,
                    y=df.Balls,
                    names=selected_values
                    )
                ]
            )
        }

if __name__ == '__main__':
    app.run_server(debug=True)

