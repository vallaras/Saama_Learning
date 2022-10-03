from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash

app = Dash(__name__)




df = pd.read_csv("laptops.csv",encoding='latin-1')

fig = px.bar(df, x="Company", y="Ram", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Laptops'),

    html.Div(children='''
        Dash: A web application framework for your Laptop_datas.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
