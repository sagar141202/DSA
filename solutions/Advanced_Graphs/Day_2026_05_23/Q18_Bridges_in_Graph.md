# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph. For example, if we have a graph with 5 nodes and the following edges: (0, 1), (1, 2), (2, 0), (1, 3), (1, 4), then the bridges in the graph are (1, 3) and (1, 4).

## Approach
We will use a depth-first search (DFS) algorithm to find all the bridges in the graph. The algorithm works by assigning a discovery time and a low value to each node, and then checking if the low value of a node is greater than the discovery time of its parent. If it is, then the edge between the node and its parent is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> findBridges(int n, vector<vector<int>>& edges) {
    // Create an adjacency list representation of the graph
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    // Initialize the discovery time and low value for each node
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> visited(n, false);
    int time = 0;
    vector<vector<int>> bridges;

    // Perform DFS to find bridges
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1, graph, disc, low, visited, bridges, time);
        }
    }

    return bridges;
}

void dfs(int u, int parent, vector<vector<int>>& graph, vector<int>& disc, vector<int>& low, vector<bool>& visited, vector<vector<int>>& bridges, int& time) {
    visited[u] = true;
    disc[u] = time;
    low[u] = time;
    time++;

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

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {1, 4}};
    vector<vector<int>> bridges = findBridges(n, edges);
    for (auto& bridge : bridges) {
        cout << "(" << bridge[0] << ", " << bridge[1] << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: (1, 3), (1, 4)
```

## Key Takeaways
- To find bridges in a graph, we need to perform a DFS traversal and keep track of the discovery time and low value for each node.
- A bridge is an edge that, when removed, increases the number of connected components in the graph.
- The algorithm has a time complexity of O(V + E) and a space complexity of O(V), where V is the number of vertices and E is the number of edges in the graph.