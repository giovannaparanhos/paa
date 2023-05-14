from collections import deque

def BFS_MOD(s: int, t: int):
    '''Breadth-First Search
    Parameters
    --------
    s: int
        source s
    t: int
        target t
    '''
    n_visited = [False]*10000
    distance_s = [0]*10000
    n_visited[s] = True
    distance_s[s] = 0
    Q = deque([s])
    while Q:
        u = Q.popleft() #dequeue Q
        if u == t:
            return distance_s[t]
        u_add =  u+1
        if u_add < 10000 and not n_visited[u_add]:
            Q.append(u_add)
            n_visited[u_add] = True
            distance_s[u_add] = distance_s[u]+1
        u_rev = reverse(u)
        if u_rev<10000 and not n_visited[u_rev]:
            Q.append(u_rev)
            distance_s[u_rev] = distance_s[u] + 1
            n_visited[u_rev] = True
            

def reverse(n: str):
    n_str = str(n) #enforce type
    n_rev = n_str[::-1]
    return int(n_rev)

T = int(input())

for i in range(T):
    s, t = map(int, input().split())
    n_press = BFS_MOD(s,t)
    print(n_press)