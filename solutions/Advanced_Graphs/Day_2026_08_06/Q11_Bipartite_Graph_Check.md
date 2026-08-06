# Bipartite Graph Check

## Problem Statement
Given an undirected graph, check if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. The graph is represented as an adjacency list. The function should return true if the graph is bipartite, false otherwise. For example, a graph with 2 nodes and 1 edge between them is bipartite, while a graph with 3 nodes and edges between each pair of nodes is not.

## Approach
We use a graph traversal algorithm (BFS or DFS) to assign each vertex a color (0 or 1). If we encounter a vertex that has already been assigned the same color as its neighbor, we return false. Otherwise, we return true after traversing all vertices.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isBipartite(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> color(n, -1);
    
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
    color[node] = currColor;
    
    for (int neighbor : graph[node]) {
        if (color[neighbor] == -1) {
            if (!dfs(graph, color, neighbor, 1 - currColor)) {
                return false;
            }
        } else if (color[neighbor] == currColor) {
            return false;
        }
    }
    
    return true;
}
```

## Test Cases
```
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
```

## Key Takeaways
- A graph is bipartite if and only if it contains no odd cycles.
- We can use BFS or DFS to traverse the graph and assign colors to the vertices.
- If we encounter a vertex that has already been assigned the same color as its neighbor, we can immediately return false.