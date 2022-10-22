from dash import Dash, dcc, html, dash_table, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url, load_figure_template
import pandas as pd
import pathlib


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()
IMG_PATH = PATH.joinpath("img").resolve()


#Data puerto Año
puerto_PA = pd.read_excel(DATA_PATH.joinpath("puerto_PA.xlsx")
                          , sheet_name="Sheet1")

#Pasar la variable de Año a entero
puerto_PA["Año"] = puerto_PA["Año"].astype(int)

#Data Puerto Especie año
puerto_PAE = pd.read_csv(DATA_PATH.joinpath("puerto_PAE.csv"))

#Pasar la variable de Año a entero
puerto_PAE["Año"] = puerto_PAE["Año"].astype(int)

# stylesheet with the .dbc class
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
# Makes the Bootstrap Themed Plotly templates available
load_figure_template("cosmo")
# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO, dbc_css])
server = app.server

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
    color="#c1d4d9",
    fluid=True,
    fixed="top",

)
########################################
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
            } , value=[1995, 2005]),
    ],
    className="mb-3",
)
###############################################
########################################
range_slider2 = html.Div(
    [
        dbc.Label("Periodo de analisis", html_for="range-slider"),
        dcc.RangeSlider(id="range-slider2",step=1, min=1989, max=2019,
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
            } , value=[1995, 2005]),
    ],
    className="mb-3",
)
###############################################

