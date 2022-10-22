import dash                              # pip install dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from dash_bootstrap_templates import load_figure_template # pip install dash_bootstrap_templates
import plotly.graph_objects as go        # pip install plotly
import cufflinks as cf                   # pip install cufflinks
from datetime import date



#Data
#Data puerto Año
puerto_PA = pd.read_excel("assets/datasets/puerto_PA.xlsx"
                          , sheet_name="Sheet1")
#Pasar la variable de Año a entero
puerto_PA["Año"] = puerto_PA["Año"].astype(int)
years_PA = puerto_PA.Año.unique()

#Data Puerto Especie año
puerto_PAE = pd.read_csv("assets/datasets/puerto_PAE.csv")
#Pasar la variable de Año a entero
puerto_PAE["Año"] = puerto_PAE["Año"].astype(int)
years_PAE = puerto_PAE.Año.unique()
# stylesheet with the .dbc class
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
# Makes the Bootstrap Themed Plotly templates available
load_figure_template("minty")
# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY, dbc_css])


#Components

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("OSPA", href="#")),
        dbc.NavItem(dbc.NavLink("Metodología", href="#")),
        dbc.NavItem(dbc.NavLink("Datasets", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Actividad", header=True),
                dbc.DropdownMenuItem("Ambientales", href="#"),
                dbc.DropdownMenuItem("Sociales", href="#"),
                dbc.DropdownMenuItem("Laborales", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Dimensiones",
        ),
    ],
    brand="Observatorio del Sistema Pesquero Argentino - Tablero de control",
    brand_href="http://www.unp.edu.ar/ospa/",
    #color="#c1d4d9",
    fluid=True,
    fixed="top",

)

range_slider = html.Div(
    [
        dbc.Label("Periodo de analisis", html_for="range-slider"),
        dcc.RangeSlider(id="range-slider",step=1, min=1989, max=2019,
                        marks={
                             1989: '89',
                             1990: '90',
                             1991: '91',
                             1992: '92',
                             1993: '93',
                             1994: '94',
                             1995: '95',
                             1996: '96',
                             1997: '97',
                             1998: '98',
                             1999: '99',
                             2000: '00',
                             2001: '01',
                             2002: '02',
                             2003: '03',
                             2004: '04',
                             2005: '05',
                             2006: '06',
                             2007: '07',
                             2008: '08',
                             2009: '09',
                             2010: '10',
                             2011: '11',
                             2012: '12',
                             2013: '13',
                             2014: '14',     # key=position, value=what you see
                             2015: '15',
                             2016: '16',
                             2017: '17',
                             2018: '18',
                             2019: '19'
            } , value=[1989, 2019]),
    ],
    className="mb-3",
)

jumbotron = html.Div(
    dbc.Container(
        [
            html.H2("Indicadores de Actividad Industrial", className="display-4", style={'textAlign':'center'}),
            html.P(
                "La presente serie de indicadores refieren a la actividad industrial pesquera en la Argentina. Entre 1989 y 2019 segun estadisticas nacionales y provinciales de dominio publico. Los datos se organizan según Provincias, Puertos y Especies donde la dimension tiempo y desembarques juegan un papel importante en la actividad pesquera en la Argentina. Las dimensiones captura incidental y descartes deben...",
                className="lead", style={'textAlign':'center'})
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 rounded-3",
)

#layout
app.layout = dbc.Container([
    #nav bar
    dbc.Row([
        dbc.Col([navbar],)]
        ,className='mb-2 mt-3'),
    #feature
    dbc.Row([
        dbc.Col([jumbotron], width={"size": 10, "offset": 1})]
        ,className='mb-2 mt-5'),

    dbc.Row([
        dbc.Col([
            dbc.Container(
                [
                    html.H3("Provincia - Puerto", className="display-5"),
                    html.P(
                        "Capturas por año según provincia y su respectivo puerto",
                        className="lead",
                    ),
                    html.Hr(className="m-1 mb-3 border border-primary", style={'width': '30%'}),
                    html.P(
                        "Participación Desembarques Totales (% y t) de los puertos de esa provincia. (Gráfico de Torta) y  de los puertos de esa provincia. (Gráfico de Barras)",
                    ),
                    range_slider,
                ],
                fluid=True,
                className="py-3",
            ),
        ], width={"size": 6, "offset": 1})
    ], className='mb-2 mt-5'),


    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='sunburst', figure={}),
                ])
            ]),
        ], width={"size": 5, "offset": 1}),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='bar-chart', figure={}),
                ])
            ]),
        ], width=5),
    ],className='mb-2 mt-5'),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='PPA-ani', figure={}),
                ])
            ]),
        ], width={"size": 10, "offset": 1}),
        ], className='mb-2'),



    dbc.Row([
        dbc.Col([
            dbc.Container(
                [
                    html.H3("Especie", className="display-5"),
                    html.P(
                        "Capturas por año según especie y Puerto",
                        className="lead",
                    ),
                    html.Hr(className="m-1 mb-3 border border-primary", style={'width': '30%'}),
                    html.P(
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi dapibus, ante vehicula hendrerit"
                        "tempus, augue neque efficitur quam, id feugiat dui sapien in nisi. Aliquam erat volutpat. "
                        "Fusce et cursus odio, vel viverra tellus. Proin sodales augue dolor, quis lobortis orci hendrerit non. "
                    ),
                ],
                fluid=True,
                className="py-3",
            ),
        ], width={"size": 6, "offset": 1})
    ], className='mb-2'),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='sunburst2', figure={}),
                ])
            ]),
        ], width={"size": 5, "offset": 1}),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='bar-chart2', figure={}),
                ])
            ]),
        ], width=5),
    ], className='mb-2 mt-5'),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='PAE-ani', figure={}),
                ])
            ]),
        ], width={"size": 10, "offset": 1}),
    ], className='mb-2'),

    html.Hr(className="my-2 mb-4 mt-4 border border-primary", style={'width': '50%'}),

    dbc.Row([
            dbc.Col([
                    html.H4("Universidad Nacional de la Patagonia San Juan Bosco", className="display-5"),
                    html.P(
                        "declaración de derechos OSPA",
                        className="lead",
                    ),
            ], width={"size": 3, "offset": 1}),
            dbc.Col([
                html.H4("Grupo de Estudios Pesqueros del Litoral Atlántico", className="display-5"),
                html.P(
                    "declaración de derechos UNPSJB",
                    className="lead",
                ),
            ], width={"size": 4, "offset": 0}),
            dbc.Col([
                html.H4("OSPA", className="display-5"),
                html.P(
                    "Observatorio del Sistema Pesquero Argentino",
                    className="lead",
                ),
            ], width={"size": 3, "offset": 0}),
        ],className='mb-2 mt-5 '),

], fluid=True,
   className="dbc")

