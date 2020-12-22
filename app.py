# Main app script
import dash
import json
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from data import format_data


def graph_element(key, attribute):
    ''' Generate a <div> element for each graph containing
    the graph itself, the title and the weight.
    '''
    return html.Div(children=[
        html.H2(children='{}. {}'.format(attribute['index'], key)),
        html.Div(children='Associated weight: {}'.format(str(round(attribute['weight'], 5)))),
        dcc.Graph(figure=attribute['fig'])])

# Try if the default files are located in the root dir, otherwise initiate with example data
try:
    csv_data = pd.read_csv('input_data.csv')
    with open('input_data_labels.json') as input_data_labels_file:
        input_data_labels = json.load(input_data_labels_file)
        csv_labels = input_data_labels['csv_labels']
        csv_type = input_data_labels['csv_type']

    attributes = format_data(csv_data, csv_labels, csv_type)
except:
    attributes = format_data()

# Generate pie char for weights with header
weights_labels = [k for k, v in attributes.items()]
weights_values = [v['weight'] for k, v in attributes.items()]

weights_fig = go.Figure(data=[go.Pie(labels=weights_labels,
    values=weights_values,
    textinfo='label+percent',
    insidetextorientation='radial')]) #, layout_margin=dict(l=50, r=50, t=50, b=50))

# weights_fig.write_image('images/Ranks.eps')

weights_graph = [html.Div(children=[
    html.H1(children='Weights', style={'textAlign': 'center'}),
    # dcc.Dropdown(options=[{'label': 'RS - Rank Sum', 'value': 'RS'},
    #                       {'label': 'ROC - Rank Order Centroid', 'value': 'ROC'}],
    #              value='RS', id='weights-selector'),
    dcc.Graph(figure=weights_fig, id='weights-graph')])]

# Generate Dash graphs from figures for each attribute, with title in a <div>
attribute_graphs = [graph_element(key, attribute) for key, attribute in attributes.items()]

# Generate overall title and attributes title
title = [html.H1(children='SMARTER Preference Elicitation Analysis Tool', style={'textAlign': 'center'}), html.Hr()]
title_attributes = [html.Hr(), html.H1(children='Attributes', style={'textAlign': 'center'})]

# Start Dash app and add the layout
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

graphs = title + weights_graph + title_attributes + attribute_graphs
app.layout = html.Div(children=graphs)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8081)
