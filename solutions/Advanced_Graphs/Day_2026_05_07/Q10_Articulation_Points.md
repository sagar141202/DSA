# Articulation Points

## Problem Statement
Given a graph, find all the articulation points in it. An articulation point is a node in the graph that, when removed, increases the number of connected components in the graph. The graph can be represented as an adjacency list, and the nodes are numbered from 1 to n. The function should return a list of all articulation points in the graph.

## Approach
We will use a Depth-First Search (DFS) approach to find the articulation points. The idea is to keep track of the discovery time and low value of each node during the DFS traversal. If the low value of a node is greater than or equal to its discovery time, and it is not the root node, then it is an articulation point.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void articulationPoints(vector<vector<int>>& graph, int node, vector<bool>& visited, vector<int>& disc, vector<int>& low, vector<bool>& ap, int& time, int parent) {
    visited[node] = true;
    disc[node] = low[node] = ++time;
    int child = 0;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            child++;
            articulationPoints(graph, neighbor, visited, disc, low, ap, time, node);
            low[node] = min(low[node], low[neighbor]);
            if (parent == -1 && child > 1) {
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
    vector<int> disc(n, 0);
    vector<int> low(n, 0);
    vector<bool> ap(n, false);
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            articulationPoints(graph, i, visited, disc, low, ap, time, -1);
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
    vector<int> result = findArticulationPoints(n, edges);
    for (int node : result) {
        cout << node << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: 1
```

## Key Takeaways
- Articulation points are nodes that, when removed, increase the number of connected components in the graph.
- We use DFS to find the articulation points by keeping track of the discovery time and low value of each node.
- A node is an articulation point if its low value is greater than or equal to its discovery time, and it is not the root node.