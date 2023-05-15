def build_matrix(n:int, value = 0):
    matrix = [[value for _ in range(n)] for _ in range(n)]
    return matrix

def add_edge(i, j, type, graph):
    graph[i][j] = 1
    if type ==2:
        graph[j][i] = 1
    return graph

def DFS_visited(graph, u, visited):
    visited[u] = True
    for v in range(len(graph)):
        if graph[u][v] == 1 and not visited[v]:
            DFS_visited(graph, v, visited)
    return visited

def DFS(graph):
    for start in range(len(graph)):
        visited = [False for _ in range(len(graph))]
        visited = DFS_visited(graph, start, visited)
        if False in visited:  
            return 0
    return 1  

while True:
    vertices, edges = map(int, input().split())
    if edges == 0 or vertices ==0: break
    graph = build_matrix(vertices)
    for i in range(edges):
        source, target, type = map(int, input().split()) 
        add_edge(source-1, target-1, type, graph)
        
        
    print(DFS(graph))
        