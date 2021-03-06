from dash_package.dash_queries import *
import dash
from dash.dependencies import Input, Output



app.layout = html.Div([
    html.H1('NYC Crime Data - 1H 2018'),
    html.Div([
        html.H2('Crime by Level of Offense & Offense Description Graph'),
        dcc.Tabs(id="tabs", children=[
            dcc.Tab(id='NYC', label='Crimes by Borough',
                children=[
                dcc.Graph(figure=
                {'data': crime_graph_creator()+crime_graph_all_boroughs(boroughs,month_names),
                'layout': {'title':'All Complaints'},
                })
                ]
            ),
            dcc.Tab(id='Felony', label='Felony Complaints',
                children=[
                dcc.Graph(figure=generalDashWrapper('level','Felony',boroughs,month_names,'Felonies','All Felonies','Felonies','line'))
                ]
            ),
            dcc.Tab(id='Misdemeanor', label='Misdemeanor Complaints',
                children=[
                dcc.Graph(figure=generalDashWrapper('level','Misdemeanor',boroughs,month_names,'Misdemeanors','All Misdemeanors','Misdemeanors','line'))
                ]
            ),
            dcc.Tab(id='Violation', label='Violation Complaints',
                children=[
                dcc.Graph(figure=generalDashWrapper('level','Violation',boroughs,month_names,'Violations','All Violations','Violations','line'))
                ]
            ),
            dcc.Tab(id='Types', label='Types of Crime',
                children=[
                dcc.Graph(figure=
                {'data': [crimeTypeQueryToDash(off_desc_return(), 'bar', 'Types of Crime in New York')],
                'layout': {'title':'Types of Crime','marker_color':'crimson'}},
                )]
            ),
            ])
        ]),
    html.H2('Crime Clusters by Primary Description'),
    dcc.Dropdown(
        id='my-dropdown',
        options=drop_down_options,
        placeholder = "Select an Offense"
        # value=drop_down_options[0]['value']
    ),
    html.Iframe(id='output-container',srcDoc = initial_display, width = '100%', height = '600')])

@app.callback(
    dash.dependencies.Output('output-container', 'srcDoc'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):
    if value != None:
        srcDoc = open('dash_package/map_storage/{}.html'.format(value), 'r').read()
        return srcDoc
