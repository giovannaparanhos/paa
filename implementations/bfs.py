def BFS(graph:dict, s):
    '''Breadth-First Search
    Parameters
    --------
    graph: dict
        Graph with Vertices V
    s: int or str
        source s'''
    vertices = {}
    for u in graph.keys():
        vertices[u] = {}
        vertices[u]['color'] = 'white'
        vertices[u]['d'] = len(graph.keys())**10
        vertices[u]['pi'] = None
    vertices[s]['color'] = 'gray'
    vertices[s]['d'] = 0
    vertices[s]['pi'] = None
    Q = []
    Q.append(s) #enqueue s
    while len(Q) != 0:
        u = Q.pop(0) #dequeue Q
        for v in graph[u]:
            if vertices[v]['color'] == 'white':
                vertices[v]['color'] = 'gray'
                vertices[v]['d'] = vertices[u]['d'] + 1
                vertices[v]['pi'] = u
                Q.append(v) #enqueue(Q, v)
        vertices[u]['color'] = 'black'
    return vertices