#sunburst *****************************************************************
@app.callback(
    Output('sunburst', 'figure'),
    [Input('range-slider', 'value')])

def update_sunburst(anos_elegidos):

    c_puerto_PA = puerto_PA[(puerto_PA['Año'] >= anos_elegidos[0]) & (puerto_PA['Año'] <= anos_elegidos[1])]


    fig_sunburst = px.sunburst(
        data_frame=c_puerto_PA,
        path=["Provincia", "Puerto", ],  # Root, branches, leaves
        values='Desembarque',
        color="Provincia",
        color_discrete_sequence=px.colors.qualitative.Pastel2,
        branchvalues="total",  # or 'remainder'
        hover_name="Puerto",
        title="Desembarques por provincia y puerto en toneladas",
        height=600,
        template="minty",  # use the minty themed figure template
    )

    fig_sunburst.update_traces(textinfo='label+percent entry+value')
    fig_sunburst.update_layout(font=dict(color="#839496"),title_font_size=24)

    return (fig_sunburst)
#*****************************************************************************

#bar-chart *****************************************************************
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('range-slider', 'value')])

def update_bar_chart(anos_elegidos):
    c_puerto_PA = puerto_PA[(puerto_PA['Año'] >= anos_elegidos[0]) & (puerto_PA['Año'] <= anos_elegidos[1])]

    fig_bar_chart = px.bar(
    data_frame=c_puerto_PA,
    x="Año",
    y="Desembarque",
    color="Puerto",               # differentiate color of marks
    color_discrete_sequence=px.colors.qualitative.Pastel2,
    opacity=0.9,                  # set opacity of markers (from 0 to 1)
    orientation="v",              # 'v','h': orientation of the marks
    barmode='relative',           # in 'overlay' mode, bars are top of one another.
    labels={"Puerto":"Puerto",
    "Desembarques":"Capturas (tn)"},           # map the labels of the figure
    title='Desembarques (t) por año - según Puerto', # figure title
    #width=1400,                   # figure width in pixels
    height=600,                   # figure height in pixels
    template='simple_white',
    )
    fig_bar_chart.update_layout(font=dict(color="#839496"),title_font_size=24)
    return (fig_bar_chart)
#*****************************************************************************

#PPA-ani *****************************************************************
@app.callback(
    Output('PPA-ani', 'figure'),
    [Input('range-slider', 'value')])

