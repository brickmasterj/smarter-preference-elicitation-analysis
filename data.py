# Convert input data into usable attributes dictionary
import plotly.graph_objects as go
import pandas as pd
from weights import get_weights


def generate_graphs(attributes):
    ''' Generate figure for each attribute in
    attributes, and return it.
    '''
    for key, value in attributes.items():
        if value['type'] == 'numerical':
            attributes[key]['fig'] = go.Figure(
                data=go.Scatter(
                    name=key,
                    x=value['levels'],
                    y=value['values'],
                    error_y=dict(
                        type='data',
                        symmetric=False,
                        array=value['pos_error'],
                        arrayminus=value['neg_error'])),
                layout_yaxis_range=[attributes[key]['min_value_level'], attributes[key]['max_value_level']],
                layout_margin=dict(l=0, r=0, t=50, b=0),
                layout_font={'size': 22})

            attributes[key]['fig'].update_xaxes(title_text = attributes[key]['x_label'], title_font = {'size': 22})
            attributes[key]['fig'].update_yaxes(title_text = 'Likelihood', title_font = {'size': 22})
        else: # it must thus be nominal
            attributes[key]['fig'] = go.Figure(
                data=go.Bar(
                    name=key,
                    x=value['levels'],
                    y=value['values'],
                    error_y=dict(
                        type='data',
                        symmetric=False,
                        array=value['pos_error'],
                        arrayminus=value['neg_error'])),
                layout_yaxis_range=[attributes[key]['min_value_level'], attributes[key]['max_value_level']],
                layout_margin=dict(l=0, r=0, t=50, b=0),
                layout_font={'size': 22})

            attributes[key]['fig'].update_xaxes(title_text = attributes[key]['x_label'], title_font = {'size': 22})
            attributes[key]['fig'].update_yaxes(title_text = 'Likelihood', title_font = {'size': 22})
        
        # attributes[key]['fig'].write_image('images/' + key.replace(' ', '_') + '.eps', height=600)

    return attributes


def format_data_lighthousestudio(csv_data, csv_labels, weighing_method):
    ''' Format data from Lighthouse Studio from Sawtooth Software
    '''
    num_of_attributes = len(csv_labels)
    attr_index = 1

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

            if level_mean + level_std < attribute['max_value_level']:
                attribute['pos_error'].append(level_std)
            else:
                attribute['pos_error'].append(attribute['max_value_level'] - level_mean)

            if level_mean - level_std > attribute['min_value_level']:
                attribute['neg_error'].append(level_std)
            else:
                attribute['neg_error'].append(abs(attribute['min_value_level'] - level_mean))

        # Generate rank score for attribute, see https://help.surveymonkey.com/articles/en_US/kb/How-do-I-create-a-Ranking-type-question
        attribute_rank = 0

        for i in range(1, num_of_attributes + 1):
            attribute_rank += csv_data['Ranking_' + str(i)].tolist().count(attribute['ranking_id']) * (num_of_attributes + 1 - i)

        attribute['rank'] = attribute_rank

    # Generate actual weights list from method
    weights = get_weights(weighing_method, num_of_attributes)

    # Sort csv_labels by highest rank and add weights and index into attributes by iterating
    attributes = dict(sorted(csv_labels.items(), key=lambda k: -k[1]['rank']))

    for attribute_name, attribute in attributes.items():
        attribute['weight'] = weights[0]
        weights.pop(0)

        attribute['index'] = attr_index
        attr_index += 1

    return attributes
    

def format_data(csv_data = None, csv_labels = None, csv_type = None, weighing_method = 'RS'):
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
