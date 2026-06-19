# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a vertex that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The input graph is connected and has n vertices.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points. It keeps track of the discovery time and low value for each vertex, and checks for conditions that indicate an articulation point. The DFS traversal is performed recursively, and the algorithm handles cases for root vertices and non-root vertices separately.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int u, int p, vector<vector<int>>& graph, vector<int>& disc, vector<int>& low, vector<bool>& ap, int& time) {
    disc[u] = low[u] = time++;
    int children = 0;
    for (int v : graph[u]) {
        if (disc[v] == -1) {
            children++;
            dfs(v, u, graph, disc, low, ap, time);
            low[u] = min(low[u], low[v]);
            if (p == -1 && children > 1) ap[u] = true;
            if (p != -1 && low[v] >= disc[u]) ap[u] = true;
        } else if (v != p) {
            low[u] = min(low[u], disc[v]);
        }
    }
}

vector<int> findArticulationPoints(int n, vector<vector<int>>& graph) {
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> ap(n, false);
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (disc[i] == -1) dfs(i, -1, graph, disc, low, ap, time);
    }
    vector<int> result;
    for (int i = 0; i < n; i++) {
        if (ap[i]) result.push_back(i);
    }
    return result;
}

int main() {
    int n = 5;
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}};
    vector<int> ap = findArticulationPoints(n, graph);
    for (int i : ap) cout << i << " ";
    return 0;
}
```

## Test Cases
```
Input: 
n = 5
graph = [[1], [0, 2], [1, 3], [2, 4], [3]]
Output: 2 3
```

## Key Takeaways
- An articulation point is a vertex that, when removed, increases the number of connected components in the graph.
- The algorithm uses DFS traversal to identify articulation points.
- The discovery time and low value are used to determine if a vertex is an articulation point.