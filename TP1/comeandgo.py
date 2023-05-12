def add_edge(graph, from_x, to_y, type):       
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

def DFS(graph:dict):
    '''Depth-First Search
    Parameters
    --------
    graph: dict
        Graph with Vertices V'''
    father = {u: None for u in graph.keys()}
    for u in graph.keys():
        visited = {u: False for u in graph.keys()}
        if not visited[u]:
            ok = DFS_visited(graph, u, visited, father)
        if not ok:
            return 0
    return 1

def DFS_visited(graph, u, visited, father):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            father[v] = u
            DFS_visited(graph, v, visited, father)
    
    if False in visited.values():
        return False
    else:
        return True
    
while True:
    line = input()
    line = line.strip().split(' ')
    line = list(map(int, line)) 
    if line == [0, 0]: break
    if len(line) == 2:
        
        n_edges = line[1]
        vertices = list(range(0, line[0]))
        neighbors = [[] for _ in range(line[0])]
        graph = dict(zip(vertices, neighbors))
        edges_added = 0
        continue
    
    edges_added += 1
    if edges_added < n_edges:
        graph = add_edge(graph, from_x=line[0], to_y=line[1], type=line[2])   
    elif edges_added == n_edges:
        graph = add_edge(graph, from_x=line[0], to_y=line[1], type=line[2])
        print(DFS(graph))