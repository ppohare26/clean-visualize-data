import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/relationship', name="Relationship 📈")

####################### DATASET #############################
data_df = pd.read_csv("Cleaned_Dataset.csv")

####################### SCATTER CHART #############################
def create_scatter_chart(x_axis="Age", y_axis="Current_Job_Level"):
    return px.scatter(data_frame=data_df, x=x_axis, y=y_axis, height=600)

####################### WIDGETS #############################
columns = ["Age", "Current_Job_Level", "Career_Satisfaction", "Job_Offers", "Work_Life_Balance", "Gender"]

x_axis = dcc.Dropdown(id="x_axis", options=columns, value="Age", clearable=False)
y_axis = dcc.Dropdown(id="y_axis", options=columns, value="Current_Job_Level", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    "X-Axis", x_axis, 
    "Y-Axis", y_axis,
    dcc.Graph(id="scatter")
])

####################### CALLBACKS ###############################
@callback(Output("scatter", "figure"), [Input("x_axis", "value"),Input("y_axis", "value"), ])
def update_scatter_chart(x_axis, y_axis):
    return create_scatter_chart(x_axis, y_axis)
