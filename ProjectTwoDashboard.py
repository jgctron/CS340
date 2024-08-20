from jupyter_dash import JupyterDash
from dash import html, dcc, Input, Output, dash_table, callback
import pandas as pd
import plotly.express as px
from pymongo import MongoClient
import base64
import dash_leaflet as dl

# MongoDB connection setup with credentials
USER = 'aacuser'
PASS = 'SNHU1234'
HOST = 'nv-desktop-services.apporto.com'
PORT = 32681
DB = 'AAC'
COL = 'animals'
connection_uri = f"mongodb://{USER}:{PASS}@{HOST}:{PORT}/{DB}?authSource=admin"
client = MongoClient(connection_uri)
db = client[DB]
collection = db[COL]

# Function to fetch data from MongoDB
def fetch_data(query={}):
    df = pd.DataFrame(list(collection.find(query)))
    if '_id' in df.columns:
        df.drop('_id', axis=1, inplace=True)
    return df

# Load and encode the logo
image_filename = 'pic.jpeg'  # Adjust the filename as needed
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')

# Initialize the Dash app
app = JupyterDash(__name__)

# Define the layout of the Dash app
app.layout = html.Div([
    html.Div([
        html.Img(src=f'data:image/jpeg;base64,{encoded_image}', style={'height': '100px'}),
        html.H2('Grazioso Salvare', style={'color': 'red'})
    ], style={'textAlign': 'center'}),

    dcc.RadioItems(
        id='rescue-type-filter',
        options=[
            {'label': 'All', 'value': 'ALL'},
            {'label': 'Water Rescue', 'value': 'Water Rescue'},
            {'label': 'Mountain Rescue', 'value': 'Mountain Rescue'},
            {'label': 'Disaster Rescue', 'value': 'Disaster Rescue'}
        ],
        value='ALL',
        labelStyle={'display': 'inline-block', 'margin': '10px'}
    ),

    dash_table.DataTable(
        id='data-table',
        columns=[{'name': i, 'id': i} for i in fetch_data().columns],
        data=fetch_data().to_dict('records'),
        style_table={'height': '300px', 'overflowY': 'auto'}
    ),

    dcc.Graph(id='pie-chart'),

    # Map display
    dl.Map(center=[30.2672, -97.7431], zoom=10, children=[
        dl.TileLayer(),
        dl.LayerGroup(id="layer")
    ], style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"})
])

# Callback to update data table, pie chart, and map based on filter selection
@app.callback(
    [Output('data-table', 'data'), Output('pie-chart', 'figure'), Output('layer', 'children')],
    [Input('rescue-type-filter', 'value')]
)
def update_data_and_chart(rescue_type):
    if rescue_type == 'ALL':
        df = fetch_data()
    else:
        df = fetch_data({'rescue_type': rescue_type})

    # Update data table
    data = df.to_dict('records')
    
    # Update pie chart
    fig = px.pie(df, names='animal_type', title='Distribution of Animal Types') if not df.empty else px.pie(title="No data available")

    # Update map
    if 'location_lat' in df.columns and 'location_long' in df.columns:
        markers = [dl.Marker(position=[row['location_lat'], row['location_long']], children=[dl.Tooltip(row['animal_type'])]) for index, row in df.iterrows()]
    else:
        markers = []

    return data, fig, markers

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
