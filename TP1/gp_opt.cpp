#include <iostream>
#include <vector>
#include <stack>

using namespace std;

long long DFS_MOD(int n_cities, int c_libs, int c_roads, vector<vector<int>>& graph) {
    long long lib_counter = 0;
    vector<bool> visited(n_cities + 1, false);
    for (int city = 1; city <= n_cities; ++city) {
        if (!visited[city]) {
            ++lib_counter;
            stack<int> stack;
            stack.push(city);
            while (!stack.empty()) {
                int current_city = stack.top();
                stack.pop();
                if (!visited[current_city]) {
                    visited[current_city] = true;
                    for (int neighbor : graph[current_city]) {
                        if (!visited[neighbor]) {
                            stack.push(neighbor);
                        }
                    }
                }
            }
        }
    }
    return lib_counter * c_libs + ((long long) visited.size() - 1) * c_roads;
}

long long run_president(int n_cities, int n_roads, int c_libs, int c_roads) {
    if (n_roads == 0) {
        return (long long) c_libs * n_cities;
    }

    vector<vector<int>> graph(n_cities + 1);
    for (int i = 0; i < n_roads; ++i) {
        int s, t;
        cin >> s >> t;
        graph[s].push_back(t);
        graph[t].push_back(s);
    }
    
    if (c_libs <= c_roads) {
        return (long long) c_libs * n_cities;
    }

    return DFS_MOD(n_cities, c_libs, c_roads, graph);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int T;
    cin >> T;
    for (int i = 0; i < T && i < 10; ++i) {
        int n_cities, n_roads, c_libs, c_roads;
        cin >> n_cities >> n_roads >> c_libs >> c_roads;
        cout << run_president(n_cities, n_roads, c_libs, c_roads) << endl;
    }
    return 0;
}
