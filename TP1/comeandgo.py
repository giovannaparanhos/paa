from collections import defaultdict

def build_testcases(testcase:str):       
    graph = build_graph(testcase)
    #print(graph)
    source = 1
    vertices = BFS(graph, source)
    ok = check_connections(vertices)
    #print(vertices)
    print(ok)


def build_graph(testcase):
    for street in testcase:   
        if len(street) == 2:
            testcase = street
            n = int(testcase[0])
            m = int(testcase[1])    
            graph = defaultdict(list)
        if n == 0 and m ==0:
            break
        
        if len(street) == 3:
            # vertex v
            v = street[0]
            # vertex w
            w = street[1]
            #adjacency type
            p = street[2]
            # pair vw is one-way v->w if 1, 
            # two-way v<=>w if 2
            if p == 1:
                graph[v].append(w)

            elif p ==2:
                if w not in graph[v]:
                    graph[v].append(w)

                if v not in graph[w]: 
                    graph[w].append(v)
            if w not in graph.keys():
                graph[w] = []
            continue
    return dict(graph)

def BFS(graph:dict, s):
    '''Breadth-First Search
    Parameters
    --------
    graph: dict
        Graph with Vertices V
    s: int or str
        source s'''
    vertices = {}
    for u in graph.keys():
        vertices[u] = {}
        vertices[u]['color'] = 'white'
        vertices[u]['d'] = len(graph.keys())**10
        vertices[u]['pi'] = None
    vertices[s]['color'] = 'gray'
    vertices[s]['d'] = 0
    vertices[s]['pi'] = None
    Q = []
    Q.append(s) #enqueue s
    while len(Q) != 0:
        u = Q.pop(0) #dequeue Q
        for v in graph[u]:
            if vertices[v]['color'] == 'white':
                vertices[v]['color'] = 'gray'
                vertices[v]['d'] = vertices[u]['d'] + 1
                vertices[v]['pi'] = u
                Q.append(v) #enqueue(Q, v)
        vertices[u]['color'] = 'black'
        if len(graph[u]) == 0:
            vertices[u]['color'] = 'gray'
    return vertices
    
def check_connections(vertices):
    for key in vertices:
        if vertices[key]['color'] == 'white':
            return 0
        elif vertices[key]['color'] == 'gray':
            return 0
    return 1


testcase = []
while True:
    line = input()
    line = line.strip().split(' ')
    line = list(map(int, line)) 
    
    if len(line) == 2 and len(testcase) > 1:        
        build_testcases(testcase)
        testcase = []
    
    if line == [0, 0]: break
    testcase.append(line)  


