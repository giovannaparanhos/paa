#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

long long DFS_MOD(int n_cities, int c_libs, int c_roads, unordered_map<int, vector<int>> &graph) {
    vector<unordered_set<int>> roads_built;
    unordered_set<int> visited;

    for (int city = 1; city <= n_cities; city++) {
        if (visited.find(city) == visited.end()) {
            unordered_set<int> component;
            vector<int> stack = {city};

            while (!stack.empty()) {
                int current_city = stack.back(); stack.pop_back();
                visited.insert(current_city);
                component.insert(current_city);

                for (int neighbor : graph[current_city]) {
                    if (visited.find(neighbor) == visited.end()) {
                        stack.push_back(neighbor);
                    }
                }

                bool isUnique = true;
                for (auto &built : roads_built) {
                    if (built == component) {
                        isUnique = false;
                        break;
                    }
                }

                if (isUnique) {
                    roads_built.push_back(component);
                }
            }
        }
    }

    long long total_cost = 0;
    for (auto &cities_one_lib : roads_built) {
        total_cost += c_libs + ((long long)cities_one_lib.size() - 1) * c_roads;
    }

    return total_cost;
}

long long run_president(int n_cities, int n_roads, int c_libs, int c_roads) {
    unordered_map<int, vector<int>> graph;

    for (int city = 1; city <= n_cities; city++) {
        graph[city] = vector<int>();
    }

    for (int j = 0; j < n_roads; j++) {
        int s, t;
        cin >> s >> t;

        graph[s].push_back(t);
        graph[t].push_back(s);

        if (j == n_roads - 1) {
            if (c_libs > 0 && c_libs <= c_roads) {
                return (long long)c_libs * n_cities;
            }
            return DFS_MOD(n_cities, c_libs, c_roads, graph);
        }
    }

    return 0;
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int n_cities, n_roads, c_libs, c_roads;
        cin >> n_cities >> n_roads >> c_libs >> c_roads;

        cout << run_president(n_cities, n_roads, c_libs, c_roads) << "\n";
    }

    return 0;
}
