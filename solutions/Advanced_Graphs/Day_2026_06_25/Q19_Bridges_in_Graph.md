# Bridges in Graph

## Problem Statement
Given an undirected graph, find all bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The graph has n nodes and m edges. For example, given a graph with 5 nodes and 6 edges: [(0, 1), (1, 2), (2, 0), (1, 3), (1, 4)], the bridges are [(1, 3), (1, 4)]. The function should return a list of all bridges in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and find bridges. It maintains a discovery time and low value for each node, and an edge is a bridge if the low value of the adjacent node is greater than the discovery time of the current node. The algorithm iterates over all nodes and edges to find all bridges.

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> findBridges(int n, vector<vector<int>> edges) {
    vector<vector<int>> graph(n);
    for (auto edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> visited(n, false);
    vector<vector<int>> bridges;
    int time = 0;

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1, disc, low, visited, bridges, graph, time);
        }
    }

    return bridges;
}

void dfs(int u, int parent, vector<int>& disc, vector<int>& low, vector<bool>& visited, vector<vector<int>>& bridges, vector<vector<int>>& graph, int& time) {
    disc[u] = low[u] = time++;
    visited[u] = true;

    for (int v : graph[u]) {
        if (!visited[v]) {
            dfs(v, u, disc, low, visited, bridges, graph, time);
            low[u] = min(low[u], low[v]);
            if (low[v] > disc[u]) {
                bridges.push_back({u, v});
            }
        } else if (v != parent) {
            low[u] = min(low[u], disc[v]);
        }
    }
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {1, 4}};
    vector<vector<int>> bridges = findBridges(n, edges);
    for (auto bridge : bridges) {
        cout << "(" << bridge[0] << ", " << bridge[1] << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, edges = [(0, 1), (1, 2), (2, 0), (1, 3), (1, 4)]
Output: [(1, 3), (1, 4)]
```

## Key Takeaways
- The algorithm uses DFS to find bridges in the graph.
- It maintains a discovery time and low value for each node to detect bridges.
- The time complexity is O(V + E), where V is the number of nodes and E is the number of edges.