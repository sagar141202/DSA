# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph. For example, given a graph with 5 nodes and edges [(0, 1), (1, 2), (2, 0), (1, 3), (1, 4)], the function should return [(1, 3), (1, 4)] as these are the bridges in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and find the bridges. It keeps track of the discovery time and low value of each node, and checks if the low value of a neighboring node is greater than the discovery time of the current node.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> findBridges(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> visited(n, false);
    vector<pair<int, int>> bridges;
    int time = 0;

    function<void(int, int)> dfs = [&](int u, int parent) {
        disc[u] = low[u] = time++;
        visited[u] = true;

        for (int v : graph[u]) {
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

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1);
        }
    }

    return bridges;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {1, 4}};
    vector<pair<int, int>> bridges = findBridges(n, edges);
    for (auto& bridge : bridges) {
        cout << "(" << bridge.first << ", " << bridge.second << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
n = 5
edges = [(0, 1), (1, 2), (2, 0), (1, 3), (1, 4)]
Output: 
(1, 3)
(1, 4)
```

## Key Takeaways
- A bridge in a graph is an edge that, when removed, increases the number of connected components.
- The algorithm uses DFS to traverse the graph and find the bridges.
- The discovery time and low value of each node are used to determine if an edge is a bridge.