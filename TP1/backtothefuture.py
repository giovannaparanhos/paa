import heapq

def add_edge(i, j, weight, graph):
    '''
    Add edge to matrix'''
    
    graph[i][j] = weight
    graph[j][i] = weight
    
    return graph

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    queue = [(0, source)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_distance:
            continue
            
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))
    return distances
                


case = 1
while True:
    try:
        vertices, routes = map(int, input().split())
        graph = {vertex: {} for vertex in range(1, vertices+1)}
        for i in range(routes):
            source, target, weight = map(int, input().split()) 
            add_edge(source, target, weight, graph)
            
        friends, seats = map(int, input().split())
        if friends > seats*routes:
            print(f"Instancia {case}")
            print("impossivel\n")
            case += 1
            continue

        price = dijkstra(graph,1)

        if price[vertices] == float('inf'):
                print(f"Instancia {case}")
                print("impossivel\n")
        else:
            print(f"Instancia {case}")
            print(price[vertices]*friends, "\n")     
        case += 1

    except EOFError:
        break