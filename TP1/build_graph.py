from collections import defaultdict

def build_testcases(text:str):
    lines = text.strip().split('\n')
    lines = [line.strip().split(' ') for line in lines]
    chunk = []
    testcases = []
    for line in lines:
        if len(line) == 2:
            testcases.append(chunk)
            chunk = []
            chunk.append(line)
        else:
            chunk.append(line)
    testcases.remove([])
    for testcase in testcases:
        build_graph(testcase)


def build_graph(testcases):
    #graph ={}
    for street in testcases:   
        street = list(map(int, street))   
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
            continue

    print(dict(graph))
    return dict(graph)

text = "4 5\n1 2 1\n 1 3 2\n2 4 1\n3 4 1\n4 1 2\n3 2\n1 2 2\n1 3 2\n3 2\n1 2 2\n1 3 1\n4 2\n1 2 2\n3 4 2\n0 0"
#text = "4 2\n1 2 2\n3 4 2\n0 0"
graph = build_testcases(text)
