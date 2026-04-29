# Articulation Points

## Problem Statement
Given an undirected graph, find all articulation points in the graph. An articulation point is a node that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of neighboring nodes. The graph may contain self-loops and multiple edges between nodes.

## Approach
The approach to finding articulation points involves using Depth-First Search (DFS) to traverse the graph and identify nodes that meet the articulation point criteria. We use a recursive DFS function to calculate the lowest reachable ancestor for each node. A node is an articulation point if it has at least two children or if it is the root node and has at least one child.

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
        graph[connection[0]].push_back(connection[1]);
        graph[connection[1]].push_back(connection[0]);
    }

    vector<int> discoveryTime(n, -1);
    vector<int> low(n, -1);
    vector<bool> isArticulationPoint(n, false);
    vector<int> parent(n, -1);
    int time = 0;

    function<void(int)> dfs = [&](int node) {
        discoveryTime[node] = time;
        low[node] = time;
        time++;
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

int main() {
    int n = 5;
    vector<vector<int>> connections = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {1, 4}};
    vector<int> articulationPoints = articulationPoints(n, connections);

    for (int point : articulationPoints) {
        cout << point << " ";
    }

    return 0;
}
```

## Test Cases
```
Input: n = 5, connections = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: [1]
```

## Key Takeaways
- Articulation points are nodes that increase the number of connected components when removed.
- The algorithm uses DFS to find articulation points by calculating the lowest reachable ancestor for each node.
- A node is an articulation point if it has at least two children or if it is the root node and has at least one child.