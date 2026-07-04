# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge in a graph is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list. The function should return a list of pairs, where each pair represents a bridge in the graph. The input graph is connected and has no self-loops or parallel edges. The number of vertices in the graph is denoted by 'n' and the number of edges is denoted by 'm'. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of all the vertices connected to it.

## Approach
We will use Depth-First Search (DFS) to traverse the graph and keep track of the discovery time and low value for each vertex. The low value of a vertex is the smallest discovery time of any vertex that can be reached from it. If the low value of a vertex is greater than its discovery time, then the edge connecting it to its parent is a bridge.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> findBridges(int n, vector<vector<int>>& graph) {
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> visited(n, false);
    vector<pair<int, int>> bridges;
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
    int n = 5;
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}};
    vector<pair<int, int>> bridges = findBridges(n, graph);
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
graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}}
Output: 
(1, 2)
(2, 3)
```

## Key Takeaways
- The DFS traversal is used to find the discovery time and low value for each vertex.
- The low value of a vertex is updated based on the discovery time of its neighbors.
- If the low value of a vertex is greater than its discovery time, then the edge connecting it to its parent is a bridge.