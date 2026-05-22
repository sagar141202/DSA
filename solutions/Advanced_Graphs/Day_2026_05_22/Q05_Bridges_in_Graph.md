# Bridges in Graph

## Problem Statement
Given an undirected graph, find all bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list. The function should return a list of pairs, where each pair represents a bridge in the graph. The input graph is connected and has no self-loops or multiple edges between any two vertices.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify bridges. It keeps track of the discovery time and low value of each vertex to determine if an edge is a bridge. If the low value of a vertex is greater than the discovery time of its parent, then the edge between them is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> findBridges(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<pair<int, int>> bridges;
    vector<bool> visited(n, false);
    int time = 0;

    function<void(int, int)> dfs = [&](int u, int parent) {
        disc[u] = low[u] = time++;
        visited[u] = true;

        for (int v : graph[u]) {
            if (v == parent) continue;
            if (!visited[v]) {
                dfs(v, u);
                low[u] = min(low[u], low[v]);
                if (low[v] > disc[u]) {
                    bridges.push_back({u, v});
                }
            } else {
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
    // Example usage:
    int n = 5;
    vector<vector<int>> graph(n);
    graph[0].push_back(1);
    graph[1].push_back(0);
    graph[1].push_back(2);
    graph[2].push_back(1);
    graph[2].push_back(3);
    graph[3].push_back(2);
    graph[3].push_back(4);
    graph[4].push_back(3);

    vector<pair<int, int>> bridges = findBridges(graph);
    for (auto& bridge : bridges) {
        cout << "(" << bridge.first << ", " << bridge.second << ")" << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and 4 edges: (0, 1), (1, 2), (2, 3), (3, 4)
Output: 
(2, 3)
(3, 4)
```

## Key Takeaways
- The algorithm uses DFS to traverse the graph and identify bridges.
- It keeps track of the discovery time and low value of each vertex to determine if an edge is a bridge.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph.