# Bipartite Graph Check

## Problem Statement
Given an undirected graph, check if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that every edge connects two vertices from different sets. The graph is represented as an adjacency list where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The function should return true if the graph is bipartite and false otherwise. The graph can have up to 100 vertices and 1000 edges. For example, a graph with vertices {0, 1, 2} and edges {(0, 1), (1, 2), (2, 0)} is not bipartite because there is no way to divide the vertices into two disjoint sets such that every edge connects two vertices from different sets.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the graph and assign colors to each vertex. If a vertex is assigned a color that is the same as one of its neighboring vertices, then the graph is not bipartite. The DFS approach ensures that all vertices are visited and assigned a color.

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
};
```

## Test Cases
```
Input: graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
Output: true
```

## Key Takeaways
- Use DFS to traverse the graph and assign colors to each vertex.
- If a vertex is assigned a color that is the same as one of its neighboring vertices, then the graph is not bipartite.
- The time complexity is O(V + E) because each vertex and edge is visited once.