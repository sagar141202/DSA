# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that every edge connects two vertices from different sets. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The function should return true if the graph is bipartite and false otherwise. For example, a graph with 4 vertices and edges between 0-1, 1-2, 2-3, and 3-0 is not bipartite, while a graph with 4 vertices and edges between 0-1, 0-2, 1-3, and 2-3 is bipartite.

## Approach
The approach involves using a depth-first search (DFS) or breadth-first search (BFS) algorithm to traverse the graph and assign each vertex a color (0 or 1). If a vertex is already colored and we encounter it with a different color, the graph is not bipartite.

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
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
```

## Key Takeaways
- Use DFS or BFS to traverse the graph and assign colors to vertices.
- If a vertex is already colored and we encounter it with a different color, the graph is not bipartite.
- The time complexity is O(V + E), where V is the number of vertices and E is the number of edges.