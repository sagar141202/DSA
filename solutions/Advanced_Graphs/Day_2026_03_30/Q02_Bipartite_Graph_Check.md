# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite, i.e., its vertices can be divided into two disjoint sets such that every edge connects two vertices from different sets. The graph is represented as an adjacency list. The function should return true if the graph is bipartite and false otherwise. The graph has n vertices and m edges. 1 ≤ n ≤ 10^5, 1 ≤ m ≤ 10^5.

## Approach
We will use a graph traversal algorithm (BFS or DFS) to assign each vertex a color (0 or 1) such that adjacent vertices have different colors. If we encounter an edge that connects two vertices of the same color, the graph is not bipartite.

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
        if (!dfs(graph, color, neighbor, !currColor)) {
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
- We can use DFS or BFS to check if a graph is bipartite by assigning colors to vertices.
- The time complexity of the algorithm is linear with respect to the number of vertices and edges.