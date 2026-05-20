# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a node that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, and the nodes are numbered from 1 to n. The function should return a vector of all articulation points in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points. It keeps track of the discovery time and low value of each node to determine if a node is an articulation point. A node is an articulation point if it has at least two children and the low value of one of its children is greater than or equal to its discovery time.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> articulationPoints(int n, vector<vector<int>>& connections) {
    vector<vector<int>> graph(n);
    for (auto& connection : connections) {
        graph[connection[0] - 1].push_back(connection[1] - 1);
        graph[connection[1] - 1].push_back(connection[0] - 1);
    }

    vector<int> discoveryTime(n, -1);
    vector<int> low(n, -1);
    vector<bool> isArticulationPoint(n, false);
    vector<int> parent(n, -1);
    vector<int> time(1, 0);
    vector<int> result;

    function<void(int)> dfs = [&](int node) {
        discoveryTime[node] = low[node] = time[0]++;
        int children = 0;

        for (int neighbor : graph[node]) {
            if (discoveryTime[neighbor] == -1) {
                parent[neighbor] = node;
                children++;
                dfs(neighbor);

                low[node] = min(low[node], low[neighbor]);

                if (parent[node] == -1 && children > 1) {
                    isArticulationPoint[node] = true;
                } else if (parent[node] != -1 && low[neighbor] >= discoveryTime[node]) {
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

    for (int i = 0; i < n; i++) {
        if (isArticulationPoint[i]) {
            result.push_back(i + 1);
        }
    }

    return result;
}
```

## Test Cases
```
Input: n = 5, connections = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
Output: [1, 4]
```

## Key Takeaways
- Articulation points are nodes that, when removed, increase the number of connected components in the graph.
- The algorithm uses DFS to traverse the graph and identify articulation points.
- A node is an articulation point if it has at least two children and the low value of one of its children is greater than or equal to its discovery time.