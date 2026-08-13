# Bipartite Graph Check

## Problem Statement
Given an undirected graph, check if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that every edge connects two vertices from different sets. The graph is represented as an adjacency list. The function should return true if the graph is bipartite, and false otherwise. For example, a graph with vertices {0, 1, 2, 3} and edges {(0, 1), (0, 3), (1, 2), (2, 3)} is bipartite.

## Approach
We will use a graph traversal algorithm (BFS or DFS) to assign each vertex a color (0 or 1). If we encounter a vertex that is already colored with the same color as its parent, we return false. Otherwise, we return true.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> color(n, -1);
        
        for (int i = 0; i < n; i++) {
            if (color[i] == -1) {
                if (!dfs(graph, color, i, 0)) return false;
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
            if (!dfs(graph, color, neighbor, !currColor)) return false;
        }
        return true;
    }
};
```

## Test Cases
```
Input: [[1,3],[0,2],[1,3],[0,2]]
Output: true
Input: [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
```

## Key Takeaways
- Use DFS or BFS to traverse the graph and assign colors to vertices.
- If a vertex is already colored with the same color as its parent, the graph is not bipartite.
- The time complexity is O(V + E) where V is the number of vertices and E is the number of edges.