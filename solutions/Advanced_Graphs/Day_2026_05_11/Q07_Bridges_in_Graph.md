# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph. For example, given a graph with 5 nodes and edges between nodes (0, 1), (1, 2), (2, 0), (1, 3), (3, 4), the function should return [(1, 3), (3, 4)] as these are the bridges in the graph.

## Approach
The approach to find bridges in a graph is to use a Depth-First Search (DFS) traversal and keep track of the discovery time and low value of each node. If the low value of a neighboring node is greater than the discovery time of the current node, then the edge between them is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<int>& disc, vector<int>& low, vector<pair<int, int>>& bridges, int& time) {
    disc[node] = low[node] = time++;
    for (int neighbor : graph[node]) {
        if (disc[neighbor] == -1) {
            dfs(neighbor, node, graph, disc, low, bridges, time);
            low[node] = min(low[node], low[neighbor]);
            if (low[neighbor] > disc[node]) {
                bridges.push_back({node, neighbor});
            }
        } else if (neighbor != parent) {
            low[node] = min(low[node], disc[neighbor]);
        }
    }
}

vector<pair<int, int>> findBridges(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (vector<int>& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<pair<int, int>> bridges;
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (disc[i] == -1) {
            dfs(i, -1, graph, disc, low, bridges, time);
        }
    }
    return bridges;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
Output: [(1, 3), (3, 4)]
```

## Key Takeaways
- The DFS traversal is used to find bridges in the graph.
- The discovery time and low value of each node are used to determine if an edge is a bridge.
- The time complexity of the solution is O(V + E), where V is the number of nodes and E is the number of edges in the graph.