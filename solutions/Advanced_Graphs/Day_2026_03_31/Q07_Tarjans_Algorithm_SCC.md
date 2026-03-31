# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The input graph is represented as an adjacency list. The graph can contain cycles and self-loops. The goal is to identify all SCCs in the graph and output the vertices in each SCC.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to traverse the graph and identify SCCs. It maintains a stack of vertices and assigns a unique index to each vertex based on the order of visitation. The algorithm also keeps track of the lowest reachable index for each vertex.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> tarjanSCC(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> index(n, -1);
    vector<int> low(n, -1);
    vector<bool> onStack(n, false);
    stack<int> stack;
    vector<vector<int>> sccs;
    int idx = 0;

    function<void(int)> dfs = [&](int u) {
        index[u] = low[u] = idx++;
        stack.push(u);
        onStack[u] = true;

        for (int v : graph[u]) {
            if (index[v] == -1) {
                dfs(v);
                low[u] = min(low[u], low[v]);
            } else if (onStack[v]) {
                low[u] = min(low[u], index[v]);
            }
        }

        if (low[u] == index[u]) {
            vector<int> scc;
            while (true) {
                int v = stack.top();
                stack.pop();
                onStack[v] = false;
                scc.push_back(v);
                if (v == u) break;
            }
            sccs.push_back(scc);
        }
    };

    for (int i = 0; i < n; i++) {
        if (index[i] == -1) {
            dfs(i);
        }
    }

    return sccs;
}

int main() {
    // Example usage:
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2}};
    vector<vector<int>> sccs = tarjanSCC(graph);
    for (const auto& scc : sccs) {
        cout << "SCC: ";
        for (int u : scc) {
            cout << u << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: graph = [[1], [0, 2], [1, 3], [2]]
Output: 
SCC: 0 1 2 3
Input: graph = [[1, 2], [3], [3], [4], [5], [6], [7], [8], [9]]
Output: 
SCC: 0 1 2
SCC: 3
SCC: 4
SCC: 5
SCC: 6
SCC: 7
SCC: 8
SCC: 9
```

## Key Takeaways
- Tarjan's algorithm uses DFS to identify SCCs in a directed graph.
- The algorithm assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex.
- The algorithm uses a stack to keep track of vertices that are currently being visited.