def DFS_MOD(n_cities, c_libs, c_roads, graph):
    #n_cities = min(n_cities, 100000)
    lib_counter = 0
    visited = {u: False for u in graph.keys()}  
    for city in graph.keys():
        if not visited[city]:
            lib_counter += 1
            visited = DFS_visited(graph, city, visited)
            
    return lib_counter * c_libs + (n_cities-lib_counter) * c_roads

def DFS_visited(graph, u, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            DFS_visited(graph, v, visited)
    return visited

def run_president(n_cities, n_roads, c_libs, c_roads):
    if n_roads == 0:
        return c_libs * n_cities

    roads = []
    
    for _ in range(n_roads):
        roads.append(tuple(map(int, input().split())))
        
        
    if c_libs <= c_roads:
        return c_libs * n_cities
    
    graph = {city: set() for city in range(1, n_cities + 1)}
    for road in roads:
        s,t = road[0], road[1]
        graph[s].add(t)
        graph[t].add(s)


    return DFS_MOD(n_cities, c_libs, c_roads, graph)

T = int(input())
for _ in range(min(T, 10)):
    n_cities, n_roads, c_libs, c_roads = map(int, input().split())
    print(run_president(n_cities, n_roads, c_libs, c_roads))
