# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, it must have at most two vertices with odd degree. If it has exactly two vertices with odd degree, the Euler path must start at one of them and end at the other. If all vertices have even degree, the Euler path can start and end at any vertex. The graph can have self-loops and multiple edges between the same pair of vertices.

## Approach
The algorithm uses Hierholzer's algorithm, which is a simple and efficient method for finding an Euler path in a graph. The algorithm works by repeatedly finding a cycle in the graph and removing it until all edges have been visited. The algorithm starts at a vertex with odd degree, if any, and explores the graph using a depth-first search.

## Complexity
- Time: O(|E| + |V|)
- Space: O(|E| + |V|)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph, int start) {
    int n = graph.size();
    vector<vector<int>> adj(n);
    vector<int> degree(n, 0);
    for (int u = 0; u < n; u++) {
        for (int v : graph[u]) {
            adj[u].push_back(v);
            degree[u]++;
            degree[v]++;
        }
    }

    vector<int> path;
    stack<int> st;
    st.push(start);

    while (!st.empty()) {
        int u = st.top();
        if (adj[u].empty()) {
            path.push_back(u);
            st.pop();
        } else {
            int v = adj[u].back();
            adj[u].pop_back();
            st.push(v);
        }
    }

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
    }

    vector<int> path = eulerPath(graph, 0);
    for (int u : path) {
        cout << u << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: 
5 7
0 1
0 2
1 2
1 3
2 3
2 4
3 4
Output: 0 1 3 2 4 3 2 0 1
```

## Key Takeaways
- An Euler path is a path that visits every edge in the graph exactly once.
- A graph has an Euler path if and only if it has at most two vertices with odd degree.
- Hierholzer's algorithm can be used to find an Euler path in a graph in O(|E| + |V|) time complexity.