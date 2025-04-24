import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/distribution', name="Distribution 📊")

####################### LOAD DATASET #############################
data_df = pd.read_csv("Cleaned_Dataset.csv")

####################### HISTOGRAM ###############################
def create_distribution(col_name="Age"):
    return px.histogram(data_frame=data_df, x=col_name, height=600)

####################### WIDGETS ################################
columns = ["Age", "Projects_Completed", "Internships_Completed", "Certifications", "Job_Offers"]
dd = dcc.Dropdown(id="dist_column", options=columns, value="Age", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.P("Select Column:"),
    dd,
    dcc.Graph(id="histogram")
])

####################### CALLBACKS ################################
@callback(Output("histogram", "figure"), [Input("dist_column", "value"), ])
def update_histogram(dist_column):
    return create_distribution(dist_column)
