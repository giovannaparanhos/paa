#include <iostream>
#include <vector>
#include <set>
#include <algorithm> 
using namespace std;

void add_edge(int i, int j, int type, vector<set<int>>& graph) {
    if (type == 1) {
        graph[i].insert(j);
    } else if (type == 2) {
        graph[i].insert(j);
        graph[j].insert(i);
    }
}

void DFS_visited(int u, vector<bool>& visited, vector<set<int>>& graph) {
    visited[u] = true;
    for (auto v : graph[u]) {
        if (!visited[v]) {
            DFS_visited(v, visited, graph);
        }
    }
}

int DFS(vector<set<int>>& graph) {
    for (int start = 0; start < graph.size(); ++start) {
        vector<bool> visited(graph.size(), false);
        DFS_visited(start, visited, graph);
        if (std::any_of(visited.begin(), visited.end(), [](bool v){ return !v; })) {
            return 0;
        }
    }
    return 1;
}
int main() {
    int vertices, edges;
    while (cin >> vertices >> edges) {
        if (edges == 0) break;
        vector<set<int>> graph(vertices+1);
        for (int i = 0; i < edges; ++i) {
            int source, target, type;
            cin >> source >> target >> type;
            add_edge(source, target, type, graph);
            if (i+1 == edges) {
                cout << DFS(graph) << endl;
            }
        }
    }
    return 0;
}