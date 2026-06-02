# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph. The constraints are: 0 <= numNodes <= 10^5, 0 <= numEdges <= 10^5, and 1 <= u, v <= numNodes.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and find the bridges. It keeps track of the discovery time and low value of each node to identify the bridges. The low value of a node is the smallest discovery time that can be reached from that node.

## Complexity
- Time: O(N + M)
- Space: O(N + M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> findBridges(int numNodes, vector<vector<int>>& edges) {
        vector<vector<int>> graph(numNodes);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        vector<int> discoveryTime(numNodes, -1);
        vector<int> low(numNodes, -1);
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

        for (int i = 0; i < numNodes; i++) {
            if (discoveryTime[i] == -1) {
                dfs(i, -1);
            }
        }

        return bridges;
    }
};
```

## Test Cases
```
Input: numNodes = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: [[1, 3], [1, 4]]
```

## Key Takeaways
- Use DFS to traverse the graph and find the bridges.
- Keep track of the discovery time and low value of each node to identify the bridges.
- The low value of a node is the smallest discovery time that can be reached from that node.