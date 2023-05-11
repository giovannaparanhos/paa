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

print(build_matrix(3, 1))