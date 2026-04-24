# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge in a graph is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list. The function should return a list of pairs, where each pair represents a bridge in the graph.

## Approach
The approach to find bridges in a graph involves using Depth-First Search (DFS) to traverse the graph and keep track of the discovery time and low value of each vertex. If the low value of a vertex is greater than the discovery time of its parent, then the edge between the vertex and its parent is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int u, int parent, vector<vector<int>>& graph, vector<int>& disc, vector<int>& low, vector<bool>& visited, vector<pair<int, int>>& bridges, int& time) {
    disc[u] = low[u] = time++;
    visited[u] = true;
    for (int v : graph[u]) {
        if (!visited[v]) {
            dfs(v, u, graph, disc, low, visited, bridges, time);
            low[u] = min(low[u], low[v]);
            if (low[v] > disc[u]) {
                bridges.push_back({u, v});
            }
        } else if (v != parent) {
            low[u] = min(low[u], disc[v]);
        }
    }
}

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
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1, graph, disc, low, visited, bridges, time);
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
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: [(1, 3), (1, 4)]
```

## Key Takeaways
- The discovery time and low value of each vertex are used to determine if an edge is a bridge.
- The low value of a vertex is the minimum discovery time of all vertices reachable from it.
- If the low value of a vertex is greater than the discovery time of its parent, then the edge between the vertex and its parent is a bridge.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph.