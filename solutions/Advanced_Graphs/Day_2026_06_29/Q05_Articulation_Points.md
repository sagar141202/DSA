# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a node that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, and the nodes are numbered from 1 to n. The function should return a list of all articulation points in the graph.

## Approach
We will use a depth-first search (DFS) algorithm to find all articulation points in the graph. The algorithm works by maintaining a timer to keep track of the discovery time and low value of each node. If a node is an articulation point, it will have at least one child node that has a low value greater than or equal to its discovery time.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<bool>& visited, vector<int>& disc, vector<int>& low, vector<bool>& ap, int& time) {
    visited[node] = true;
    disc[node] = low[node] = time++;
    int child = 0;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            child++;
            dfs(neighbor, node, graph, visited, disc, low, ap, time);
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

vector<int> findArticulationPoints(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    vector<bool> visited(n, false);
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> ap(n, false);
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1, graph, visited, disc, low, ap, time);
        }
    }
    vector<int> articulationPoints;
    for (int i = 0; i < n; i++) {
        if (ap[i]) {
            articulationPoints.push_back(i);
        }
    }
    return articulationPoints;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {1, 4}};
    vector<int> articulationPoints = findArticulationPoints(n, edges);
    for (int point : articulationPoints) {
        cout << point << " ";
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
- The algorithm uses a depth-first search (DFS) to find all articulation points in the graph.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph.