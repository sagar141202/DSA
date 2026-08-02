# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, return one possible path. If the graph does not have an Euler path, return an empty list. The graph is represented as an adjacency list. The function should take as input a graph and return a list of edges representing the Euler path.

## Approach
The algorithm uses Hierholzer's algorithm to find an Euler path in the graph. It starts by finding a vertex with an odd degree, then traverses the graph using a stack to keep track of the current path. If a vertex has no more edges to traverse, it backtracks to the previous vertex.

## Complexity
- Time: O(E + V)
- Space: O(E + V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to find an Euler path in a graph
vector<pair<int, int>> eulerPath(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> degree(n, 0);
    for (int i = 0; i < n; i++) {
        for (int j : graph[i]) {
            degree[i]++;
            degree[j]++;
        }
    }

    int start = -1;
    for (int i = 0; i < n; i++) {
        if (degree[i] % 2 == 1) {
            if (start == -1) {
                start = i;
            } else {
                return {}; // graph does not have an Euler path
            }
        }
    }

    if (start == -1) {
        start = 0; // graph has an Euler circuit
    }

    vector<pair<int, int>> result;
    stack<int> s;
    s.push(start);

    while (!s.empty()) {
        int u = s.top();
        if (!graph[u].empty()) {
            int v = graph[u].back();
            graph[u].pop_back();
            graph[v].erase(remove(graph[v].begin(), graph[v].end(), u), graph[v].end());
            s.push(v);
        } else {
            result.push_back({s.top(), u});
            s.pop();
        }
    }

    reverse(result.begin(), result.end());
    return result;
}

// Example usage:
int main() {
    vector<vector<int>> graph = {{1}, {0, 2}, {1}};
    vector<pair<int, int>> path = eulerPath(graph);
    for (auto& edge : path) {
        cout << "(" << edge.first << ", " << edge.second << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: graph = [[1], [0, 2], [1]]
Output: [(0, 1), (1, 2), (2, 1)]
Input: graph = [[1, 2], [0, 2], [0, 1]]
Output: [(0, 1), (1, 2), (2, 0)]
```

## Key Takeaways
- The graph must be connected to have an Euler path.
- If the graph has more than two vertices with odd degree, it does not have an Euler path.
- Hierholzer's algorithm can be used to find an Euler path in a graph.