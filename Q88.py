import numpy as np

def pagerank(adj_matrix, damping_factor=0.85, epsilon=1e-8):
    n = adj_matrix.shape[0]
    deg_out = np.sum(adj_matrix, axis=1)
    P = adj_matrix / deg_out[:, np.newaxis]
    v = np.ones(n) / n
    while True:
        v_new = (1 - damping_factor) / n + damping_factor * P.T.dot(v)
        if np.linalg.norm(v - v_new) < epsilon:
            break
        v = v_new
    return v
