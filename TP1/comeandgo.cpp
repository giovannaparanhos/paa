#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <iterator>

using namespace std;

map<int, vector<int>> add_edge(map<int, vector<int>> graph, int from_x, int to_y, int type) {
    int i = from_x - 1;
    int j = to_y - 1;

    if (type == 1) {
        graph[i].push_back(j);
    } else if (type == 2) {
        if (find(graph[i].begin(), graph[i].end(), j) == graph[i].end()) {
            graph[i].push_back(j);
        }

        if (find(graph[j].begin(), graph[j].end(), i) == graph[j].end()) {
            graph[j].push_back(i);
        }
    }

    if (graph.find(j) == graph.end()) {
        graph[j] = vector<int>();
    }

    return graph;
}
bool DFS_visited(map<int, vector<int>> graph, int u, map<int, bool> &visited) {
    visited[u] = true;
    for (int v : graph[u]) {
        if (!visited[v]) {
            if (!DFS_visited(graph, v, visited)) {
                return false;
            }
        }
    }
    return true;
}

bool DFS(map<int, vector<int>> graph) {
    for (auto u : graph) {
        map<int, bool> visited;
        for (auto v : graph) {
            visited[v.first] = false;
        }
        if (!visited[u.first]) {
            if (!DFS_visited(graph, u.first, visited)) {
                return false;
            }
        }
        for (auto const& x : visited) {
            if(x.second == false) 
                return false;
        }
    }
    return true;
}

int main() {
    int n_edges, from_x, to_y, type;
    map<int, vector<int>> graph;
    while (true) {
        string line;
        getline(cin, line);
        if (line == "0 0") {
            break;
        }

        istringstream iss(line);
        vector<int> nums(istream_iterator<int>{iss}, istream_iterator<int>());
        if (nums.size() == 2) {
            n_edges = nums[1];
            graph.clear();
            for (int i = 0; i < nums[0]; i++) {
                graph[i] = vector<int>();
            }
        } else {
            from_x = nums[0];
            to_y = nums[1];
            type = nums[2];
            graph = add_edge(graph, from_x, to_y, type);
            if (graph.size() == n_edges) {
                cout << DFS(graph) << endl;
            }
        }
    }
    return 0;
}
