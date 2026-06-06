# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points. An articulation point is a node in the graph that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, and the function should return a vector of all articulation points. The graph can have up to 10^5 nodes and 10^5 edges. For example, in a graph with nodes {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (1, 3), (1, 4)}, the articulation points are {1}.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and find articulation points. It keeps track of the discovery time and low value of each node to determine if a node is an articulation point. The low value of a node is the smallest discovery time of any node reachable from it.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> articulationPoints(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> ap(n, false);
    vector<int> parent(n, -1);
    vector<int> time(1, 0);
    function<void(int)> dfs = [&](int u) {
        disc[u] = low[u] = time[0]++;
        int child = 0;
        for (int v : graph[u]) {
            if (disc[v] == -1) {
                parent[v] = u;
                child++;
                dfs(v);
                low[u] = min(low[u], low[v]);
                if (parent[u] == -1 && child > 1) {
                    ap[u] = true;
                }
                if (parent[u] != -1 && low[v] >= disc[u]) {
                    ap[u] = true;
                }
            } else if (v != parent[u]) {
                low[u] = min(low[u], disc[v]);
            }
        }
    };

    for (int i = 0; i < n; i++) {
        if (disc[i] == -1) {
            dfs(i);
        }
    }

    vector<int> result;
    for (int i = 0; i < n; i++) {
        if (ap[i]) {
            result.push_back(i);
        }
    }
    return result;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: [1]
```

## Key Takeaways
- Articulation points are nodes that, when removed, increase the number of connected components in the graph.
- The algorithm uses DFS to traverse the graph and find articulation points.
- The low value of a node is used to determine if a node is an articulation point.