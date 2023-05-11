from collections import defaultdict

def build_testcases(v, testcase:str):
    weights = build_matrix(v, 1) #equal weights
    graph = build_graph(testcase)
    #print(graph)
    

    #print(vertices)
    print(ok)

def build_matrix(n, value = 0):
    line = n*[value]
    matrix = n*[line]
    return matrix

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


    
def floyd_warshall(W):
    pass

testcase = []
while True:
    line = input()
    line = line.strip().split(' ')
    line = list(map(int, line)) 
    
    if len(line) == 2:
        n_vertices = line[0]
        if len(testcase) > 1:        
            build_testcases(testcase)
            testcase = []
    
    if line == [0, 0]: break
    testcase.append(line)  


