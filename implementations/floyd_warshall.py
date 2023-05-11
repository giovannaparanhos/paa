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
    n = len(W)
    D_k_1 = W
    for k in range(1, n+1):
        D_k = build_matrix(n)
        for i in range(0, n+1):
            for i in range(0, n+1):

