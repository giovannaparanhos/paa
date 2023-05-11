from collections import defaultdict

def build_matrix(n, value = 0):
    line = n*[value]
    matrix = n*[line]
    return matrix

def floyd_warshall(W):
    n = len(W)
    D_k_1 = [row[:] for row in W]
    for k in range(0, n):
        D_k = build_matrix(n)
        for i in range(0, n):
            for j in range(0, n):
                D_k[i][j] = min(D_k_1[i][j], (D_k_1[i][k]+D_k_1[k][j]))
                D_k[j][j] = 1
        D_k_1 = D_k
    return D_k_1
def run_algo(W):
    matrix = floyd_warshall(W)
    for i in len(matrix):
        if 0 in matrix:
            return False
    return True

while True:
    line = input()
    line = line.strip().split(' ')
    line = list(map(int, line)) 
    
    if len(line) == 2:
        if adj_matrix:
            run_algo(adj_matrix)
        n_vertices = line[0]
        adj_matrix = build_matrix(n_vertices)
    elif len(line) == 3:
        #include lines
        pass
    
    if line == [0, 0]: break



