# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is a bipartite graph. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The function should return true if the graph is bipartite and false otherwise. For example, given a graph with 6 vertices and edges between (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), the function should return false because the graph contains an odd cycle.

## Approach
The approach is to use a graph traversal algorithm (BFS or DFS) to assign each vertex a color (0 or 1) and check if any adjacent vertices have the same color. If a vertex has not been colored yet, assign it the opposite color of its parent. If a vertex has already been colored and its color is the same as its parent, return false.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isBipartite(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> color(n, -1); // -1: not colored, 0: color 0, 1: color 1

    for (int i = 0; i < n; i++) {
        if (color[i] == -1) { // not colored yet
            if (!dfs(graph, color, i, 0)) {
                return false;
            }
        }
    }
    return true;
}

bool dfs(vector<vector<int>>& graph, vector<int>& color, int vertex, int currColor) {
    color[vertex] = currColor;
    for (int neighbor : graph[vertex]) {
        if (color[neighbor] == -1) { // not colored yet
            if (!dfs(graph, color, neighbor, 1 - currColor)) {
                return false;
            }
        } else if (color[neighbor] == currColor) { // same color
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
- A bipartite graph can be checked using a graph traversal algorithm (BFS or DFS) with a coloring approach.
- The time complexity of the solution is O(V + E), where V is the number of vertices and E is the number of edges.
- The space complexity of the solution is O(V), where V is the number of vertices.