jumbotron = html.Div(
    dbc.Container(
        [
            html.H2("Indicadores de Actividad Industrial", className="display-3", style={'textAlign':'center'}),
            html.P(
                "La presente serie de indicadores refieren a la actividad industrial pesquera en la Argentina. Entre 1989 y 2019 segun estadisticas nacionales y provinciales de dominio publico. Los datos se organizan según Provincias, Puertos y Especies donde la dimension tiempo y desembarques juegan un papel importante en la actividad pesquera en la Argentina. Las dimensiones captura incidental y descartes deben...",
                className="lead", style={'textAlign':'center'})
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 rounded-3",
)
################################################
unpsjb = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src=IMG_PATH.joinpath("logounisinletras.gif"),
                        className="img-fluid rounded-start",
                        style={'max-height':'100px','width':'auto'},
                    ),
                    className="col-md-4 p-1",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("UNPSJB", className="card-title"),
                            html.P(
                                "Universidad Nacional"
                                "de la Patagonia"
                                "San Juan Bosco ",
                                className="card-text",
                            ),
                            dbc.CardLink("UNPSJB", href="http://www.unp.edu.ar/"),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    #style={"width": "24rem"},
)
################################################
ospa = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src=IMG_PATH.joinpath("logoOSPA.png"),
                        className="rounded-start",
                        style={'max-height':'100px','width':'auto'}
                    ),
                    className="col-md-4 p-3",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("OSPA", className="card-title"),
                            html.P(
                                "Observatorio del Sistema Pesquero Argentino",
                                className="card-text",
                            ),
                            dbc.CardLink("OSPA", href="http://www.unp.edu.ar/ospa/"),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    #style={"width": "24rem"},
)
################################################
gepla = dbc.Card(
    dbc.CardBody(
        [
            html.H4("GEPLA", className="card-title"),
            html.P(
                "Grupo de Estudios Pesqueros del Litoral Atlántico "
            ),
        ]
    ),
    #style={"width": "18rem"},
)
###############################################
###### Layout ########
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([navbar],)]
        ,className='mb-2 mt-3'),

    dbc.Row([
        dbc.Col([jumbotron], width={"size": 10, "offset": 1})]
        ,className='mb-2 mt-5'),

    dbc.Row([
        dbc.Col([
            dbc.Container(
                [
                    html.H3("Provincia - Puerto", className="display-3"),
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
                    html.H3("Especie", className="display-3"),
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
                    range_slider2,
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

    html.Hr(className="my-2 mb-4 mt-4 border border-primary", style={'width': '100%'}),

    dbc.Row([
            dbc.Col([unpsjb,
            ], width={"size": 3, "offset": 1}),
            dbc.Col([gepla,
            ], width={"size": 2, "offset": 1}),
            dbc.Col([ospa,
            ], width={"size": 3, "offset": 1}),

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
        template='cosmo',
    )

    fig_sunburst.update_traces(textinfo='label+percent entry+value')
    fig_sunburst.update_layout(font=dict(color="#839496"),
                               title_font_size=24)

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
    template='cosmo',
    )
    fig_bar_chart.update_layout(font=dict(color="#839496"),
                                title_font_size=24,
                                legend_font_size=14)
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
    color="Provincia",               # differentiate color of marks
    color_discrete_sequence=px.colors.qualitative.Pastel2,
    opacity=0.9,                  # set opacity of markers (from 0 to 1)
    orientation="v",              # 'v','h': orientation of the marks
    barmode='relative',           # in 'overlay' mode, bars are top of one another.
                                  # in 'group' mode, bars are placed beside each other.
                                  # in 'relative' mode, bars are stacked above (+) or below (-) zero.
    #----------------------------------------------------------------------------------------------
    #facet_row='Provincia',          # assign marks to subplots in the vertical direction
    # facet_col='caste',          # assigns marks to subplots in the horizontal direction
    # facet_col_wrap=2,           # maximum number of subplot columns. Do not set facet_row!

    # color_discrete_sequence=["pink","yellow"],               # set specific marker colors. Color-colum data cannot be numeric
    # color_discrete_map={"Male": "gray" ,"Female":"red"},     # map your chosen colors
    # color_continuous_scale=px.colors.diverging.Picnic,       # set marker colors. When color colum is numeric data
    # color_continuous_midpoint=100,                           # set desired midpoint. When colors=diverging
    # range_color=[1,10000],                                   # set your own continuous color scale
    #----------------------------------------------------------------------------------------------
    # text='Desembarque',            # values appear in figure as text labels
     hover_name='Puerto',   # values appear in bold in the hover tooltip
    # hover_data=['Desembarque'],    # values appear as extra data in the hover tooltip
     #custom_data=['others'],     # invisible values that are extra data to be used in Dash callbacks or widgets

    # log_x=True,                 # x-axis is log-scaled
    # log_y=True,                 # y-axis is log-scaled
    # error_y="err_plus",         # y-axis error bars are symmetrical or for positive direction
    # error_y_minus="err_minus",  # y-axis error bars in the negative direction

    labels={"Puerto":"Puerto",
    "Desembarque":"Capturas (tn)"},           # map the labels of the figure
    title='Desembarques (t) por Año - según puerto y provincia ', # figure title
    #width=1400,                   # figure width in pixels
    height=600,                    # figure height in pixels
    template='cosmo',       # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                  # 'plotly_white', 'plotly_dark', 'presentation',
                                  # 'xgridoff', 'ygridoff', 'gridon', 'none'

     animation_frame='Año',     # assign marks to animation frames
     # animation_group=,         # use only when df has multiple rows with same object
     # range_x=[5,50],           # set range of x-axis
     range_y=[0,500000],           # set range of x-axis
     #category_orders={'Año':    # force a specific ordering of values per column
     #[2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001]},

)

    fig_PPA_ani.update_layout(font=dict(color="#839496"),
                                title_font_size=24,
                                legend_font_size=14)
    return (fig_PPA_ani)
#*****************************************************************************


#sunburst2 *****************************************************************
@app.callback(
    Output('sunburst2', 'figure'),
    [Input('range-slider2', 'value')])

def update_sunburst(anos_elegidos):

    c_puerto_PAE = puerto_PAE[(puerto_PAE['Año'] >= anos_elegidos[0]) & (puerto_PAE['Año'] <= anos_elegidos[1])]


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
        template='cosmo',
    )

    fig_sunburst2.update_traces(textinfo='label+percent entry+value')
    fig_sunburst2.update_layout(font=dict(color="#839496"),
                               title_font_size=24)

    return (fig_sunburst2)
#*****************************************************************************


#bar-chart2 *****************************************************************
@app.callback(
    Output('bar-chart2', 'figure'),
    [Input('range-slider2', 'value')])

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
    template='cosmo',
    )
    fig_bar_chart2.update_layout(font=dict(color="#839496"),
                                title_font_size=24,
                                legend_font_size=14)
    return (fig_bar_chart2)
#*****************************************************************************

#PAEa-ani *****************************************************************
@app.callback(
    Output('PAE-ani', 'figure'),
    [Input('range-slider2', 'value')])

def update_PAE_ani(anos_elegidos):
    c_puerto_PAE = puerto_PAE[(puerto_PAE['Año'] >= anos_elegidos[0]) & (puerto_PAE['Año'] <= anos_elegidos[1])]

    fig_PAE_ani =  px.bar(
    data_frame=c_puerto_PAE,
    x="Especie",
    y="Desembarques",
    color="Puerto",
    color_discrete_sequence=px.colors.qualitative.Pastel2,
    opacity=0.9,
    orientation="v",
    barmode='relative',
    hover_name='Desembarques',
    labels={"Puerto":"Puerto","Desembarques":"Capturas (tn)"},
    title='Desembarques (Tn) por Especie (top 10) - Año - segun Puerto',
    #width=1366,
    height=720,
    template='cosmo',
    animation_frame='Año',       # assign marks to animation frames
    range_y=[0,500000]           # set range of x-axis
    )
    fig_PAE_ani.update_layout(font=dict(color="#839496"),
                                title_font_size=24,
                                legend_font_size=14,
                                uniformtext_minsize=14,
                                uniformtext_mode='hide',
                                xaxis={'categoryorder':'total descending'})
    fig_PAE_ani.update_xaxes(range=(-.5, 10.5))
    return (fig_PAE_ani)
#*****************************************************************************

if __name__=='__main__':
    app.run_server(debug=False)