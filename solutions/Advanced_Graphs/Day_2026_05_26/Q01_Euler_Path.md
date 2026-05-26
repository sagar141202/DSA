# Euler Path

## Problem Statement
An Euler path is a path in a graph that visits every edge exactly once. Given a connected graph with non-negative edge weights, find an Euler path if it exists. The graph can be represented as an adjacency list, and the function should return the path as a sequence of nodes. The graph is considered undirected, and the function should work for both directed and undirected graphs. For example, given a graph with nodes {1, 2, 3} and edges {(1, 2), (2, 3), (3, 1)}, the function should return a path such as [1, 2, 3, 1].

## Approach
The approach to solving this problem involves using Hierholzer's algorithm, which states that a graph has an Euler path if and only if at most two vertices have odd degrees. We will use a depth-first search (DFS) to traverse the graph and find the Euler path.

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> degree(n, 0);
    vector<vector<int>> adj(n);
    for (int i = 0; i < n; i++) {
        for (int j : graph[i]) {
            adj[i].push_back(j);
            degree[i]++;
            degree[j]++;
        }
    }
    int countOdd = 0;
    for (int i = 0; i < n; i++) {
        if (degree[i] % 2 != 0) {
            countOdd++;
        }
    }
    if (countOdd > 2) {
        return {};
    }
    vector<int> path;
    stack<int> st;
    st.push(0);
    while (!st.empty()) {
        int node = st.top();
        if (adj[node].empty()) {
            path.push_back(node);
            st.pop();
        } else {
            st.push(adj[node].back());
            adj[node].pop_back();
        }
    }
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    vector<vector<int>> graph = {{1}, {0, 2}, {1}};
    vector<int> path = eulerPath(graph);
    for (int node : path) {
        cout << node << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: {{1}, {0, 2}, {1}}
Output: 0 1 2 1 0
```

## Key Takeaways
- The graph must be connected to have an Euler path.
- At most two vertices can have odd degrees for an Euler path to exist.
- Hierholzer's algorithm can be used to find an Euler path in a graph.