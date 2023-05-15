#include <iostream>
#include <vector>
#include <set>
#include <stack>
#include <algorithm> 
using namespace std;
void add_edge(int i, int j, int type, vector<set<int>>& graph) {
    graph[i].insert(j);
    if (type == 2) {
        graph[j].insert(i);
    } 
}

void DFS_visited(int start, vector<bool>& visited, vector<set<int>>& graph) {
    stack<int> stack;
    stack.push(start);
    while (!stack.empty()) {
        int u = stack.top();
        stack.pop();
        if (!visited[u]) {
            visited[u] = true;
            for (auto v : graph[u]) {
                if (!visited[v]) {
                    stack.push(v);
                }
            }
        }
    }
}

int DFS(vector<set<int>>& graph) {
    for (int start = 1; start < graph.size(); ++start) {
        vector<bool> visited(graph.size(), false);
        DFS_visited(start, visited, graph);
        if (std::any_of(visited.begin()+1, visited.end(), [](bool v){ return !v; })) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int vertices, edges;
    while (cin >> vertices >> edges) {
        if (edges == 0 || vertices == 0) break;
        vector<set<int>> graph(vertices+1);
        for (int i = 0; i < edges; ++i) {
            int source, target, type;
            cin >> source >> target >> type;
            add_edge(source, target, type, graph);
        }
        cout << DFS(graph) << endl;
    }
    return 0;
}