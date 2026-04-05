# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a node that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of all articulation points in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points. It keeps track of the discovery time and low value of each node to determine if a node is an articulation point. A node is an articulation point if it is the root of the DFS tree and has at least two children, or if it is not the root and has a child that is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<int>& visited, vector<int>& ap, vector<int>& disc, vector<int>& low, int& time) {
    visited[node] = 1;
    disc[node] = low[node] = time++;
    int child = 0;
    for (int neighbor : graph[node]) {
        if (neighbor == parent) continue;
        if (visited[neighbor]) {
            low[node] = min(low[node], disc[neighbor]);
        } else {
            child++;
            dfs(neighbor, node, graph, visited, ap, disc, low, time);
            low[node] = min(low[node], low[neighbor]);
            if (low[neighbor] >= disc[node] && parent != -1) {
                ap[node] = 1;
            }
        }
    }
    if (parent == -1 && child > 1) {
        ap[node] = 1;
    }
}

vector<int> findArticulationPoints(int n, vector<vector<int>>& graph) {
    vector<int> visited(n, 0);
    vector<int> ap(n, 0);
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
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}};
    vector<int> ap = findArticulationPoints(n, graph);
    for (int node : ap) {
        cout << node << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, graph = [[1], [0, 2], [1, 3], [2, 4], [3]]
Output: [2, 3]
```

## Key Takeaways
- Use DFS to traverse the graph and identify articulation points.
- Keep track of the discovery time and low value of each node to determine if a node is an articulation point.
- A node is an articulation point if it is the root of the DFS tree and has at least two children, or if it is not the root and has a child that is a bridge.