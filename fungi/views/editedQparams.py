def clean_q_params(q_params):
    for q in list(q_params):
        if q_params[q] == '' or q_params[q] == 'None' or q_params[q] == 'value' or q_params[q] == 'initial':
            del q_params[q]
    return q_params
