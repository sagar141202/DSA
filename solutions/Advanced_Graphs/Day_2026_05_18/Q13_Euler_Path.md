# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path if it exists. An Euler path is a path that visits every edge in the graph exactly once. The graph can have multiple connected components, but an Euler path must visit all edges in the graph. If the graph has more than two vertices with odd degree (in the case of undirected graphs) or more than one vertex with odd in-degree and one vertex with odd out-degree (in the case of directed graphs), then an Euler path does not exist.

## Approach
The algorithm to find an Euler path involves using a depth-first search (DFS) to traverse the graph and visit all edges. We start at an arbitrary vertex and explore as far as possible along each branch before backtracking. The key intuition is to ensure that we visit all edges in the graph exactly once.

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph, int start) {
    int n = graph.size();
    vector<vector<int>> adj(n);
    for (int i = 0; i < n; i++) {
        for (int j : graph[i]) {
            adj[i].push_back(j);
            adj[j].push_back(i); // for undirected graph
        }
    }

    vector<int> path;
    stack<int> st;
    st.push(start);

    while (!st.empty()) {
        int v = st.top();
        if (!adj[v].empty()) {
            st.push(adj[v].back());
            adj[v].pop_back();
        } else {
            path.push_back(v);
            st.pop();
        }
    }

    reverse(path.begin(), path.end());
    return path;
}

int main() {
    int n = 5;
    vector<vector<int>> graph(n);
    // initialize graph
    graph[0].push_back(1);
    graph[1].push_back(2);
    graph[2].push_back(0);
    graph[2].push_back(3);
    graph[3].push_back(4);

    vector<int> path = eulerPath(graph, 0);
    for (int v : path) {
        cout << v << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: 
Graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (2, 3), (3, 4)}
Output: 0 1 2 0 2 3 4
```

## Key Takeaways
- An Euler path visits every edge in the graph exactly once.
- If the graph has more than two vertices with odd degree (in the case of undirected graphs) or more than one vertex with odd in-degree and one vertex with odd out-degree (in the case of directed graphs), then an Euler path does not exist.
- The algorithm uses a depth-first search (DFS) to traverse the graph and visit all edges.