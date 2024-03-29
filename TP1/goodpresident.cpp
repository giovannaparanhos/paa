#include <iostream>
#include <vector>
#include <unordered_set>
#include <stack>

using namespace std;

long long DFS_MOD(int n_cities, int c_libs, int c_roads, vector<unordered_set<int>>& graph) {
    long long lib_counter = 0;
    unordered_set<int> visited;
    for (int city = 1; city <= n_cities; ++city) {
        if (visited.find(city) == visited.end()) {
            ++lib_counter;
            stack<int> stack;
            stack.push(city);
            while (!stack.empty()) {
                int current_city = stack.top();
                stack.pop();
                if (visited.find(current_city) == visited.end()) {
                    visited.insert(current_city);
                    for (int neighbor : graph[current_city]) {
                        if (visited.find(neighbor) == visited.end()) {
                            stack.push(neighbor);
                        }
                    }
                }
            }
        }
    }
    return lib_counter * c_libs + (visited.size() - 1) * c_roads;
}

long long run_president(int n_cities, int n_roads, int c_libs, int c_roads) {
    if (n_roads == 0) {
        return (long long) c_libs * n_cities;
    }

    vector<unordered_set<int>> graph(n_cities + 1);
    for (int i = 0; i < n_roads; ++i) {
        int s, t;
        cin >> s >> t;
        graph[s].insert(t);
        graph[t].insert(s);
    }
    
    if (c_libs <= c_roads) {
        return (long long) c_libs * n_cities;
    }

    return DFS_MOD(n_cities, c_libs, c_roads, graph);
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T && i < 10; ++i) {
        int n_cities, n_roads, c_libs, c_roads;
        cin >> n_cities >> n_roads >> c_libs >> c_roads;
        cout << run_president(n_cities, n_roads, c_libs, c_roads) << endl;
    }
    return 0;
}
