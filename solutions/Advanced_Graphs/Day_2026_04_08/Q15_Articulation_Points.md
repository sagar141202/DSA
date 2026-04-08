# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a vertex that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list and has n vertices and m edges. The vertices are numbered from 1 to n. The input is a list of edges, where each edge is a pair of vertices.

## Approach
The algorithm uses depth-first search (DFS) to find articulation points. It maintains a timer to keep track of the order in which vertices are visited. A vertex is an articulation point if it is the root of the DFS tree and has at least two children, or if it is not the root and has a child that is not reachable from any of its other children.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int u, int p, vector<vector<int>>& graph, vector<bool>& visited, vector<bool>& ap, vector<int>& disc, vector<int>& low, int& time) {
    visited[u] = true;
    disc[u] = low[u] = time++;
    int child = 0;
    for (int v : graph[u]) {
        if (!visited[v]) {
            child++;
            dfs(v, u, graph, visited, ap, disc, low, time);
            low[u] = min(low[u], low[v]);
            if (p == -1 && child > 1) {
                ap[u] = true;
            }
            if (p != -1 && low[v] >= disc[u]) {
                ap[u] = true;
            }
        } else if (v != p) {
            low[u] = min(low[u], disc[v]);
        }
    }
}

void findArticulationPoints(vector<vector<int>>& graph, int n) {
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
    for (int i = 0; i < n; i++) {
        if (ap[i]) {
            cout << i + 1 << " ";
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    findArticulationPoints(graph, n);
    return 0;
}
```

## Test Cases
```
Input: 
5 5
1 2
2 3
3 4
4 5
5 2
Output: 2 5
```

## Key Takeaways
- Articulation points are critical vertices in a graph that, when removed, increase the number of connected components.
- DFS is used to find articulation points by maintaining a timer and checking for certain conditions.
- The algorithm has a time complexity of O(V + E) and a space complexity of O(V), where V is the number of vertices and E is the number of edges.