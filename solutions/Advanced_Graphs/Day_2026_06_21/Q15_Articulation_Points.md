# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a node in the graph that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, and the nodes are numbered from 1 to n. The input is a list of edges in the graph, where each edge is represented as a pair of nodes. The output should be a list of all articulation points in the graph. For example, in the graph with edges [(1, 2), (2, 3), (3, 4), (4, 1), (2, 5)], the articulation point is 2.

## Approach
The algorithm to find articulation points involves using Depth-First Search (DFS) to traverse the graph and keep track of the discovery time and low value of each node. The low value of a node is the smallest discovery time of any node that can be reached from the current node. If the low value of a node is greater than or equal to its discovery time, then the node is an articulation point.

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
        graph[edge[0] - 1].push_back(edge[1] - 1);
        graph[edge[1] - 1].push_back(edge[0] - 1);
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
    vector<int> result;
    for (int i = 0; i < n; i++) {
        if (ap[i]) {
            result.push_back(i + 1);
        }
    }
    return result;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{1, 2}, {2, 3}, {3, 4}, {4, 1}, {2, 5}};
    vector<int> result = findArticulationPoints(n, edges);
    for (int node : result) {
        cout << node << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, edges = [[1, 2], [2, 3], [3, 4], [4, 1], [2, 5]]
Output: [2]
```

## Key Takeaways
- Articulation points are nodes that, when removed, increase the number of connected components in the graph.
- The algorithm uses DFS to find articulation points by keeping track of the discovery time and low value of each node.
- A node is an articulation point if its low value is greater than or equal to its discovery time, or if it is the root node and has more than one child.