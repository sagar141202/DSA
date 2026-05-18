# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points. An articulation point is a node in the graph that, when removed, increases the number of connected components in the graph. The graph can have up to 10^5 nodes and edges. The input is an adjacency list representation of the graph, and the output should be a list of all articulation points.

## Approach
We will use Depth-First Search (DFS) to traverse the graph and identify articulation points. The algorithm works by maintaining a timer for the discovery time and low value of each node, and checking for conditions that indicate an articulation point. We also keep track of the parent of each node to handle the case where the root node is an articulation point.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<bool>& visited, 
         vector<int>& disc, vector<int>& low, vector<bool>& ap, int& time) {
    visited[node] = true;
    disc[node] = low[node] = time++;
    int child = 0;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            child++;
            dfs(neighbor, node, graph, visited, disc, low, ap, time);
            low[node] = min(low[node], low[neighbor]);
            if (parent != -1 && low[neighbor] >= disc[node])
                ap[node] = true;
            if (parent == -1 && child > 1)
                ap[node] = true;
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
- Articulation points are critical nodes in the graph that, when removed, increase the number of connected components.
- DFS is used to traverse the graph and identify articulation points by maintaining discovery time and low values for each node.
- The algorithm checks for conditions such as the low value of a neighbor being greater than or equal to the discovery time of the current node to determine if a node is an articulation point.