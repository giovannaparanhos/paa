def build_matrix(n:int, value = 0):
    '''Build an nxn matrix with equal values. 
    
    Parameters
    ----------
    n: int
     number os rows/lines
    
    value: any
     Defaults to 0. Value to fill matrix.'''
    matrix = [[value for _ in range(n)] for _ in range(n)]
    return matrix

def add_edge(matrix, from_x, to_y, type):
    '''
    Add edge'''
    i = from_x - 1
    j = to_y - 1 
    #add self reaching edge
    matrix[i][j] = 1
    if type == 1:
        matrix[i][j] = 1
    elif type == 2:
        matrix[i][j] = 1
        matrix[j][i] = 1
    else:
        pass
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
    D_k = [row[:] for row in W]
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                D_k[i][j] = min(D_k[i][j], (D_k[i][k]+D_k[k][j]))

    return D_k

