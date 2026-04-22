# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge in a graph is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, and the function should return a list of pairs of nodes that form a bridge. The graph can have up to 10^5 nodes and 10^5 edges. For example, in the graph with edges [(0, 1), (1, 2), (2, 0), (1, 3)], the bridge is [(1, 3)].

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and find the bridges. It keeps track of the discovery time and low value of each node to identify the bridges. If the low value of a node is greater than the discovery time of its parent, then the edge between them is a bridge.

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
    int n = 4;
    vector<vector<int>> graph(n);
    graph[0].push_back(1);
    graph[1].push_back(0);
    graph[1].push_back(2);
    graph[2].push_back(1);
    graph[2].push_back(0);
    graph[1].push_back(3);
    graph[3].push_back(1);

    vector<vector<int>> bridges = findBridges(graph);
    for (auto& bridge : bridges) {
        cout << "(" << bridge[0] << ", " << bridge[1] << ")" << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: [(0, 1), (1, 2), (2, 0), (1, 3)]
Output: [(1, 3)]
```

## Key Takeaways
- Use DFS to traverse the graph and find the bridges.
- Keep track of the discovery time and low value of each node to identify the bridges.
- If the low value of a node is greater than the discovery time of its parent, then the edge between them is a bridge.