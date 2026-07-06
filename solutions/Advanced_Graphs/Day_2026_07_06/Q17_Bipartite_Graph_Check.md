# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite, i.e., its vertices can be divided into two disjoint sets such that every edge connects two vertices from different sets. The graph is represented as an adjacency list. The function should return true if the graph is bipartite and false otherwise. For example, a graph with vertices {0, 1, 2, 3} and edges {(0, 1), (0, 3), (1, 2), (2, 3)} is bipartite, while a graph with vertices {0, 1, 2} and edges {(0, 1), (1, 2), (2, 0)} is not.

## Approach
The approach is to use a graph traversal algorithm (BFS or DFS) and assign a color to each vertex. If at any point we encounter a vertex that has the same color as one of its neighbors, we return false. Otherwise, we return true.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isBipartite(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> color(n, -1); // -1: not colored, 0: red, 1: blue

    for (int i = 0; i < n; i++) {
        if (color[i] == -1) {
            if (!dfs(graph, color, i, 0)) {
                return false;
            }
        }
    }

    return true;
}

bool dfs(vector<vector<int>>& graph, vector<int>& color, int node, int currColor) {
    if (color[node] != -1) {
        return color[node] == currColor;
    }

    color[node] = currColor;
    for (int neighbor : graph[node]) {
        if (!dfs(graph, color, neighbor, 1 - currColor)) {
            return false;
        }
    }

    return true;
}
```

## Test Cases
```
Input: [[1, 3], [0, 2], [1, 3], [0, 2]]
Output: true
Input: [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
Output: false
```

## Key Takeaways
- A bipartite graph can be checked using a graph traversal algorithm like DFS or BFS.
- We assign a color to each vertex and check if any two adjacent vertices have the same color.
- If we find any two adjacent vertices with the same color, we return false; otherwise, we return true.