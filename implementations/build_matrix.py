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

print(build_matrix(3, 1))