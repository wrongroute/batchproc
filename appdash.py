import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
from dash.dependencies import Input, Output

df = pd.read_csv('valueslist.csv')

external_stylesheets = ['/static/smallcss.css']#'https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(className="o-div", children=[
    html.Nav(className="nav nav-pills", children=[
            html.Div(className="w-div", children=[
                html.Img(src="/static/parkin.png", className="logo"),
                html.A('S-parking', className="titlelink", href='/'),
                dcc.Tabs(id="tabs", value='tab-1', children=[
                    dcc.Tab(label='Эвакуированные авто', value='tab-1'),
                    dcc.Tab(label='Tab two', value='tab-2'),
                    dcc.Tab(label='Tab three', value='tab-3')
                ]),

                ]
            )
        ]
    ),
    html.Div(className="cont-div", children=[
    html.Div(id='tabs-content')
    ])])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])

def render_content(tab):
    if tab == 'tab-1':
        return html.Div(children=[html.H3(className="info-m", children='Эвакуированные автомобили города Сочи'),
            html.Div(className="data-div", children=[dash_table.DataTable(data=df.to_dict('records'),
                id='datatable-interactivity',
                columns=[{'id': c, 'name': c} for c in df.columns],
                filter_action="native",
                page_action="native",
                page_current= 0,
                page_size= 50,
                style_header={
                    'fontWeight': 'bold'
                    },
                style_cell_conditional=[
                    {
                    'font-family': 'Open Sans, HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif',
                    'font-size': '16px',
                    'text-align': 'center'
                    }
                ]
            ),
            html.Div(id='datatable-interactivity-container')
            ]
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
