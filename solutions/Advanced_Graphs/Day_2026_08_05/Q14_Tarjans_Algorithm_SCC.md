# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighbors. The function should return a list of lists, where each sublist contains the vertices of an SCC.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to traverse the graph and find SCCs. It assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm then uses this information to identify the SCCs.

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

    function<void(int)> strongConnect = [&](int u) {
        index[u] = low[u] = idx++;
        stack.push(u);
        onStack[u] = true;

        for (int v : graph[u]) {
            if (index[v] == -1) {
                strongConnect(v);
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
        if (index[i] == -1) strongConnect(i);
    }

    return sccs;
}

int main() {
    // Example usage:
    vector<vector<int>> graph = {{1}, {0, 2}, {1}};
    vector<vector<int>> sccs = tarjanSCC(graph);
    for (auto& scc : sccs) {
        for (int u : scc) cout << u << " ";
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [[1], [0, 2], [1]]
Output: [0 1 2]
Input: [[1, 2], [3], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]
Output: [[0 1 2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]
```

## Key Takeaways
- Tarjan's algorithm is an efficient way to find strongly connected components in a directed graph.
- The algorithm uses a depth-first search approach to traverse the graph and identify SCCs.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges.