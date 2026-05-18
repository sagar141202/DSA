# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is a bipartite graph. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. The graph is represented as an adjacency list. The function should return true if the graph is bipartite, and false otherwise. For example, a graph with vertices {0, 1, 2} and edges {(0, 1), (1, 2), (2, 0)} is not bipartite, but a graph with vertices {0, 1, 2} and edges {(0, 1), (1, 2)} is bipartite.

## Approach
We will use a graph traversal algorithm (BFS or DFS) to assign each vertex a color (0 or 1), ensuring that adjacent vertices have different colors. If we encounter a vertex that cannot be colored without violating this rule, the graph is not bipartite.

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
Input: graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
Output: true

Input: graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
Output: false
```

## Key Takeaways
- A graph is bipartite if and only if it does not contain an odd cycle.
- The coloring approach ensures that adjacent vertices have different colors, which is a necessary condition for a graph to be bipartite.
- The time complexity is O(V + E) because we visit each vertex and edge once.