from heapq import heappop, heappush

def add_edge(u, v, cap, cost, graph: dict):
    graph[u].append([v, cap, cost, 0])
    graph[v].append([u, 0, -cost, 0])
    return graph

def min_cost_flow(s, t, flow, graph):
    n = len(graph)
    potential = [0]*n
    dist = [float('inf')]*n
    v_prev = [0]*n
    e_prev = [0]*n
    res = 0
    while flow:
        dist = [float('inf')]*n
        dist[s] = 0
        q = [(1, s)]
        while q:
            c, v = heappop(q)
            if dist[v] < c:
                continue
            for i, (w, _, cap, cost) in enumerate(graph[v]):
                if cap > 0 and dist[w] > dist[v] + cost + potential[v] - potential[w]:
                    dist[w] = dist[v] + cost + potential[v] - potential[w]
                    v_prev[w] = v
                    e_prev[w] = i
                    heappush(q, (dist[w], w))
        if dist[t] == float('inf'):
            return -1
        for i in range(n):
            potential[i] += dist[i]
        d = flow
        v = t
        while v != s:
            d = min(d, graph[v_prev[v]][e_prev[v]][2])
            v = v_prev[v]
        flow -= d
        res += d * potential[t]
        v = t
        while v != s:
            e = graph[v_prev[v]][e_prev[v]]
            e[2] -= d
            graph[v][e[1]][2] += d
            v = v_prev[v]
    return res

test_case = 1
while True:
    try:
        vertices, routes = map(int, input().split())
        graph = {vertex: [] for vertex in range(1, vertices+1)}
        for _ in range(routes):
            source, target, cost = map(int, input().split())
            add_edge(source, target, 1, cost, graph)
            add_edge(target, source, 1, cost, graph)

        friends, seats = map(int, input().split())

        for i in range(1, vertices+1):
            for j in range(len(graph[i])):
                w, rev, _, _ = graph[i][j]
                if graph[i][j][2] > 0:
                    graph[i][j][2] = seats

        cost = min_cost_flow(0, vertices-1, friends, graph)

        print(f'Instancia {test_case}')
        if cost == -1:
            print('impossivel')
        else:
            print(cost)
        test_case += 1
    except EOFError:
        break
