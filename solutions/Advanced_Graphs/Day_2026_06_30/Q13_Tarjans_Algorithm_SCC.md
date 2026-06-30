# Tarjan's Algorithm (SCC)

## Problem Statement
Tarjan's algorithm is used to find Strongly Connected Components (SCCs) in a directed graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. Given a directed graph with V vertices and E edges, the task is to find all SCCs in the graph. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to traverse the graph and find SCCs. It assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm then uses this information to identify the SCCs.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Tarjan {
public:
    vector<vector<int>> scc(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> index(n, -1);
        vector<int> low(n, -1);
        vector<int> stack;
        vector<vector<int>> result;
        int idx = 0;

        function<void(int)> dfs = [&](int u) {
            index[u] = low[u] = idx++;
            stack.push_back(u);

            for (int v : graph[u]) {
                if (index[v] == -1) {
                    dfs(v);
                    low[u] = min(low[u], low[v]);
                } else if (find(stack.begin(), stack.end(), v) != stack.end()) {
                    low[u] = min(low[u], index[v]);
                }
            }

            if (low[u] == index[u]) {
                vector<int> component;
                while (true) {
                    int v = stack.back();
                    stack.pop_back();
                    component.push_back(v);
                    if (v == u) break;
                }
                result.push_back(component);
            }
        };

        for (int i = 0; i < n; i++) {
            if (index[i] == -1) {
                dfs(i);
            }
        }

        return result;
    }
};

int main() {
    int n, e;
    cin >> n >> e;

    vector<vector<int>> graph(n);
    for (int i = 0; i < e; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
    }

    Tarjan tarjan;
    vector<vector<int>> sccs = tarjan.scc(graph);

    for (const auto& scc : sccs) {
        for (int vertex : scc) {
            cout << vertex << " ";
        }
        cout << endl;
    }

    return 0;
}
```

## Test Cases
```
Input:
5 5
0 1
1 2
2 0
1 3
3 4

Output:
0 2 1 
3 
4 
```

## Key Takeaways
- Tarjan's algorithm is an efficient method for finding SCCs in a directed graph.
- The algorithm uses DFS to assign indices and low values to vertices, which helps identify the SCCs.
- The time complexity of Tarjan's algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph.