# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, and the task is to identify all SCCs in the graph. For example, in a graph with vertices {1, 2, 3, 4} and edges {(1, 2), (2, 3), (3, 1), (4, 4)}, there are two SCCs: {1, 2, 3} and {4}.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to traverse the graph and identify SCCs. The algorithm assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm then uses this information to identify the roots of SCCs and construct the SCCs.

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
        vector<vector<int>> sccs;
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
                vector<int> scc;
                while (true) {
                    int v = stack.back();
                    stack.pop_back();
                    scc.push_back(v);
                    if (v == u) break;
                }
                sccs.push_back(scc);
            }
        };

        for (int i = 0; i < n; i++) {
            if (index[i] == -1) dfs(i);
        }

        return sccs;
    }
};

int main() {
    vector<vector<int>> graph = {{1}, {2}, {0}, {3}, {4}, {5}, {6}, {7}, {}};
    Tarjan tarjan;
    vector<vector<int>> sccs = tarjan.scc(graph);
    for (const auto& scc : sccs) {
        for (int u : scc) cout << u << " ";
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
      0 -> 1
      1 -> 2
      2 -> 0
      3 -> 3
Output: 
      0 1 2 
      3
```

## Key Takeaways
- Tarjan's algorithm uses DFS to traverse the graph and identify SCCs.
- The algorithm assigns a unique index to each vertex based on the order of visitation.
- The algorithm keeps track of the lowest reachable index for each vertex to identify the roots of SCCs.