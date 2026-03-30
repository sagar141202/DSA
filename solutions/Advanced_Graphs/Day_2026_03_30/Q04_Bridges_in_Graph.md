# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge in a graph is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list and has V vertices and E edges. The task is to find all the bridges in the graph and return them as a list of pairs of vertices. The graph does not contain self-loops or multiple edges between any two vertices. The input graph is connected.

## Approach
The approach to solve this problem is to use Depth-First Search (DFS) and keep track of the discovery time and low value of each vertex. The low value of a vertex is the minimum discovery time of any vertex that is reachable from it. If the low value of a vertex is greater than the discovery time of its parent, then the edge between the vertex and its parent is a bridge.

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

vector<pair<int, int>> findBridges(int V, vector<vector<int>>& graph) {
    vector<int> disc(V, -1);
    vector<int> low(V, -1);
    vector<bool> visited(V, false);
    vector<pair<int, int>> bridges;
    int time = 0;
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            dfs(i, -1, graph, disc, low, visited, bridges, time);
        }
    }
    return bridges;
}

int main() {
    int V = 5;
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}};
    vector<pair<int, int>> bridges = findBridges(V, graph);
    for (auto bridge : bridges) {
        cout << "(" << bridge.first << ", " << bridge.second << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and edges: (0, 1), (1, 2), (2, 3), (3, 4)
Output: 
(2, 3)
```

## Key Takeaways
- The DFS traversal is used to find the bridges in the graph.
- The discovery time and low value of each vertex are used to determine if an edge is a bridge.
- The low value of a vertex is the minimum discovery time of any vertex that is reachable from it.