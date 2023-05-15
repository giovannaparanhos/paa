def DFS_MOD(n_cities, c_libs, c_roads, graph):
    n_cities = min(n_cities, 100000)
    lib_counter = 0
    visited = set()
    for city in range(1, n_cities + 1):
        if city not in visited:
            lib_counter += 1
            stack = [city]
            while stack:
                current_city = stack.pop()
                if current_city not in visited:
                    visited.add(current_city)
                    stack.extend([neighbor for neighbor in graph[current_city] if neighbor not in visited])
     
    return lib_counter * c_libs + (len(visited)-1) * c_roads

def run_president(n_cities, n_roads, c_libs, c_roads):
    if n_roads == 0:
        return c_libs * n_cities

    graph = {city: set() for city in range(1, n_cities + 1)}
    for _ in range(n_roads):
        s, t = map(int, input().split())
        if c_libs>c_roads:
            graph[s].add(t)
            graph[t].add(s)
            
    if c_libs <= c_roads:
        return c_libs * n_cities

    return DFS_MOD(n_cities, c_libs, c_roads, graph)

T = int(input())
for _ in range(min(T, 10)):
    n_cities, n_roads, c_libs, c_roads = map(int, input().split())
    print(run_president(n_cities, n_roads, c_libs, c_roads))
