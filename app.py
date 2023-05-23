from dash import Dash, dcc, html, Input, Output, callback


app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.Div('Frist Div'),
    html.Div('Second Div'),
])

app.run_server(debug=False)