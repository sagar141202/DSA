# Bridges in Graph

## Problem Statement
Given an undirected graph, find all bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph. The input graph is guaranteed to be connected.

## Approach
The algorithm uses a depth-first search (DFS) to traverse the graph and identify bridges. It keeps track of the discovery time and low value of each node, and checks if the low value of a neighboring node is greater than the discovery time of the current node. If so, the edge between the current node and the neighboring node is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> findBridges(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<vector<int>> bridges;
    int time = 0;

    function<void(int, int)> dfs = [&](int u, int parent) {
        disc[u] = low[u] = time++;
        for (int v : graph[u]) {
            if (disc[v] == -1) {
                dfs(v, u);
                low[u] = min(low[u], low[v]);
                if (low[v] > disc[u]) {
                    bridges.push_back({u, v});
                }
            } else if (v != parent) {
                low[u] = min(low[u], disc[v]);
            }
        }
    };

    for (int i = 0; i < n; i++) {
        if (disc[i] == -1) {
            dfs(i, -1);
        }
    }

    return bridges;
}
```

## Test Cases
```
Input: [[1], [0, 2], [1]]
Output: []
Input: [[1, 2], [0, 2], [0, 1]]
Output: []
Input: [[1], [0, 2, 3], [1], [1]]
Output: [[1, 3], [1, 2]]
```

## Key Takeaways
- Bridges in a graph are edges that, when removed, increase the number of connected components.
- The algorithm uses DFS to identify bridges by comparing the discovery time and low value of each node.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges.