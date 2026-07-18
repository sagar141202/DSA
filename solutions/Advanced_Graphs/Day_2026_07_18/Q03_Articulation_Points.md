# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a node that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of all articulation points in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points. It keeps track of the discovery time and low value of each node to determine if it's an articulation point. If a node is a cut vertex, it will have at least one child that doesn't have a lower low value than its parent.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<bool>& visited, vector<bool>& ap, vector<int>& disc, vector<int>& low, int& time) {
    visited[node] = true;
    disc[node] = low[node] = time++;
    int children = 0;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            children++;
            dfs(neighbor, node, graph, visited, ap, disc, low, time);
            low[node] = min(low[node], low[neighbor]);
            if (parent == -1 && children > 1) {
                ap[node] = true;
            } else if (parent != -1 && low[neighbor] >= disc[node]) {
                ap[node] = true;
            }
        } else if (neighbor != parent) {
            low[node] = min(low[node], disc[neighbor]);
        }
    }
}

vector<int> findArticulationPoints(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    vector<bool> visited(n, false);
    vector<bool> ap(n, false);
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1, graph, visited, ap, disc, low, time);
        }
    }
    vector<int> result;
    for (int i = 0; i < n; i++) {
        if (ap[i]) {
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {1, 4}};
    vector<int> ap = findArticulationPoints(n, edges);
    for (int node : ap) {
        cout << node << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: [1]
```

## Key Takeaways
- Articulation points are nodes that, when removed, increase the number of connected components in the graph.
- DFS is used to traverse the graph and identify articulation points.
- The discovery time and low value of each node are used to determine if it's an articulation point.