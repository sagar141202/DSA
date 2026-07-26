# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite, meaning it can be colored using two colors such that no two adjacent vertices have the same color. The graph is represented as an adjacency list where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The function should return true if the graph is bipartite and false otherwise. For example, a graph with 5 vertices and edges between (0,1), (0,4), (1,2), (1,3), (1,4), (2,3), and (3,4) is not bipartite.

## Approach
We will use a depth-first search (DFS) algorithm to traverse the graph and assign colors to each vertex. If we encounter a vertex that has already been assigned a color and it is the same as the current vertex's color, then the graph is not bipartite. We will keep track of the colors using a vector where each index represents a vertex and its corresponding value is the color of that vertex.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isBipartite(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> colors(n, -1);

    for (int i = 0; i < n; i++) {
        if (colors[i] == -1) {
            if (!dfs(graph, colors, i, 0)) {
                return false;
            }
        }
    }

    return true;
}

bool dfs(vector<vector<int>>& graph, vector<int>& colors, int vertex, int color) {
    if (colors[vertex] != -1) {
        return colors[vertex] == color;
    }

    colors[vertex] = color;

    for (int neighbor : graph[vertex]) {
        if (!dfs(graph, colors, neighbor, !color)) {
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

Input: [[1,4], [0,2,3,4], [1,3], [1,2], [0,1,3]]
Output: false
```

## Key Takeaways
- A bipartite graph can be checked using DFS by assigning colors to each vertex.
- If a vertex has already been assigned a color and it is the same as the current vertex's color, then the graph is not bipartite.
- The time complexity is O(V + E) and the space complexity is O(V) where V is the number of vertices and E is the number of edges.