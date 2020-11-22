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

attributes = format_data()

# Generate Dash graphs from figures, with title in a <div>
graphs = [graph_element(key, attribute['weight'], attribute['fig']) for key, attribute in attributes.items()]

# Start Dash app and add the layout
app = dash.Dash(__name__)

app.layout = html.Div(children=graphs)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8081)
