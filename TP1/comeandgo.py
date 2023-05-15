def DFS(graph):
    '''Depth-First Search
    Parameters
    --------
    graph: dict
        Graph with Vertices V'''
    for start in graph.keys():
        visited = {u: False for u in graph.keys()}  
        visited = DFS_visited(graph, start, visited)
        if False in visited.values():  
            return 0
    return 1  

def DFS_visited(graph, u, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            DFS_visited(graph, v, visited)
    return visited

    
def add_edge(i, j, type, graph):
    graph[i].add(j)
    if type ==2:
        graph[j].add(i)

    return graph

while True:
    vertices, edges = map(int, input().split())
    if edges == 0: break
    graph = {vertex: set() for vertex in range(1, vertices+1)}
    for i in range(edges):
        source, target, type = map(int, input().split()) 
        add_edge(source, target, type, graph)
        
        if i+1 == edges:
            print(DFS(graph))
        