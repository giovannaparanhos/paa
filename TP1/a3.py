from heapq import heappush, heappop


def add_edge(u, v, cap, cost, graph):
    graph[u].append([v, len(graph[v]), cap, cost])
    graph[v].append([u, len(graph[u])-1, 0, -cost])

def dijkstra(cicites):
    pass

def min_cost_flow(s, t, f, graph):
    res = 0
    h = [0]*cities
    v_prev = [0]*cities
    e_prev = [0]*cities

    while f:
        dist = [float('inf')]*cities
        dist[s] = 0
        queue = [(0, s)]

        while queue:
            c, v = heappop(queue)
            if dist[v] < c:
                continue
            for i in range(len(graph[v])):
                e = graph[v][i]
                if e[2] > 0 and dist[e[0]] > dist[v] + e[3] + h[v] - h[e[0]]:
                    dist[e[0]] = dist[v] + e[3] + h[v] - h[e[0]]
                    v_prev[e[0]] = v
                    e_prev[e[0]] = i
                    heappush(queue, (dist[e[0]], e[0]))

        if dist[t] == float('inf'):
            return -1

        for v in range(cities):
            h[v] += dist[v]

        d = f
        v = t
        while v != s:
            d = min(d, graph[v_prev[v]][e_prev[v]][2])
            v = v_prev[v]

        f -= d
        res += d * h[t]
        v = t
        while v != s:
            graph[v_prev[v]][e_prev[v]][2] -= d
            graph[v][graph[v_prev[v]][e_prev[v]][1]][2] += d
            v = v_prev[v]

    return res

test_case = 1
while True:
    try:
        cities, routes = map(int, input().split())
        
        graph = [[] for _ in range(cities)]
        for _ in range(routes):
            source, target, cost= map(int, input().split())
            add_edge(source-1, target-1, 1, cost, graph)
            add_edge(target-1, source-1, 1, cost, graph)

        friends, seats = map(int, input().split())
        for i in range(cities):
            for j in range(len(graph[i])):
                if graph[i][j][2] > 0:
                    graph[i][j][2] = seats

        cost = min_cost_flow(0, cities-1, friends, graph)
        print(f'Instancia {test_case}')
        if cost == -1:
            print('impossivel')
        else:
            print(cost)

        test_case += 1
    except EOFError:
        break
