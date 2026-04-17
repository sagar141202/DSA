# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. The graph is represented as an adjacency list. The function should return true if the graph is bipartite, and false otherwise. For example, a graph with vertices {0, 1, 2} and edges {(0, 1), (1, 2)} is bipartite, but a graph with vertices {0, 1, 2} and edges {(0, 1), (1, 2), (2, 0)} is not.

## Approach
The algorithm uses a breadth-first search (BFS) traversal to assign colors to each vertex. If a vertex is assigned a color that is the same as its neighbor, the graph is not bipartite. We use a queue to keep track of vertices to visit next. The algorithm iterates through each vertex, assigning colors and checking for conflicts.

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
Input: [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
Output: false
```

## Key Takeaways
- A graph is bipartite if its vertices can be divided into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other set.
- BFS traversal can be used to assign colors to vertices and check for conflicts.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges.