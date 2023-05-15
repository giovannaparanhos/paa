#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> build_matrix(int n, int value = 0) {
    vector<vector<int>> matrix(n, vector<int>(n, value));
    return matrix;
}

void add_edge(int i, int j, int type, vector<vector<int>>& graph) {
    graph[i][j] = 1;
    if (type == 2) {
        graph[j][i] = 1;
    }
}

void DFS_visited(int u, vector<bool>& visited, vector<vector<int>>& graph) {
    visited[u] = true;
    for (int v = 0; v < graph.size(); ++v) {
        if (graph[u][v] == 1 && !visited[v]) {
            DFS_visited(v, visited, graph);
        }
    }
}

int DFS(vector<vector<int>>& graph) {
    for (int start = 0; start < graph.size(); ++start) {
        vector<bool> visited(graph.size(), false);
        DFS_visited(start, visited, graph);
        
        bool found = false;
        for (bool v : visited) {
            if (!v) {
                found = true;
                break;
            }
        }
        if (found) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int vertices, edges;
    while (cin >> vertices >> edges) {
        if (edges == 0 || vertices == 0) break;
        auto graph = build_matrix(vertices);
        for (int i = 0; i < edges; ++i) {
            int source, target, type;
            cin >> source >> target >> type;
            add_edge(source-1, target-1, type, graph);
        }
        cout << DFS(graph) << endl;
    }
    return 0;
}
