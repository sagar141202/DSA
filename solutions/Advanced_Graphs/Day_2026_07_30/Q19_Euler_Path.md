# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, return one possible path. If not, return an empty list. The graph is represented as an adjacency list where each key is a node and its corresponding value is a list of neighboring nodes. The input graph can have at most 100 nodes and 1000 edges.

## Approach
The algorithm to find an Euler path involves using Hierholzer's algorithm, which is based on Depth-First Search (DFS) and works by repeatedly finding and removing cycles from the graph until only one cycle remains, which is the Euler path. We also need to check if the graph is connected and if it has at most two nodes with odd degrees.

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>> graph, int start) {
    int V = graph.size();
    vector<int> degree(V, 0);
    vector<vector<int>> adj(V);
    for (int i = 0; i < V; i++) {
        for (int j : graph[i]) {
            adj[i].push_back(j);
            degree[i]++;
            degree[j]++;
        }
    }

    int odd = 0;
    for (int i = 0; i < V; i++) {
        if (degree[i] % 2 != 0) {
            odd++;
        }
    }

    if (odd > 2) {
        return {};
    }

    vector<int> path;
    stack<int> st;
    st.push(start);
    while (!st.empty()) {
        int u = st.top();
        if (!adj[u].empty()) {
            st.push(adj[u].back());
            adj[u].pop_back();
        } else {
            path.push_back(u);
            st.pop();
        }
    }

    reverse(path.begin(), path.end());
    return path;
}

int main() {
    // Example usage:
    vector<vector<int>> graph = {{1, 2}, {0, 2}, {0, 1}};
    vector<int> path = eulerPath(graph, 0);
    for (int node : path) {
        cout << node << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: graph = [[1, 2], [0, 2], [0, 1]], start = 0
Output: [0, 1, 2, 0]
```

## Key Takeaways
- To find an Euler path, we need to check if the graph is connected and if it has at most two nodes with odd degrees.
- Hierholzer's algorithm can be used to find an Euler path by repeatedly finding and removing cycles from the graph.
- The algorithm involves using DFS to traverse the graph and find the Euler path.