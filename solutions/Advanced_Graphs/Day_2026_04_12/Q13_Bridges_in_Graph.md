# Bridges in Graph

## Problem Statement
Given an undirected graph, find all bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph. The graph may contain self-loops and multiple edges between nodes. The input graph is guaranteed to be connected.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and find bridges. It keeps track of the discovery time and low value for each node, and checks if the low value of a neighboring node is greater than the discovery time of the current node.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> findBridges(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<vector<int>> bridges;
    vector<bool> visited(n, false);
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
    // example usage
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2}};
    vector<vector<int>> bridges = findBridges(graph);
    for (auto& bridge : bridges) {
        cout << "(" << bridge[0] << ", " << bridge[1] << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [[1], [0, 2], [1, 3], [2]]
Output: [(1, 2)]
```

## Key Takeaways
- A bridge is an edge that, when removed, increases the number of connected components in the graph.
- The algorithm uses DFS to traverse the graph and find bridges.
- The low value of a node is the smallest discovery time that can be reached from that node.