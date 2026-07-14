# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that every edge connects two vertices from different sets. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The function should return true if the graph is bipartite and false otherwise. The graph may contain self-loops or multiple edges between vertices, but these should be ignored. The input graph is represented as a vector of vectors, where each inner vector represents the neighbors of a vertex.

## Approach
To check if a graph is bipartite, we can use a graph traversal algorithm such as Breadth-First Search (BFS) or Depth-First Search (DFS) and assign each vertex a color (0 or 1) as we traverse the graph. If at any point we encounter a vertex that has already been assigned a color and it is the same as the color of its parent, then the graph is not bipartite.

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

bool dfs(vector<vector<int>>& graph, vector<int>& color, int vertex, int currColor) {
    if (color[vertex] != -1) {
        return color[vertex] != currColor;
    }
    
    color[vertex] = currColor;
    
    for (int neighbor : graph[vertex]) {
        if (!dfs(graph, color, neighbor, 1 - currColor)) {
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
- A bipartite graph can be identified by assigning colors to vertices and ensuring that no two adjacent vertices have the same color.
- BFS or DFS can be used to traverse the graph and assign colors.
- The time complexity of this solution is O(V + E), where V is the number of vertices and E is the number of edges, because we visit each vertex and edge once.