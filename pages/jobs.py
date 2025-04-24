import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/jobs', name="Jobs Count 📊")

####################### DATASET #############################
data_df = pd.read_csv("Cleaned_Dataset.csv")

####################### BAR CHART #############################
def create_bar_chart(col_name="Gender"):
    fig =  px.histogram(data_frame=data_df, x="Job_Offers", color=col_name,
                        histfunc="count", barmode='group', height=600)
    fig = fig.update_layout(bargap=0.5)
    return fig

####################### WIDGETS ################################
columns = ["Gender", "University_GPA", "Internships_Completed", "Certifications"]
dd = dcc.Dropdown(id="sel_col", options=columns, value="Gender", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    dd, 
    dcc.Graph(id="bar_chart")
])

####################### CALLBACKS ################################
@callback(Output("bar_chart", "figure"), [Input("sel_col", "value"), ])
def update_bar_chart(sel_col):
    return create_bar_chart(sel_col)
