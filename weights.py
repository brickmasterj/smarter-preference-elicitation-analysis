# Implement ROC, RS, RR and ROD


def get_roc_weights(n):
    ''' Generates weights based on ROC method
    introduced by Edwards and Barron (1998)
    '''
    weights = [(1 / n) * sum(1 / j for j in range(i, n + 1)) for i in range(1, n + 1)]

    return weights
    

def get_rs_weights(n):
    ''' Generate weights based on RS method
    '''
    weights = [(2 * (n + 1 - i)) / (n * (n + 1)) for i in range(1, n + 1)]

    return weights


def get_weights(weighing_method, num_of_attributes, additional_options = None):
    ''' Wrapper function for getting weights.
    Will split based on method to appropriate actual
    weight generating function
    '''
    weights = []

    if weighing_method == 'ROC':
        weights = get_roc_weights(num_of_attributes)
    if weighing_method == 'RS':
        weights = get_rs_weights(num_of_attributes)

    return weights
