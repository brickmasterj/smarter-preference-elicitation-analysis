# Main app script
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
from data import format_data


def graph_element(key, weight, fig):
    ''' Generate a <div> element for each graph containing
    the graph itself, the title and the weight.
    '''
    return html.Div(children=[
        html.H2(children='{} {}'.format(key, weight)),
        dcc.Graph(figure=fig)])

# # Example attributes dataset
# example_attributes_dataset = {
#     'Cost': {                                       # Name of the attribute, must be unique!
#         'type': 'numerical',                        # Type of the attribute
#         'weight': 0.75,                             # Weight distributed to attribute based on selected weighin method
#         'levels': [10, 20, 30, 40, 50],             # Levels of the attribute, array[int||float] for numerical, array[str] for nominal
#         'values': [0.9, 0.5, 0.2, 0.15, 0.1],       # Average value elicited for each level
#         'pos_error': [0.1, 0.2, 0.1, 0.05, 0.02],   # Error bar in positive direction for each level
#         'neg_error': [0.2, 0.1, 0.05, 0.1, 0.1],    # Error bar in negative direction for each level
#         'x_label': 'Cost [€]'                       # Label for x-axis
#     },
#     'Happiness': {                                  # Name of the attribute, must be unique!
#         'type': 'nominal',                          # Type of the attribute
#         'weight': 0.25,                             # Weight distributed to attribute based on selected weighin method
#         'levels': ['Barely any',                    # Levels of the attribute, array[int||float] for numerical, array[str] for nominal
#             'A bit',
#             'Average amount',
#             'A lot'],             
#         'values': [0.2, 0.4, 0.6, 0.8],             # Average value elicited for each level
#         'pos_error': [0.1, 0.2, 0.1, 0.2],          # Error bar in positive direction for each level
#         'neg_error': [0.2, 0.3, 0.2, 0.1],          # Error bar in negative direction for each level
#         'x_label': 'Happiness [-]'                  # Label for x-axis
#     }
# }

# # If no attributes dataset is provided, use the example one
# attributes = example_attributes_dataset

# # Generate figure for each attribute
# for key, value in attributes.items():
#     if value['type'] == 'numerical':
#         attributes[key]['fig'] = go.Figure(data=go.Scatter(
#             name=key,
#             x=value['levels'],
#             y=value['values'],
#             error_y=dict(
#                 type='data',
#                 symmetric=False,
#                 array=value['pos_error'],
#                 arrayminus=value['neg_error'])))
#     else:
#         attributes[key]['fig'] = go.Figure(data=go.Bar(
#             name=key,
#             x=value['levels'],
#             y=value['values'],
#             error_y=dict(
#                 type='data',
#                 symmetric=False,
#                 array=value['pos_error'],
#                 arrayminus=value['neg_error'])))

attributes = format_data()

# Generate Dash graphs from figures, with title in a <div>
graphs = [graph_element(key, attribute['weight'], attribute['fig']) for key, attribute in attributes.items()]

# fig_cost = go.Figure(data=go.Scatter(
#     name='Cost',
#     x=test_dataset['attributes']['Cost']['levels'],
#     y=test_dataset['attributes']['Cost']['values'],
#     error_y=dict(
#         type='data',
#         symmetric=False,
#         array=test_dataset['attributes']['Cost']['pos_error'],
#         arrayminus=test_dataset['attributes']['Cost']['neg_error'])
# ))

# fig_happiness = go.Figure(data=go.Bar(
#     name='Happiness',
#     x=test_dataset['attributes']['Happiness']['levels'],
#     y=test_dataset['attributes']['Happiness']['values'],
#     error_y=dict(
#         type='data',
#         symmetric=False,
#         array=test_dataset['attributes']['Happiness']['pos_error'],
#         arrayminus=test_dataset['attributes']['Happiness']['neg_error'])
# ))

app = dash.Dash(__name__)

app.layout = html.Div(children=graphs)
# [
#     html.H1(children='Hello Dash'),

#     html.Div(children='''
#         Dash: A web application framework for Python.
#     '''),

#     dcc.Graph(figure=fig_cost),

#     dcc.Graph(figure=fig_happiness)
# ])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8081)
