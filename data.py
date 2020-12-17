# Convert input data into usable attributes dictionary
import plotly.graph_objects as go
import pandas as pd

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


def format_data_lighthousestudio(csv_data, csv_labels, weighing_method = 'ROC'):
    ''' Format data from Lighthouse Studio from Sawtooth Software
    '''
    for attribute_name, attribute in csv_labels.items():
        # Generate level data
        # Initiate empty lists
        attribute['values'] = []
        attribute['pos_error'] = []
        attribute['neg_error'] = []

        # Loop over each level and calculate mean and std
        for level in attribute['level_col_names']:
            level_data = csv_data[level]
            level_mean = level_data.mean()
            level_std = level_data.std()

            attribute['values'].append(level_mean)
            attribute['pos_error'].append(level_std)
            attribute['neg_error'].append(level_std)

        # Generate weights
        attribute['weight'] = 1 # TODO: REMOVE DUMMY WEIGHTs

    return csv_labels


def format_data(csv_data = None, csv_labels = None, csv_type = None, weighing_method = 'ROC'):
    ''' Formated data into usable attributes dict,
    given input csv data, as well as specifying the type.
    Also given a certain weighing method.
    If no csv is provided, return example data.
    '''
    if csv_type == 'LighthouseStudio':
        attributes_dataset = format_data_lighthousestudio(csv_data, csv_labels, weighing_method)
        return generate_graphs(attributes_dataset)
    else:
        # Return example data
        # Example attributes dataset
        example_attributes_dataset = {
            'Cost': {                                       # Name of the attribute, must be unique!
                'type': 'numerical',                        # Type of the attribute
                'weight': 0.75,                             # Weight distributed to attribute based on selected weighin method
                'levels': [10, 20, 30, 40, 50],             # Levels of the attribute, array[int||float] for numerical, array[str] for nominal
                'level_col_names': ['Cost_r1',              # Names of the columns for each level in the dataset
                    'Cost_r2', 
                    'Cost_r3', 
                    'Cost_r4', 
                    'Cost_r5'], 
                'min_value_level': 1,                       # The minimum value that can be inputted by a user for a level
                'max_value_level': 7,                       # The maximum value that can be inputted by a user for a level
                'values': [0.9, 0.5, 0.2, 0.15, 0.1],       # Average value elicited for each level
                'pos_error': [0.1, 0.2, 0.1, 0.05, 0.02],   # Error bar in positive direction for each level
                'neg_error': [0.2, 0.1, 0.05, 0.1, 0.1],    # Error bar in negative direction for each level
                'x_label': 'Cost [€]',                      # Label for x-axis
                'ranking_id': 1},                           # ID given to this attribute in the ranking question
            'Happiness': {                                  # Name of the attribute, must be unique!
                'type': 'nominal',                          # Type of the attribute
                'weight': 0.25,                             # Weight distributed to attribute based on selected weighin method
                'levels': ['Barely any',                    # Levels of the attribute, array[int||float] for numerical, array[str] for nominal
                    'A bit',
                    'Average amount',
                    'A lot'],             
                'level_col_names': ['Happiness_r1',         # Names of the columns for each level in the dataset
                    'Happiness_r2', 
                    'Happiness_r3', 
                    'Happiness_r4'],                             
                'min_value_level': 1,                       # The minimum value that can be inputted by a user for a level
                'max_value_level': 7,                       # The maximum value that can be inputted by a user for a level
                'values': [0.2, 0.4, 0.6, 0.8],             # Average value elicited for each level
                'pos_error': [0.1, 0.2, 0.1, 0.2],          # Error bar in positive direction for each level
                'neg_error': [0.2, 0.3, 0.2, 0.1],          # Error bar in negative direction for each level
                'x_label': 'Happiness [-]',                 # Label for x-axis
                'ranking_id': 1}}                           # ID given to this attribute in the ranking question

        return generate_graphs(example_attributes_dataset)
