import pandas_datareader.data as web
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies  import Input, Output

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime.now()

stocks = 'NTNX'

df = web.DataReader(stocks, 'yahoo', start, end)
#print(df.tail(10))

app = dash.Dash()

app.layout = html.Div(children=[
         html.H3(children='''
            Symbol to graph:
        '''),

         dcc.Graph(
        id='example-graph',
             figure={
                 'data': [
                     {'x':df.index, 'y':df.Close , 'type':'line', 'name': stocks},
                 ],
                 
                 'layout': {
                     'title': stocks

                 }

             }

         )
    
])


if __name__ == '__main__':
    app.run_server(debug=True)
