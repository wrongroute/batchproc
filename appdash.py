import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
from dash.dependencies import Input, Output
from dash.development.base_component import Component, _explicitize_args



df = pd.read_csv('valueslist.csv')
#first graph
dates = df.Дата.unique()
groupdate = df.groupby('Дата').count()
countsdate = groupdate.Номер.values
#second graph
sources = df.Источник.unique()
groupsource = df.groupby('Источник').count()
countssource = groupsource.Номер.values
vcountssource = [i for i in countssource if i > 3]
#third
targets = df.Штрафстоянка.unique()
grouptarget = df.groupby('Штрафстоянка').count()
countstarget = grouptarget.Номер.values

external_stylesheets = ['/static/smallcss.css']#'https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(className="o-div", children=[
    html.Nav(className="nav nav-pills", children=[
            html.Div(className="w-div", children=[
                html.Img(src="/static/parkin.png", className="logo"),
                html.A('S-parking', className="titlelink", href='/'),
                dcc.Tabs(id="tabs", value='tab-1', children=[
                    dcc.Tab(label='Эвакуированные авто', value='tab-1'),
                    dcc.Tab(label='Статистика эвакуаций', value='tab-2'),
                    dcc.Tab(label='Общественные парковки', value='tab-3')
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
            html.Div(className="data-div", children=[dash_table.DataTable(data=df.sort_values(by=['Дата', 'Время'], ascending=False).to_dict('records'),
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

    if tab == 'tab-2':
        return html.Div(children=[html.H3(className="info-m", children='Статистика автомобильных эвакуаций в городе Сочи'),
            html.Div(className="data-div", children=[
    dcc.Graph(
        figure=dict(
            data=[
                dict(
                    x=[i for i in dates],
                    y=[i for i in countsdate],
                    name='За последние 10 дней',
                    marker=dict(color='rgb(55, 83, 109)')
                )
            ],
            layout=dict(
                title='Количество эвакуаций в день',
                showlegend=True,
                legend=dict(
                    x=0,
                    y=0
                ),
                margin=dict(l=40, r=20, t=80, b=30)
        )
    ),
        style={'height': 400, 'weight': '100%'},
                id='my-graph'
        ),

                dcc.Graph(
                    figure=dict(
                        data=[
                            dict(
                                # autosize=True,
                                type="pie",
                                labels=[i for i in sources],
                                values=[i for i in vcountssource],
                                name="Sources",
                                title={'text': "Активность по улицам",
                                       'y': 1,
                                       'x': 1,
                                       },
                                # title='Количество эвакуаций по улицам',
                                hoverinfo="label+value",
                                textinfo="label",
                                hole=0.5,
                                plot_bgcolor="white",
                                marker=dict(colors=["#fac1b7", "#a9bb95", "#92d8d8"]),
                                domain={"x": [0.5, 0.45], "y": [1.5, 1.5]},
                                margin=dict(l=0, r=20, b=0, t=80),
                                titlefont=dict(size=20),
                            )
                        ]
                    ),
                    style={'height': 600, 'weight': '100%', 'font-size': 20},
                    id='my-pie'
                ),

                dcc.Graph(
                    figure=dict(
                        data=[
                            dict(
                                #autosize=True,
                                type="pie",
                                labels=[i for i in targets],
                                values=[i for i in countstarget],
                                name="Targets",
                                title={'text': "Активность по штрафстоянкам",
                                       'y': 1,
                                       'x': 1,
                                       },
                                # title='Количество эвакуаций по улицам',
                                hoverinfo="label+value",
                                textinfo="label",
                                hole=0.65,
                                plot_bgcolor="white",
                                marker=dict(colors=["#fac1b7", "#a9bb95", "#92d8d8"]),
                                domain={"x": [0.5, 0.45], "y": [1.5, 1.5]},
                                margin=dict(l=0, r=20, b=0, t=80),
                                titlefont=dict(size=20)
                            )
                        ]
                    ),
                    style={'height': 600, 'weight': '100%', 'font-size': 20},
                    id='my-pie2'
                )


    ])]
    )

    if tab == 'tab-3':
        return html.Div(
               html.Iframe(src="https://yandex.ru/map-widget/v1/-/CGxQJ0--",
                width="90%",
                height="1000",
            )
        )



if __name__ == '__main__':
    app.run_server(debug=True)
