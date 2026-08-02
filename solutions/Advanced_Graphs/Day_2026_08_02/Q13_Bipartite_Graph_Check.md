# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to a vertex in V. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The function should return true if the graph is bipartite and false otherwise. The graph can have up to 100 vertices and 1000 edges.

## Approach
The approach is to use a graph traversal algorithm (BFS or DFS) to assign each vertex a color (0 or 1) such that no two adjacent vertices have the same color. If we encounter a vertex that is already colored with the same color as its parent, we return false. Otherwise, we return true after traversing the entire graph.

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
        if (color[i] == -1) {
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
        if (color[neighbor] == -1) {
            if (!dfs(graph, color, neighbor, 1 - currColor)) {
                return false;
            }
        } else if (color[neighbor] == currColor) {
            return false;
        }
    }

    return true;
}

int main() {
    // example usage
    vector<vector<int>> graph = {{1, 3}, {0, 2}, {1, 3}, {0, 2}};
    cout << boolalpha << isBipartite(graph) << endl; // true

    return 0;
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
- A bipartite graph can be checked using a graph traversal algorithm (BFS or DFS) with a color assignment approach.
- The time complexity is O(V + E) and the space complexity is O(V), where V is the number of vertices and E is the number of edges.
- The algorithm returns true if the graph is bipartite and false otherwise.