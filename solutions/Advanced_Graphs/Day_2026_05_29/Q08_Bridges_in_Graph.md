# Bridges in Graph

## Problem Statement
Given an undirected graph, find all bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph. For example, if the input graph is represented as `{0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}`, the function should return `[(2, 3), (3, 4)]`, which are the bridges in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify bridges. It keeps track of the discovery time and low value of each node, and checks if the low value of a neighboring node is greater than the discovery time of the current node.

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
        vector<int> disc(n, -1);
        vector<int> low(n, -1);
        vector<vector<int>> bridges;
        int time = 0;

        // Perform DFS traversal
        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, -1, disc, low, bridges, graph, time);
            }
        }

        return bridges;
    }

    void dfs(int u, int parent, vector<int>& disc, vector<int>& low, vector<vector<int>>& bridges, vector<vector<int>>& graph, int& time) {
        disc[u] = low[u] = time++;
        for (int v : graph[u]) {
            if (disc[v] == -1) {
                dfs(v, u, disc, low, bridges, graph, time);
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
    vector<vector<int>> graph = {{1, 2}, {0, 2}, {0, 1, 3}, {2, 4}, {3}};
    vector<vector<int>> bridges = solution.findBridges(graph);
    for (auto bridge : bridges) {
        cout << "(" << bridge[0] << ", " << bridge[1] << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}
Output: [(2, 3), (3, 4)]
```

## Key Takeaways
- The algorithm uses DFS to traverse the graph and identify bridges.
- The discovery time and low value of each node are used to determine if an edge is a bridge.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges.