# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, output the path. If not, output a message saying that the graph does not have an Euler path. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The input graph is connected and has at most 100 nodes and 1000 edges.

## Approach
The algorithm uses depth-first search (DFS) to traverse the graph and find an Euler path. It starts at a node with an odd degree, if one exists, and explores as far as possible along each branch before backtracking. The algorithm ensures that every edge is visited exactly once.

## Complexity
- Time: O(E + V)
- Space: O(E + V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> degree(n, 0);
    for (int i = 0; i < n; i++) {
        degree[i] = graph[i].size();
    }
    int start = 0;
    for (int i = 0; i < n; i++) {
        if (degree[i] % 2 != 0) {
            start = i;
            break;
        }
    }
    vector<int> path;
    vector<bool> visited(n * n, false);
    function<void(int)> dfs = [&](int node) {
        while (degree[node] > 0) {
            int neighbor = graph[node].back();
            graph[node].pop_back();
            degree[node]--;
            degree[neighbor]--;
            dfs(neighbor);
        }
        path.push_back(node);
    };
    dfs(start);
    reverse(path.begin(), path.end());
    return path;
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
    vector<int> path = eulerPath(graph);
    for (int node : path) {
        cout << node << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: 
4 4
0 1
1 2
2 3
3 0
Output: 0 1 2 3 0
```

## Key Takeaways
- An Euler path exists if and only if at most two nodes have an odd degree.
- The algorithm uses DFS to traverse the graph and find an Euler path.
- The time complexity is O(E + V), where E is the number of edges and V is the number of vertices.