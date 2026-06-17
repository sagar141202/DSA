# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to a vertex in V. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The function should return true if the graph is bipartite and false otherwise. For example, a graph with vertices {0, 1, 2} and edges {(0, 1), (1, 2)} is bipartite, but a graph with vertices {0, 1, 2} and edges {(0, 1), (1, 2), (2, 0)} is not.

## Approach
We can solve this problem using a graph traversal algorithm, specifically BFS or DFS, and assign each vertex a color (0 or 1) as we traverse the graph. If we encounter a vertex that has already been assigned a color and it's different from the expected color, we return false. Otherwise, we return true after traversing all vertices.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isBipartite(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> color(n, -1); // -1: unvisited, 0: color 0, 1: color 1

    for (int i = 0; i < n; i++) {
        if (color[i] == -1) { // if vertex is unvisited
            color[i] = 0; // assign color 0
            queue<int> q;
            q.push(i);

            while (!q.empty()) {
                int vertex = q.front();
                q.pop();

                for (int neighbor : graph[vertex]) {
                    if (color[neighbor] == -1) { // if neighbor is unvisited
                        color[neighbor] = 1 - color[vertex]; // assign opposite color
                        q.push(neighbor);
                    } else if (color[neighbor] == color[vertex]) { // if neighbor has same color
                        return false; // graph is not bipartite
                    }
                }
            }
        }
    }

    return true; // graph is bipartite
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
- We can use BFS or DFS to traverse the graph and assign colors to each vertex to check if the graph is bipartite.
- If we encounter a vertex that has already been assigned a color and it's different from the expected color, the graph is not bipartite.