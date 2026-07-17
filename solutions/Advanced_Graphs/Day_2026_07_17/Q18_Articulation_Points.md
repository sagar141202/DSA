# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points. An articulation point is a node in the graph that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The graph has 'n' nodes and 'm' edges.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points. It maintains a timer to keep track of the discovery time and low value of each node. A node is an articulation point if it has at least two children and the low value of one of its children is greater than or equal to its discovery time.

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
        if (visited[neighbor] == 0) {
            child++;
            dfs(neighbor, node, graph, visited, ap, disc, low, time);
            low[node] = min(low[node], low[neighbor]);
            if (parent != -1 && low[neighbor] >= disc[node]) ap[node] = 1;
        } else {
            low[node] = min(low[node], disc[neighbor]);
        }
    }
    if (parent == -1 && child > 1) ap[node] = 1;
}

void findArticulationPoints(int n, vector<vector<int>>& graph) {
    vector<int> visited(n, 0);
    vector<int> ap(n, 0);
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (visited[i] == 0) dfs(i, -1, graph, visited, ap, disc, low, time);
    }
    for (int i = 0; i < n; i++) {
        if (ap[i] == 1) cout << i << " ";
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    findArticulationPoints(n, graph);
    return 0;
}
```

## Test Cases
```
Input: 
5 5
0 1
1 2
2 0
1 3
1 4
Output: 1
```

## Key Takeaways
- Articulation points are critical nodes in a graph that, when removed, increase the number of connected components.
- The algorithm uses DFS to identify articulation points by maintaining a timer and low value for each node.
- A node is an articulation point if it has at least two children and the low value of one of its children is greater than or equal to its discovery time.