def build_matrix(n:int, value = 0):
    '''Build an nxn matrix with equal values. 
    
    Parameters
    ----------
    n: int
     number os rows/lines
    
    value: any
     Defaults to 0. Value to fill matrix.'''
    line = n*[value]
    matrix = n*[line]
    return matrix

def floyd_warshall(W):
    ''''Implementation of the Floyd-Warshall algorithm.
    Parameters
    ----------
    W: list(list)
     Weight matrix
    
    Returns
    -------
    D_k_1: list(list)
    '''
    n = len(W)
    D_k_1 = [row[:] for row in W]
    for k in range(0, n):
        D_k = build_matrix(n)
        for i in range(0, n):
            for j in range(0, n):
                D_k[i][j] = min(D_k_1[i][j], (D_k_1[i][k]+D_k_1[k][j]))
        D_k_1 = D_k
    return D_k_1

