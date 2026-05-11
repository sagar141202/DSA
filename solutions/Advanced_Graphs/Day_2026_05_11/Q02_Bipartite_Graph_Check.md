# Bipartite Graph Check

## Problem Statement
Given an undirected graph, check if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that every edge connects two vertices from different sets. The graph is represented as an adjacency list. The function should return true if the graph is bipartite, and false otherwise. The graph may contain self-loops and multiple edges between the same pair of vertices. The number of vertices in the graph is denoted by 'n' and the number of edges is denoted by 'm'.

## Approach
To check if a graph is bipartite, we can use a graph traversal algorithm such as Breadth-First Search (BFS) or Depth-First Search (DFS) and assign colors to the vertices. If we find an edge that connects two vertices of the same color, the graph is not bipartite.

## Complexity
- Time: O(n + m)
- Space: O(n)

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
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
```

## Key Takeaways
- A bipartite graph can be checked using a graph traversal algorithm such as DFS or BFS.
- Assigning colors to the vertices is a key step in checking if a graph is bipartite.
- The time complexity of the solution is O(n + m), where n is the number of vertices and m is the number of edges.