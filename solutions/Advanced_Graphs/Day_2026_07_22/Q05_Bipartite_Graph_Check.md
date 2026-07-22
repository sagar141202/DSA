# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite, i.e., its vertices can be divided into two disjoint sets such that every edge connects two vertices from different sets. The graph is represented as an adjacency list. The function should return true if the graph is bipartite and false otherwise. The graph may contain self-loops and multiple edges between the same pair of vertices.

## Approach
To check if a graph is bipartite, we can use a graph traversal algorithm like BFS or DFS and assign colors (0 and 1) to the vertices. If we encounter a vertex that is already colored with the same color as its parent, then the graph is not bipartite.

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
            if (!dfs(graph, color, neighbor, !currColor)) {
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
- A graph is bipartite if and only if it does not contain an odd cycle.
- We can use DFS or BFS to assign colors to the vertices and check for bipartiteness.
- If a graph is bipartite, we can divide its vertices into two disjoint sets such that every edge connects two vertices from different sets.