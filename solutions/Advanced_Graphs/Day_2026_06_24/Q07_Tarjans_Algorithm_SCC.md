# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The algorithm should output the number of SCCs and the vertices in each SCC.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to find SCCs. It assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm then groups vertices with the same lowest reachable index into the same SCC.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Tarjan {
public:
    vector<vector<int>> scc(const vector<vector<int>>& graph) {
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
            if (index[i] == -1) dfs(i);
        }

        return result;
    }
};

int main() {
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2}};
    Tarjan tarjan;
    vector<vector<int>> sccs = tarjan.scc(graph);

    cout << "Number of SCCs: " << sccs.size() << endl;
    for (int i = 0; i < sccs.size(); i++) {
        cout << "SCC " << i + 1 << ": ";
        for (int vertex : sccs[i]) {
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
Graph: 
0 -> 1
1 -> 0, 2
2 -> 1, 3
3 -> 2

Output: 
Number of SCCs: 1
SCC 1: 0 1 2 3
```

## Key Takeaways
- Tarjan's algorithm uses DFS to find SCCs in a directed graph.
- The algorithm assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex.
- Vertices with the same lowest reachable index are grouped into the same SCC.