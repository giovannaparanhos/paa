from collections import defaultdict


def add_edge(matrix, from_x, to_y, type):
    '''
    Add edge to matrix'''
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


def add_edge(graph, from_x, to_y, type):     
    '''add edge to dict'''  
    i = from_x -1
    j = to_y - 1
        # pair vw is one-way v->w if 1, 
        # two-way v<=>w if 2
    if type == 1:
        graph[i].append(j)

    elif type ==2:
        if j not in graph[i]:
            graph[i].append(j)

        if i not in graph[j]: 
            graph[j].append(i)
    if j not in graph.keys():
        graph[j] = []
    
    return dict(graph)