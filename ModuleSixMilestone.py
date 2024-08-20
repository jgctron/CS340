from jupyter_dash import JupyterDash
from dash import html, dcc, Input, Output, dash_table
import pandas as pd
import dash_leaflet as dl
from CRUD_python8_10_DrWilson import AnimalShelterCRUD

# MongoDB connection setup with credentials
USER = 'aacuser'
PASS = 'SNHU1234'
HOST = 'nv-desktop-services.apporto.com'
PORT = 32681
DB = 'aac'
COL = 'animals'

# Create MongoDB client
# Dr. Wilson
# The Python module you defined should be used here to connect to MongoDB
# instead of directly connecting to MongoDB using PyMongo
#
# Change to your own connection information here
data = AnimalShelterCRUD(USER, PASS, '127.0.0.1', 27017, 'aac')

# Function to fetch data from MongoDB
def fetch_data(query={}):
    df = pd.DataFrame(list(data.read(query)))
    if '_id' in df.columns:
        df.drop('_id', axis=1, inplace=True)
    return df

# Initialize the Dash app
app = JupyterDash(__name__)

# Define the layout of the Dash app
app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-id',
        columns=[{'name': i, 'id': i} for i in fetch_data().columns],
        data=fetch_data().to_dict('records'),
        row_selectable='single',
        page_size=10,
        selected_rows=[0],
        style_table={'overflowX': 'auto'}
    ),
    html.Div(id='map-id', className='col s12 m6', style={'width': '100%', 'height': '50vh'})
])

# Function to update the map based on selected data table row
@app.callback(
    Output('map-id', 'children'),
    [Input('datatable-id', 'derived_virtual_data'),
     Input('datatable-id', 'selected_rows')]
)
def update_output(rows, selected_rows):
    if not selected_rows:
        selected_rows = [0]
    dff = pd.DataFrame(rows)
    print('hi')
    selected_data = dff.iloc[selected_rows[0]]
    print(selected_data)
    return [
        dl.Map(style={'width': '1000px', 'height': '500px'},
               center=[30.75, -97.48], zoom=10, children=[
            dl.TileLayer(), # Dr. Wilson - change lattitude to location_lat & longitude to location_long
            dl.Marker(position=[selected_data.get('location_lat', 30.75), selected_data.get('location_long', -97.48)],
                      children=[
                          dl.Tooltip(selected_data.get('animal_type', '')),
                          dl.Popup([
                              html.H1("Animal Name"),
                              html.P(selected_data.get('name', 'No Name Provided'))
                          ])
                      ])
        ])
    ]

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