def update_PPA_ani(anos_elegidos):
    c_puerto_PA = puerto_PA[(puerto_PA['Año'] >= anos_elegidos[0]) & (puerto_PA['Año'] <= anos_elegidos[1])]

    fig_PPA_ani = px.bar(
    data_frame=c_puerto_PA,
    x="Puerto",
    y="Desembarque",
    color="Provincia",
    color_discrete_sequence=px.colors.qualitative.Pastel2,
    opacity=0.9,
    orientation="v",
    barmode='relative',
    hover_name='Puerto',
    labels={"Puerto":"Puerto","Desembarque":"Capturas (tn)"},
    title='Desembarques (t) por Año - según puerto y provincia ',
    #width=1400,
    height=600,
    template='plotly_white',
    animation_frame='Año',
    range_y=[0,500000]
    )

    fig_PPA_ani.update_layout(font=dict(color="#839496"),title_font_size=24)
    return (fig_PPA_ani)
#*****************************************************************************


#sunburst2 *****************************************************************
@app.callback(
    Output('sunburst2', 'figure'),
    [Input('range-slider', 'value')])

def update_sunburst(anos_elegidos):

    c_puerto_PAE = puerto_PAE[(puerto_PAE['Año'] >= anos_elegidos[0]) & (puerto_PAE['Año'] <= anos_elegidos[1])]
    print (c_puerto_PAE.info())

    fig_sunburst2 = px.sunburst(
        data_frame=c_puerto_PAE,
        path=["Puerto", "Especie" ],  # Root, branches, leaves
        values='Desembarques',
        color="Puerto",
        color_discrete_sequence=px.colors.qualitative.Pastel2,
        branchvalues="total",  # or 'remainder'
        hover_name="Puerto",
        title="Desembarques por puerto y especie en toneladas",
        height=600,
        template='simple_white',
    )

    fig_sunburst2.update_traces(textinfo='label+percent entry+value')
    fig_sunburst2.update_layout(font=dict(color="#839496"),title_font_size=24)

    return (fig_sunburst2)
#*****************************************************************************


#bar-chart2 *****************************************************************
@app.callback(
    Output('bar-chart2', 'figure'),
    [Input('range-slider', 'value')])

def update_bar_chart2(anos_elegidos):

    c_puerto_PAE = puerto_PAE[(puerto_PAE['Año'] >= anos_elegidos[0]) & (puerto_PAE['Año'] <= anos_elegidos[1])]


    fig_bar_chart2 = px.bar(
    data_frame=c_puerto_PAE,
    x="Año",
    y="Desembarques",
    color="Especie",               # differentiate color of marks
    color_discrete_sequence=px.colors.qualitative.Pastel2,
    opacity=0.9,                  # set opacity of markers (from 0 to 1)
    orientation="v",              # 'v','h': orientation of the marks
    barmode='relative',           # in 'overlay' mode, bars are top of one another.
    labels={"Especie":"Especie",
    "Desembarques":"Capturas (tn)"},           # map the labels of the figure
    title='Desembarques (t) por año - según ', # figure title
    #width=1400,                   # figure width in pixels
    height=600,                   # figure height in pixels
    template='simple_white',
    )
    fig_bar_chart2.update_layout(title_font_size=24,legend_font_size=14)
    return (fig_bar_chart2)
#*****************************************************************************

#PAEa-ani *****************************************************************
@app.callback(
    Output('PAE-ani', 'figure'),
    [Input('range-slider', 'value')])

def update_PAE_ani(anos_elegidos):
    c_puerto_PAE = puerto_PAE[(puerto_PAE['Año'] >= anos_elegidos[0]) & (puerto_PAE['Año'] <= anos_elegidos[1])]


    fig_PAE_ani =  px.bar(
    data_frame=puerto_PAE,
    x="Especie",
    y="Desembarques",
    color="Puerto",               # differentiate color of marks
    opacity=0.9,                  # set opacity of markers (from 0 to 1)
    orientation="v",              # 'v','h': orientation of the marks
    barmode='relative',           # in 'overlay' mode, bars are top of one another.
                                  # in 'group' mode, bars are placed beside each other.
                                  # in 'relative' mode, bars are stacked above (+) or below (-) zero.
    hover_name='Desembarques',    # values appear in bold in the hover tooltip
    labels={"Puerto":"Puerto",
    "Desembarques":"Capturas (tn)"},           # map the labels of the figure
    title='Desembarques (Tn) por Especie (top 10) - Año - segun Puerto', # figure title
    #width=1366,                   # figure width in pixels
    height=720,                   # figure height in pixels
    template='plotly_white',            # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                  # 'plotly_white', 'plotly_dark', 'presentation',
                                  # 'xgridoff', 'ygridoff', 'gridon', 'none'
     animation_frame='Año',     # assign marks to animation frames
     range_y=[0,500000]           # set range of x-axis
)
    fig_PAE_ani.update_layout(title_font_size=24,
                                legend_font_size=14,
                                uniformtext_minsize=14,
                                uniformtext_mode='hide',
                                xaxis={'categoryorder':'total descending'})
    fig_PAE_ani.update_xaxes(range=(-.5, 10.5))

    return (fig_PAE_ani)
#*****************************************************************************

if __name__=='__main__':
    app.run_server(debug=True, port=8003)