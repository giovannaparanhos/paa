from collections import defaultdict


def build_testcases(testcase:str):       
    graph = build_graph(testcase)
    #print(graph)
    source = 1
   
    #print(vertices)
    print(ok)


def build_graph(testcases):
    for street in testcases:   
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



if __name__ == '__main__':
    maps = 0
    while True:
        line = input()
        line = line.strip().split(' ')
        line = list(map(int, line)) 
        if len(line) == 1:
            p_maps = line[0] 
        if len(line) == 4:
            curr_map = dict()
            n_cities = line[0]
            m_libraries = line[1]
            b_cost_lib = line[2]
            e_cost_road = line[3]
            maps += 1
        while len(line) == 2:
            city_x = line[0]
            city_y = line[1]
            
        if maps > p_maps:
            exit
    
    
