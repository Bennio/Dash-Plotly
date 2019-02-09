import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

df = [{'x':[1,2,3,4,5], 'y':[1,4,9,16,25] , 'type':'line', 'name':'boats'},
                         {'x':[5,4,3,2,1], 'y':[9,8,7,6,5] , 'type':'bar', 'name':'cars'},
   ]

''' dict = [{'x': ['abhi','lovee','ishu','mouli'],
		'y': [19,21,14,13],
                'type':'bar', 'name':'details',
		}]'''

app.layout = html.Div(children=[
    html.H1('IPL Visualizations'),
    dcc.Graph(id='example',
             figure={
                 'data':df
                      ,    
                 'layout': {
                     'title': 'ipl simple plotting'
                 }
                 
             })
])

if __name__ == '__main__':
    app.run_server(debug=True)
