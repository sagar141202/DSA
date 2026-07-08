# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a node that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of all articulation points in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points by checking if the removal of a node increases the number of connected components. It utilizes the concept of low values and discovery times to determine articulation points.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<int>& visited, vector<int>& ap, vector<int>& disc, vector<int>& low, int& time) {
    visited[node] = true;
    disc[node] = low[node] = time++;
    int child = 0;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            child++;
            dfs(neighbor, node, graph, visited, ap, disc, low, time);
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

vector<int> articulationPoints(int n, vector<vector<int>>& connections) {
    vector<vector<int>> graph(n);
    for (auto& connection : connections) {
        graph[connection[0]].push_back(connection[1]);
        graph[connection[1]].push_back(connection[0]);
    }
    vector<int> visited(n, false);
    vector<int> ap(n, false);
    vector<int> disc(n, INT_MAX);
    vector<int> low(n, INT_MAX);
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
    vector<vector<int>> connections = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {1, 4}};
    vector<int> ap = articulationPoints(n, connections);
    for (int point : ap) {
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
- Articulation points are nodes that, when removed, increase the number of connected components in the graph.
- The algorithm uses DFS to traverse the graph and identify articulation points by checking if the removal of a node increases the number of connected components.
- The concept of low values and discovery times is used to determine articulation points.