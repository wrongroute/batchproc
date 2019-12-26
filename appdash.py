import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table

df = pd.read_csv('valueslist.csv')

external_stylesheets = ['/static/smallcss.css']#'https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(className="o-div", children=[
    html.Nav(className="nav nav-pills", children=[
            html.Div(className="w-div", children=[
            html.Img(src="/static/parkin.png", className="logo"),
            html.A('S-parking', className="titlelink", href='/'),
            html.A('Статистика', className="nav-link-btn", href='/stat'),
            html.A('Сведения', className="nav-link-btn", href='/')
    ])]),
            html.Div(className="cont-div", children=[
            html.H3(className="info-m", children='Эвакуированные автомобили Сочи'),
            html.Div(className="data-div", children=[dash_table.DataTable(data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
                style_cell_conditional=[
                    {
                    'font-family': 'Open Sans, HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif'
                    }
                ]
            )
            ])
    ])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
