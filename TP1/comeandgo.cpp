#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <string>
#include <sstream>
#include <iterator>
#include <cmath>

using namespace std;

unordered_map<int, unordered_set<int>> build_graph(vector<vector<int>>& testcases) {
    unordered_map<int, unordered_set<int>> graph;
    for (auto& street : testcases) {
        if (street.size() == 3) {
            int v = street[0];
            int w = street[1];
            int p = street[2];
            if (p == 1) {
                graph[v].insert(w);
            } else if (p == 2) {
                graph[v].insert(w);
                graph[w].insert(v);
            }
        }
    }
    return graph;
}

unordered_map<int, unordered_map<string, int>> BFS(unordered_map<int, unordered_set<int>>& graph, int s) {
    unordered_map<int, unordered_map<string, int>> vertices;
    for (auto& u : graph) {
        vertices[u.first]["color"] = 0;
        vertices[u.first]["d"] = pow(graph.size(), 10);
        vertices[u.first]["pi"] = -1;
    }
    vertices[s]["color"] = 1;
    vertices[s]["d"] = 0;
    vertices[s]["pi"] = -1;
    queue<int> Q;
    Q.push(s);
    while (!Q.empty()) {
        int u = Q.front(); Q.pop();
        for (auto& v : graph[u]) {
            if (vertices[v]["color"] == 0) {
                vertices[v]["color"] = 1;
                vertices[v]["d"] = vertices[u]["d"] + 1;
                vertices[v]["pi"] = u;
                Q.push(v);
            }
        }
        vertices[u]["color"] = 2;
    }
    return vertices;
}

int check_connections(unordered_map<int, unordered_map<string, int>>& vertices) {
    for (auto& kv : vertices) {
        if (kv.second["color"] == 0) return 0;
    }
    return 1;
}

void build_testcases(vector<vector<vector<int>>>& testcases) {
    for (auto& testcase : testcases) {
        if (testcase.empty()) continue;
        auto graph = build_graph(testcase);
        if (!graph.empty()) {
            auto vertices = BFS(graph, graph.begin()->first);
            int ok = check_connections(vertices);
            cout << ok << endl;
        }
    }
}

int main() {
    vector<vector<vector<int>>> testcases;
    string line;
    vector<vector<int>> testcase;
    while (getline(cin, line)) {
        istringstream iss(line);
        vector<int> nums((istream_iterator<int>(iss)), istream_iterator<int>());
        if (nums.size() == 2 && nums[0] == 0 && nums[1] == 0) {
            testcases.push_back(testcase);
            testcase.clear();
        } else {
            testcase.push_back(nums);
        }
    }
    if (!testcase.empty()) testcases.push_back(testcase);
    build_testcases(testcases);
    return 0;
}
