# Articulation Points

## Problem Statement
Given a graph, find all articulation points in the graph. An articulation point is a node in the graph that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, and the function should return a list of all articulation points. The graph can have multiple edges between two nodes, and the edges are undirected. The input graph is represented as a list of edges, where each edge is a pair of nodes.

## Approach
The algorithm uses Depth-First Search (DFS) to find articulation points. It keeps track of the discovery time and low value of each node. A node is an articulation point if it has a child with a low value greater than its discovery time, or if it is the root node and has at least two children.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<bool>& visited, 
         vector<int>& disc, vector<int>& low, vector<bool>& articulation, 
         int& time) {
    visited[node] = true;
    disc[node] = low[node] = time++;
    int children = 0;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            children++;
            dfs(neighbor, node, graph, visited, disc, low, articulation, time);
            low[node] = min(low[node], low[neighbor]);
            if (parent != -1 && low[neighbor] >= disc[node]) {
                articulation[node] = true;
            }
        } else if (neighbor != parent) {
            low[node] = min(low[node], disc[neighbor]);
        }
    }
    if (parent == -1 && children > 1) {
        articulation[node] = true;
    }
}

vector<int> findArticulationPoints(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    vector<bool> visited(n, false);
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> articulation(n, false);
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1, graph, visited, disc, low, articulation, time);
        }
    }
    vector<int> result;
    for (int i = 0; i < n; i++) {
        if (articulation[i]) {
            result.push_back(i);
        }
    }
    return result;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: [1]
```

## Key Takeaways
- Articulation points are nodes that, when removed, increase the number of connected components in the graph.
- The algorithm uses DFS to find articulation points by keeping track of the discovery time and low value of each node.
- A node is an articulation point if it has a child with a low value greater than its discovery time, or if it is the root node and has at least two children.