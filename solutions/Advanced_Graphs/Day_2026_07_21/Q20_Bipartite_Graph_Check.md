# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that every edge connects two vertices from different sets. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of vertices connected to it. The function should return true if the graph is bipartite and false otherwise. For example, a graph with vertices 0, 1, 2, and 3, and edges (0, 1), (0, 3), (1, 2), and (2, 3) is not bipartite, while a graph with vertices 0, 1, 2, and 3, and edges (0, 1), (0, 3), and (1, 2) is bipartite.

## Approach
To solve this problem, we can use a graph traversal algorithm such as Breadth-First Search (BFS) or Depth-First Search (DFS) to assign each vertex a color (0 or 1). We start with an arbitrary vertex and assign it a color. Then, we traverse the graph and assign the opposite color to each of its neighbors. If we encounter a vertex that has already been assigned a color and it is the same as the current vertex, then the graph is not bipartite.

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
Input: [[1, 3], [0, 2], [1, 3], [0, 2]]
Output: false
Input: [[1, 3], [0, 2], [1], [0]]
Output: true
```

## Key Takeaways
- A bipartite graph can be checked using graph traversal algorithms like DFS or BFS.
- Assigning colors to vertices is a common approach to solving bipartite graph problems.
- The time complexity of this solution is O(V + E), where V is the number of vertices and E is the number of edges.