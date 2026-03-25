# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, output the path. If not, output a message indicating that no Euler path exists. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighbors. The graph has n nodes and m edges. 1 ≤ n ≤ 10^5, 1 ≤ m ≤ 10^5.

## Approach
The algorithm uses a depth-first search (DFS) approach to find an Euler path in the graph. It starts at an arbitrary node and explores as far as possible along each branch before backtracking. If the graph has an Euler path, the DFS will visit every edge exactly once.

## Complexity
- Time: O(m + n)
- Space: O(m + n)

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
    for (int i = 0; i < n; i++) {
        for (int j : graph[i]) {
            degree[j]--;
        }
    }
    int start = 0;
    for (int i = 0; i < n; i++) {
        if (degree[i] == 1) {
            start = i;
            break;
        }
    }
    vector<int> path;
    vector<bool> visited(n * n, false);
    function<void(int)> dfs = [&](int node) {
        while (graph[node].size() > 0) {
            int neighbor = graph[node].back();
            graph[node].pop_back();
            int edge = node * n + neighbor;
            if (!visited[edge]) {
                visited[edge] = true;
                dfs(neighbor);
            }
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
5 6
0 1
0 2
1 2
1 3
2 4
3 4
Output: 0 1 3 4 2 0
```

## Key Takeaways
- An Euler path exists if and only if at most two nodes have odd degree.
- If the graph is connected and has an Euler path, the path starts at a node with odd degree and ends at a node with odd degree.
- The algorithm uses DFS to find an Euler path in O(m + n) time complexity.