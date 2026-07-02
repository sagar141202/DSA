# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The graph may contain self-loops and multiple edges between the same pair of nodes. The task is to identify all the bridges in the given graph and return them as a list of pairs, where each pair represents the nodes connected by a bridge.

## Approach
The approach to finding bridges in a graph involves using a depth-first search (DFS) algorithm to traverse the graph and identify the bridges. The algorithm uses the concept of low values and discovery times to detect bridges. The low value of a node is the smallest discovery time of any node that is reachable from it. If the low value of a node is greater than its discovery time, then the edge connecting it to its parent is a bridge.

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
    int time = 0;

    function<void(int, int)> dfs = [&](int u, int parent) {
        disc[u] = low[u] = time++;
        for (int v : graph[u]) {
            if (disc[v] == -1) {
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
        if (disc[i] == -1) {
            dfs(i, -1);
        }
    }

    return bridges;
}

int main() {
    int n = 5;
    vector<vector<int>> graph(n);
    graph[0].push_back(1);
    graph[1].push_back(0);
    graph[1].push_back(2);
    graph[2].push_back(1);
    graph[1].push_back(3);
    graph[3].push_back(1);
    graph[3].push_back(4);
    graph[4].push_back(3);

    vector<vector<int>> bridges = findBridges(graph);
    for (auto& bridge : bridges) {
        cout << "(" << bridge[0] << ", " << bridge[1] << ")" << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 nodes and 6 edges: (0, 1), (1, 2), (2, 1), (1, 3), (3, 4), (4, 3)
Output: 
(1, 3)
(3, 4)
```

## Key Takeaways
- The algorithm uses DFS to traverse the graph and identify bridges.
- The low value of a node is used to detect bridges.
- The algorithm has a time complexity of O(V + E) and a space complexity of O(V).