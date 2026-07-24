# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a node that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of all articulation points in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points. It keeps track of the discovery time and low value for each node, and checks if the current node is an articulation point based on its low value and the low value of its neighbors.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<int>& visited, vector<int>& ap, vector<int>& disc, vector<int>& low, int& time, vector<vector<int>>& graph) {
    visited[node] = true;
    disc[node] = low[node] = time++;
    int child = 0;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            child++;
            dfs(neighbor, node, visited, ap, disc, low, time, graph);
            low[node] = min(low[node], low[neighbor]);
            if (parent == -1 && child > 1) {
                ap[node] = true;
            }
            if (parent != -1 && low[neighbor] >= disc[node]) {
                ap[node] = true;
            }
        } else if (neighbor != parent) {
            low[node] = min(low[node], disc[neighbor]);
        }
    }
}

vector<int> findArticulationPoints(int n, vector<vector<int>>& graph) {
    vector<int> visited(n, false);
    vector<int> ap(n, false);
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1, visited, ap, disc, low, time, graph);
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
Input: n = 5, graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}}
Output: 2 3
```

## Key Takeaways
- Articulation points are nodes that, when removed, increase the number of connected components in the graph.
- The algorithm uses DFS to identify articulation points by keeping track of the discovery time and low value for each node.
- A node is an articulation point if it is the root of the DFS tree and has at least two children, or if it is not the root and the low value of one of its neighbors is greater than or equal to its discovery time.