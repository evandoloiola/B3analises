# -*- coding: utf-8 -*-
#dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from DatabaseConnect import Database as Dt
#connect to data base
data = Dt()
df = data.read_sql("SELECT `Fundo`,`Data`,`Variação` FROM `fundos` WHERE `Fundo` LIKE '%Equitas%'")
#css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#tabela
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

#layout

app.layout = html.Div(children=[
    html.H1(children='Aplicativo de Fundos'),

    html.Div(children='''
        FundosApp: Compare os diversos fundos.
    '''),
    html.Div(
    dcc.Dropdown(
        options = [
            {'label':'Amarelo', 'value':'am'},
            {'label':'Verde', 'value':'vd'}
        ]
    )
    ),
    dcc.Graph(
        id = 'teste', 
        figure={
            'data': [
                {'x':df['Data'], 'y':df['Variação'], 'type':'scatter','name':'Fundos'}
            ]
        }
    ),
    html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)])
    
])


if __name__ == '__main__':
    app.run_server(debug=True)