def DFS(graph:dict):
    '''Depth-First Search
    Parameters
    --------
    graph: dict
        Graph with Vertices V'''
    visited = {u: False for u in graph.keys()}
    father = {u: None for u in graph.keys()}
    for u in graph.keys():
        if not visited[u]:
            ok = DFS_visited(graph, u, visited, father)
        if ok == 0:
            return 0
        else:
            continue
    return 1

def DFS_visited(graph, u, visited, father):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            father[v] = u
            DFS_visited(graph, v, visited, father)
    
    if False in visited.values():
        return 0