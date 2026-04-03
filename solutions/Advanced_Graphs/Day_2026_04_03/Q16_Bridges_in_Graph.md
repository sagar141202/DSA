# Bridges in Graph

## Problem Statement
Given an undirected graph with V vertices and E edges, find all the bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list. The function should return a vector of pairs, where each pair represents a bridge in the graph. The vertices are numbered from 0 to V-1. The graph does not contain self-loops or multiple edges between any two vertices.

## Approach
The algorithm uses a depth-first search (DFS) to traverse the graph and find the bridges. It keeps track of the discovery time and low value of each vertex to determine if an edge is a bridge. If the low value of a vertex is greater than the discovery time of its parent, then the edge between them is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> findBridges(int V, vector<vector<int>>& adj) {
    vector<int> disc(V, -1);
    vector<int> low(V, -1);
    vector<bool> visited(V, false);
    vector<pair<int, int>> bridges;
    int time = 0;

    function<void(int, int)> dfs = [&](int u, int parent) {
        disc[u] = low[u] = time++;
        visited[u] = true;

        for (int v : adj[u]) {
            if (!visited[v]) {
                dfs(v, u);
                low[u] = min(low[u], low[v]);
                if (low[v] > disc[u]) {
                    bridges.push_back({u, v});
                }
            } else if (v != parent) {
                low[u] = min(low[u], disc[v]);
            }
        }
    };

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            dfs(i, -1);
        }
    }

    return bridges;
}

int main() {
    int V = 5;
    vector<vector<int>> adj = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}};
    vector<pair<int, int>> bridges = findBridges(V, adj);
    for (auto& bridge : bridges) {
        cout << "(" << bridge.first << ", " << bridge.second << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: V = 5, adj = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}}
Output: (2, 4)
```

## Key Takeaways
- The algorithm uses DFS to traverse the graph and find the bridges.
- The discovery time and low value of each vertex are used to determine if an edge is a bridge.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges.