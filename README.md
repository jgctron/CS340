Grazioso Salvare Dashboard

 It is dashboard application, which was develped by Python's Dash framework and connected to MongoDB database for fetch data from it. Also, received fetched data will be showed with interactive components of the dashboard such as data table, pie chart, and map. This application will help to Grazioso Salvare, which is animal rescue organization, to track and manage rescue animals' records effectively.

Project Overview

The dashboard provides the following functionalities:

 Web App: User interface for an interactive application that retrieves animal data from a MongoDB database. When a rescue type is selected through a radio button input field, the data in the table filter information based on that selection.

Pie Chart: Shows the distribution of types of animals in the database. The chart is interactive and changes based on the selected type of rescue.

 Map Integration: a map of the locations of rescued animals with markers that are updated by the filtered data.

 Branding: The Grazioso Salvare logo is clearly displayed at the top of the dashboard, unifying the brand across all elements.

Installation and Setup

Prerequisites

Python 3.x

Jupyter Notebook or JupyterLab

Required Python packages: Dash, Plotly, Pandas, Pymongo, Dash-Leaflet

Installation Steps

Set up MongoDB connection:

Ensure that the MongoDB instance is accessible with the following credentials:

Host: nv-desktop-services.apporto.com

Port: 32681

Username: aacuser

Password: SNHU1234

Ensure that the AAC database and animals collection are set up correctly.

Run the Dashboard:

Open the ProjectTwoDashboard.ipynb file in Jupyter Notebook or JupyterLab.

Run all cells in the notebook to start the dashboard.

Features

1. Interactive Data Table

The table below displays in-depth information about the rescued animals.
Usually this table helps various users in improve their knowledge about the rescuing events being held to help animals in need.
What makes this table so unique is that it can be filtered by giving information about rescue type (Water Rescue, Mountain Rescue or Disaster Rescue).

2. Pie Chart

 This pie chart illustrates what % of animals (Dog, Cat. The chart is automatically updated depending on which data is sent by filtering it by type of rescue.

3. Map Visualization

Map depicts the rescue operations geographically. Each marker On this map shows the location where an animal is saved. The map updates by showing only locations that are relevant to the selected filter.

Code Overview

The code is structured as follows:

 establish a connection to the MongoDB database, using pymongo to initiate the connection based on credentials and connection URI – defined in connection_uri.

 Functionality offered: The fetch_data function is for querying the MongoDB collection and receives a Pandas DataFrame as output. In order to clean the complex dataset for display, the function drops the _id field of MongoDB.

 Dash Board Layout:The dash board layout consists of a combination of Dashboard components like  html.Div,  dcc.RadioItems, dash_table.DataTable, dcc.Graph and dl.Map.These components are used to make the dash board responsive.

 Callbacks: Dash callbacks to update the data table, as well as pie chart and markers in the map based on the rescue type selected.  update_data_and_chart is used to process the input from the radio buttons and display the updated data.

Reflection and Insights

How do you write programs that are maintainable, readable, and adaptable?

As the person who made the code, I made sure when revisiting it that it was not difficult to know what the code does, how it can be changed, how new functionalities can be added and what information it can be asked to retrieve in the future. Thanks to the modularisation of the functions (e.g., the function fetch_data can be used again and again if we want to query other data), each part of the code and the functions central to it would be easy to read and not very long - replacing the part of the code that deals with preprocessing the data would not be stressful or required extensive training. Using Dash components would also make the code adaptable and modular so new features can work on the whole code.

How do you approach a problem as a computer scientist?

In never faced such problem. I followed these steps: first I understood the requirement of the project, after that, I break down the problem into subproblems and solved them piece by piece. For data storage and retrieval, I used a MongoDB database, and the database schema was designed according to the requirements of the application. The flexibility of the code that I wrote allowed me to focus on one specific feature at a time, solving separate tasks without worrying about how it fits in the larger, completed product.

What do computer scientists do, and why does it matter?

Computer scientists harness technology to resolve real-world issues. The mission of my project is to support this aim. A user-friendly interface between the data and the user can help Grazioso Salvare analyse its rescue operations in a more structured, reliable, painless, and efficient way to inform its decisions.

Future Work

In the future, this dashboard could be extended to include additional features such as:

Refining Filtering: Allow more refined filters to let you search by breed, age, outcomes, or other characteristic.  

Analytics: Adding more charts and graphs to provide deeper insights into rescue operations.

User Authentication: Implementing user authentication to restrict access to sensitive data.
