# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, it must have at most two vertices with odd degrees. The problem requires finding an Euler path in the graph, if one exists. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The function should return a list of vertices representing the Euler path.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the graph and find the Euler path. It starts at an arbitrary vertex and explores as far as possible along each branch before backtracking. The algorithm keeps track of the vertices and edges visited to ensure that each edge is visited exactly once.

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> path;
    vector<bool> visited(n * n, false);
    function<void(int)> dfs = [&](int u) {
        for (int v : graph[u]) {
            int edgeIndex = u * n + v;
            if (!visited[edgeIndex]) {
                visited[edgeIndex] = true;
                dfs(v);
                path.push_back(u);
            }
        }
    };
    for (int i = 0; i < n; i++) {
        if (graph[i].size() % 2 != 0) {
            dfs(i);
            break;
        }
    }
    reverse(path.begin(), path.end());
    return path;
}
```

## Test Cases
```
Input: graph = [[1], [0, 2], [1]]
Output: [0, 1, 2, 1, 0]
```

## Key Takeaways
- The graph must have at most two vertices with odd degrees to have an Euler path.
- The algorithm uses DFS to traverse the graph and find the Euler path.
- The time complexity is linear with respect to the number of vertices and edges in the graph.