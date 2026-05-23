# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that every edge connects two vertices from different sets. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The function should return true if the graph is bipartite and false otherwise. For example, a graph with 4 vertices and edges between (0, 1), (0, 3), (1, 2), and (2, 3) is bipartite, while a graph with 4 vertices and edges between (0, 1), (0, 2), (1, 2), and (1, 3) is not.

## Approach
The algorithm uses a breadth-first search (BFS) traversal to assign colors to each vertex, where two colors represent the two disjoint sets. If a vertex is assigned a color that is the same as one of its neighboring vertices, the graph is not bipartite.

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
            queue<int> q;
            q.push(i);
            color[i] = 0;

            while (!q.empty()) {
                int node = q.front();
                q.pop();

                for (int neighbor : graph[node]) {
                    if (color[neighbor] == -1) {
                        color[neighbor] = 1 - color[node];
                        q.push(neighbor);
                    } else if (color[neighbor] == color[node]) {
                        return false;
                    }
                }
            }
        }
    }

    return true;
}
```

## Test Cases
```
Input: [[1, 3], [0, 2], [1, 3], [0, 2]]
Output: true

Input: [[1, 2], [0, 2], [0, 1], [1]]
Output: false
```

## Key Takeaways
- A bipartite graph can be represented as two disjoint sets of vertices, where every edge connects two vertices from different sets.
- BFS traversal can be used to assign colors to each vertex and determine if a graph is bipartite.
- The time complexity of this solution is O(V + E), where V is the number of vertices and E is the number of edges.