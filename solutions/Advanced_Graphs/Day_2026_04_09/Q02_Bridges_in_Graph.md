# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the graph and identify bridges. It keeps track of the discovery time and low value of each node to determine if an edge is a bridge. If the low value of a neighboring node is greater than the discovery time of the current node, then the edge between them is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> findBridges(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<vector<int>> bridges;
    int time = 0;

    function<void(int, int)> dfs = [&](int u, int parent) {
        disc[u] = low[u] = time++;
        for (int v : graph[u]) {
            if (disc[v] == -1) {
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

    for (int i = 0; i < n; i++) {
        if (disc[i] == -1) {
            dfs(i, -1);
        }
    }

    return bridges;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {3, 4}};
    vector<vector<int>> bridges = findBridges(n, edges);
    for (auto& bridge : bridges) {
        cout << bridge[0] << " " << bridge[1] << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
Output: [[1, 3], [3, 4]]
```

## Key Takeaways
- The algorithm uses DFS to traverse the graph and identify bridges.
- The discovery time and low value of each node are used to determine if an edge is a bridge.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges.