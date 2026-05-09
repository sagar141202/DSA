# Bridges in Graph

## Problem Statement
Given an undirected graph, find all bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify bridges. It maintains a timer to track the discovery time and low value of each node. If the low value of a neighboring node is greater than the discovery time of the current node, then the edge between them is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> findBridges(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<vector<int>> bridges;
        vector<int> disc(n, -1);
        vector<int> low(n, -1);
        vector<bool> visited(n, false);
        int time = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, -1, graph, bridges, disc, low, visited, time);
            }
        }

        return bridges;
    }

    void dfs(int u, int parent, vector<vector<int>>& graph, vector<vector<int>>& bridges, vector<int>& disc, vector<int>& low, vector<bool>& visited, int& time) {
        visited[u] = true;
        disc[u] = low[u] = time++;
        for (int v : graph[u]) {
            if (!visited[v]) {
                dfs(v, u, graph, bridges, disc, low, visited, time);
                low[u] = min(low[u], low[v]);
                if (low[v] > disc[u]) {
                    bridges.push_back({u, v});
                }
            } else if (v != parent) {
                low[u] = min(low[u], disc[v]);
            }
        }
    }
};

int main() {
    Solution solution;
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2}};
    vector<vector<int>> bridges = solution.findBridges(graph);
    for (auto bridge : bridges) {
        cout << "(" << bridge[0] << ", " << bridge[1] << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: graph = [[1], [0, 2], [1, 3], [2]]
Output: [(1, 3)]
```

## Key Takeaways
- The algorithm uses DFS to traverse the graph and identify bridges.
- The discovery time and low value of each node are used to determine if an edge is a bridge.
- The function returns a list of pairs, where each pair represents a bridge in the graph.