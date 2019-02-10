import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np
import pandas as pd

df = pd.read_csv('finalBats.csv')
df1 = pd.read_csv('finalBatsSR.csv')

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id='scatter-chartdf',
        figure = {
            'data': [
                     {'x':df.Player, 'y':df.RohitSharma , 'type':'line', 'name': 'RohitSharma'},
                     {'x':df.Player, 'y':df.ShaneWatson , 'type':'line', 'name': 'ShaneWatson'},
                     {'x':df.Player, 'y':df.ViratKohli , 'type':'line', 'name': 'ViratKohli'},
                     {'x':df.Player, 'y':df.ABdeVilliers , 'type':'line', 'name': 'ABdeVilliers'},
                     {'x':df.Player, 'y':df.SureshRaina , 'type':'line', 'name': 'SureshRaina'},
                     {'x':df.Player, 'y':df.MSDhoni , 'type':'line', 'name': 'MSDhoni'},
                 ],

        'layout': go.Layout(
            title = 'Season-wise Runs Scored by Batsmen',
            xaxis = {'title':'IPL year'},
            yaxis = {'title':'Runs scored in Seasons'}
            )
         }
        )
,
    dcc.Graph(
        id='scatter-chartdf1',
        figure = {
            'data': [
                     {'x':df1.Player, 'y':df1.RohitSharma , 'type':'line', 'name': 'RohitSharma'},
                     {'x':df1.Player, 'y':df1.ShaneWatson , 'type':'line', 'name': 'ShaneWatson'},
                     {'x':df1.Player, 'y':df1.ViratKohli , 'type':'line', 'name': 'ViratKohli'},
                     {'x':df1.Player, 'y':df1.ABdeVilliers , 'type':'line', 'name': 'ABdeVilliers'},
                     {'x':df1.Player, 'y':df1.SureshRaina , 'type':'line', 'name': 'SureshRaina'},
                     {'x':df1.Player, 'y':df1.MSDhoni , 'type':'line', 'name': 'MSDhoni'},
                 ],

        'layout': go.Layout(
            title = 'Season-wise Strike Rate Scored by Batsmen',
            xaxis = {'title':'IPL year'},
            yaxis = {'title':'Strike Rate of all Seasons'}
            )
         }
        )

    
    ])


if __name__ == '__main__':
    app.run_server(debug=True)


