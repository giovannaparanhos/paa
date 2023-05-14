
def DFS_MOD(n_cities, c_libs, c_roads, graph):
    roads_built = []
    cities = set()
    for city in range(1, n_cities+1):
        if city not in cities:
            stack = [city]
            while stack:
                current_city = stack.pop()
                cities.add(current_city)
                for neighbor in graph[current_city]:
                    if neighbor not in cities:
                        stack.append(neighbor)
            roads_built.append(cities)
    total_cost=0
    for cities in roads_built:
        total_cost+= c_libs + (len(cities)-1)*c_roads
    return total_cost

def run_president(n_cities, n_roads, c_libs, c_roads):
    
    graph = {city: [] for city in range(1, n_cities+1)}
    j=0
    while j < n_roads:
        j+=1
        s, t = map(int, input().split())
        graph[s].append(t)
        graph[t].append(s)

        if j==n_roads:
            if c_libs > 0 and c_libs <= c_roads:
                total_cost=c_libs*n_cities
                return total_cost
            total_cost = DFS_MOD(n_cities, c_libs, c_roads, graph)
            return total_cost


T = int(input())
i = 0
while i < T:
    n_cities, n_roads, c_libs, c_roads  = map(int, input().split())
    print(run_president(n_cities, n_roads, c_libs, c_roads))
    i += 1
