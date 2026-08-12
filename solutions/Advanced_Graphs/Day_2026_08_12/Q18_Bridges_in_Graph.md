# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph. The input graph is guaranteed to be connected.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify bridges. It keeps track of the discovery time and low value of each node to determine if an edge is a bridge. If the low value of a node is greater than the discovery time of its parent, then the edge between them is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> findBridges(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> discoveryTime(n, -1);
    vector<int> low(n, -1);
    vector<vector<int>> bridges;
    vector<bool> visited(n, false);
    int time = 0;

    function<void(int, int)> dfs = [&](int node, int parent) {
        discoveryTime[node] = low[node] = time++;
        visited[node] = true;

        for (int neighbor : graph[node]) {
            if (neighbor == parent) continue;
            if (!visited[neighbor]) {
                dfs(neighbor, node);
                low[node] = min(low[node], low[neighbor]);
                if (low[neighbor] > discoveryTime[node]) {
                    bridges.push_back({node, neighbor});
                }
            } else {
                low[node] = min(low[node], discoveryTime[neighbor]);
            }
        }
    };

    for (int i = 0; i < n; i++) {
        if (!visited[i]) dfs(i, -1);
    }

    return bridges;
}
```

## Test Cases
```
Input: [[1], [0, 2], [1, 3], [2]]
Output: []
Input: [[1, 2], [0, 2], [0, 1, 3], [2]]
Output: [[1, 2], [2, 3]]
```

## Key Takeaways
- Use DFS to traverse the graph and identify bridges.
- Keep track of the discovery time and low value of each node to determine if an edge is a bridge.
- If the low value of a node is greater than the discovery time of its parent, then the edge between them is a bridge.