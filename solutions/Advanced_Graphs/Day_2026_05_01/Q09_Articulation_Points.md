# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points. An articulation point is a node in the graph that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list where each index represents a node and its corresponding value is a list of its neighboring nodes. The input graph is connected and has n nodes numbered from 0 to n-1. The function should return a list of all articulation points in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points by tracking the discovery time and low value of each node. A node is an articulation point if it is the root node and has at least two children, or if it is not the root node and has a child that cannot reach any of its ancestors.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> articulationPoints(int n, vector<vector<int>>& connections) {
    vector<int> low(n, -1);
    vector<int> disc(n, -1);
    vector<int> parent(n, -1);
    vector<int> ap(n, 0);
    vector<vector<int>> graph(n);
    int time = 0;

    // Build the graph
    for (auto& connection : connections) {
        graph[connection[0]].push_back(connection[1]);
        graph[connection[1]].push_back(connection[0]);
    }

    // Perform DFS
    function<void(int)> dfs = [&](int u) {
        disc[u] = low[u] = time++;
        int children = 0;
        for (int v : graph[u]) {
            if (disc[v] == -1) {
                parent[v] = u;
                children++;
                dfs(v);
                low[u] = min(low[u], low[v]);
                if (parent[u] == -1 && children > 1) {
                    ap[u] = 1;
                }
                if (parent[u] != -1 && low[v] >= disc[u]) {
                    ap[u] = 1;
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

int main() {
    int n = 5;
    vector<vector<int>> connections = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {1, 4}};
    vector<int> ap = articulationPoints(n, connections);
    for (int point : ap) {
        cout << point << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, connections = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: [1]
```

## Key Takeaways
- Articulation points are critical nodes in a graph that, when removed, increase the number of connected components.
- The algorithm uses DFS to identify articulation points by tracking the discovery time and low value of each node.
- A node is an articulation point if it is the root node and has at least two children, or if it is not the root node and has a child that cannot reach any of its ancestors.