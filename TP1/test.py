from collections import deque

def reverse_number(n):
    return int(str(n)[::-1])

def bfs(a, b):
    visited = [False] * 10000
    dist = [0] * 10000
    queue = deque([a])
    visited[a] = True
    dist[a] = 0
    while queue:
        current = queue.popleft()
        if current == b:
            return dist[current]
        # Adding 1
        if current + 1 < 10000 and not visited[current + 1]:
            queue.append(current + 1)
            visited[current + 1] = True
            dist[current + 1] = dist[current] + 1
        # Reversing
        reversed_current = reverse_number(current)
        if reversed_current < 10000 and not visited[reversed_current]:
            queue.append(reversed_current)
            visited[reversed_current] = True
            dist[reversed_current] = dist[current] + 1

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))