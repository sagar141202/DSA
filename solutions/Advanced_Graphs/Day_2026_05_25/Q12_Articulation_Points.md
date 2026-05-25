# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a node that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, and the function should return a vector of all articulation points. The graph can have up to 10^5 nodes and edges.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points by checking if the removal of a node increases the number of connected components. The DFS function keeps track of the discovery time and low value of each node to determine if it's an articulation point.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> articulationPoints(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    vector<int> discoveryTime(n, -1);
    vector<int> low(n, -1);
    vector<bool> isArticulationPoint(n, false);
    vector<int> parent(n, -1);
    int time = 0;

    function<void(int)> dfs = [&](int node) {
        discoveryTime[node] = low[node] = time++;
        int childCount = 0;

        for (int neighbor : graph[node]) {
            if (discoveryTime[neighbor] == -1) {
                parent[neighbor] = node;
                childCount++;
                dfs(neighbor);

                low[node] = min(low[node], low[neighbor]);

                if (parent[node] == -1 && childCount > 1) {
                    isArticulationPoint[node] = true;
                }

                if (parent[node] != -1 && low[neighbor] >= discoveryTime[node]) {
                    isArticulationPoint[node] = true;
                }
            } else if (neighbor != parent[node]) {
                low[node] = min(low[node], discoveryTime[neighbor]);
            }
        }
    };

    for (int i = 0; i < n; i++) {
        if (discoveryTime[i] == -1) {
            dfs(i);
        }
    }

    vector<int> result;
    for (int i = 0; i < n; i++) {
        if (isArticulationPoint[i]) {
            result.push_back(i);
        }
    }

    return result;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: [1]
```

## Key Takeaways
- Articulation points are nodes that, when removed, increase the number of connected components in the graph.
- The algorithm uses DFS to traverse the graph and identify articulation points by checking if the removal of a node increases the number of connected components.
- The time complexity of the algorithm is O(V + E), where V is the number of nodes and E is the number of edges in the graph.