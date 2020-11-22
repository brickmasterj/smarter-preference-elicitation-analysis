# Convert input data into usable attributes dictionary
import plotly.graph_objects as go

def generate_graphs(attributes):
    ''' Generate figure for each attribute in
    attributes, and return it.
    '''
    for key, value in attributes.items():
        if value['type'] == 'numerical':
            attributes[key]['fig'] = go.Figure(data=go.Scatter(
                name=key,
                x=value['levels'],
                y=value['values'],
                error_y=dict(
                    type='data',
                    symmetric=False,
                    array=value['pos_error'],
                    arrayminus=value['neg_error'])))
        else: # it must thus be nominal
            attributes[key]['fig'] = go.Figure(data=go.Bar(
                name=key,
                x=value['levels'],
                y=value['values'],
                error_y=dict(
                    type='data',
                    symmetric=False,
                    array=value['pos_error'],
                    arrayminus=value['neg_error'])))

    return attributes


def format_data(csv_data = None, csv_type = None):
    ''' Formated data into usable attributes dict,
    given input csv data, as well as specifying the type.
    If no csv is provided, return example data.
    '''
    if csv_data is not None:
        # TODO: Implement formatting data
        return dict()
    else:
        # Return example data
        # Example attributes dataset
        example_attributes_dataset = {
            'Cost': {                                       # Name of the attribute, must be unique!
                'type': 'numerical',                        # Type of the attribute
                'weight': 0.75,                             # Weight distributed to attribute based on selected weighin method
                'levels': [10, 20, 30, 40, 50],             # Levels of the attribute, array[int||float] for numerical, array[str] for nominal
                'values': [0.9, 0.5, 0.2, 0.15, 0.1],       # Average value elicited for each level
                'pos_error': [0.1, 0.2, 0.1, 0.05, 0.02],   # Error bar in positive direction for each level
                'neg_error': [0.2, 0.1, 0.05, 0.1, 0.1],    # Error bar in negative direction for each level
                'x_label': 'Cost [€]'},                     # Label for x-axis
            'Happiness': {                                  # Name of the attribute, must be unique!
                'type': 'nominal',                          # Type of the attribute
                'weight': 0.25,                             # Weight distributed to attribute based on selected weighin method
                'levels': ['Barely any',                    # Levels of the attribute, array[int||float] for numerical, array[str] for nominal
                    'A bit',
                    'Average amount',
                    'A lot'],             
                'values': [0.2, 0.4, 0.6, 0.8],             # Average value elicited for each level
                'pos_error': [0.1, 0.2, 0.1, 0.2],          # Error bar in positive direction for each level
                'neg_error': [0.2, 0.3, 0.2, 0.1],          # Error bar in negative direction for each level
                'x_label': 'Happiness [-]'}}                # Label for x-axis

        return generate_graphs(example_attributes_dataset)
