# Bridges in Graph

## Problem Statement
Given an undirected graph, find all bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph. For example, given a graph with 5 nodes and edges between nodes (0, 1), (1, 2), (2, 0), (1, 3), (3, 4), the function should return [(1, 3), (1, 4)].

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and find bridges. It keeps track of the discovery time and low value for each node, and if the low value of a neighboring node is greater than the discovery time of the current node, then the edge between them is a bridge.

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

    vector<int> discoveryTime(n, -1);
    vector<int> low(n, -1);
    vector<vector<int>> bridges;
    int time = 0;

    function<void(int, int)> dfs = [&](int node, int parent) {
        discoveryTime[node] = low[node] = time++;
        for (int neighbor : graph[node]) {
            if (discoveryTime[neighbor] == -1) {
                dfs(neighbor, node);
                low[node] = min(low[node], low[neighbor]);
                if (low[neighbor] > discoveryTime[node]) {
                    bridges.push_back({node, neighbor});
                }
            } else if (neighbor != parent) {
                low[node] = min(low[node], discoveryTime[neighbor]);
            }
        }
    };

    for (int i = 0; i < n; i++) {
        if (discoveryTime[i] == -1) {
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
        cout << "(" << bridge[0] << ", " << bridge[1] << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
Output: [(1, 3), (3, 4)]
```

## Key Takeaways
- Bridges in a graph are edges that, when removed, increase the number of connected components.
- The algorithm uses DFS to traverse the graph and find bridges.
- The discovery time and low value of each node are used to determine if an edge is a bridge.