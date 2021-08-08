import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    np_matrix = np.array(list).reshape(3, 3)
    # required the result to be lists and not Numpy arrays.
    means = [ np_matrix.mean(axis=0).tolist() , np_matrix.mean(axis=1).tolist(), np_matrix.mean() ]
    vars = [ np_matrix.var(axis=0).tolist(), np_matrix.var(axis=1).tolist(), np_matrix.var() ]
    stds = [ np_matrix.std(axis=0).tolist(), np_matrix.std(axis=1).tolist(), np_matrix.std() ]
    maxs = [ np_matrix.max(axis=0).tolist(), np_matrix.max(axis=1).tolist(), np_matrix.max() ]
    mins = [ np_matrix.min(axis=0).tolist(), np_matrix.min(axis=1).tolist(), np_matrix.min() ]
    sums = [ np_matrix.sum(axis=0).tolist(), np_matrix.sum(axis=1).tolist(), np_matrix.sum() ]

    calculations = {
        'mean': means,
        'variance': vars,
        'standard deviation': stds,
        'max': maxs,
        'min': mins,
        'sum': sums
    }
    return calculations