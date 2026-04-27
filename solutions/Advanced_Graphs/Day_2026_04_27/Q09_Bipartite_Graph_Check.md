# Bipartite Graph Check

## Problem Statement
Given an undirected graph, check if it is a bipartite graph. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. The graph is represented as an adjacency list. The function should return true if the graph is bipartite, false otherwise. The graph can have multiple connected components. The number of vertices in the graph is in the range [1, 1000] and the number of edges is in the range [0, 10000].

## Approach
We will use a graph traversal algorithm (BFS or DFS) to assign each vertex a color (0 or 1) and check if any edge connects two vertices of the same color. If we find such an edge, we return false. Otherwise, we return true after checking all vertices.

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
- A bipartite graph can be checked using a graph traversal algorithm like DFS or BFS.
- We can use a color array to keep track of the color of each vertex.
- If we find an edge that connects two vertices of the same color, we return false. Otherwise, we return true after checking all vertices.