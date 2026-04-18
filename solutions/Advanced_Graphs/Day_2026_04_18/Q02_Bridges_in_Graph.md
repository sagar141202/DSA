# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge in a graph is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph. The input graph is represented as a 2D vector of integers, where each integer represents a node in the graph. The graph has 'n' nodes numbered from 0 to 'n-1'. The function should return a vector of pairs, where each pair contains two integers representing the nodes of a bridge.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and find the bridges. It uses the concept of low and discovery time to identify the bridges. The low value of a node is the smallest discovery time of any node that is reachable from it. If the low value of a node is greater than its discovery time, then the edge between the node and its parent is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> findBridges(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    vector<int> discoveryTime(n, -1);
    vector<int> low(n, -1);
    vector<vector<int>> bridges;
    int time = 0;

    function<void(int, int)> dfs = [&](int node, int parent) {
        discoveryTime[node] = low[node] = time++;
        for (int neighbor : graph[node]) {
            if (discoveryTime[neighbor] == -1) {
                dfs(neighbor, node);
                low[node] = min(low[node], low[neighbor]);
                if (low[neighbor] > discoveryTime[node]) {
                    bridges.push_back({node, neighbor});
                }
            } else if (neighbor != parent) {
                low[node] = min(low[node], discoveryTime[neighbor]);
            }
        }
    };

    for (int i = 0; i < n; i++) {
        if (discoveryTime[i] == -1) {
            dfs(i, -1);
        }
    }

    return bridges;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: [[1, 3], [1, 4]]
```

## Key Takeaways
- The algorithm uses DFS to traverse the graph and find the bridges.
- The low value of a node is the smallest discovery time of any node that is reachable from it.
- If the low value of a node is greater than its discovery time, then the edge between the node and its parent is a bridge.