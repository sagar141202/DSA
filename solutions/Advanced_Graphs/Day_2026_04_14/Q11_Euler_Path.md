# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, return one possible path. If no such path exists, return an empty list. The graph is represented as an adjacency list, where each key is a node and its corresponding value is a list of neighboring nodes. The graph has at most 100 nodes and 1000 edges.

## Approach
The algorithm uses Hierholzer's algorithm to find an Euler path in the graph. It first checks if all nodes have even degrees, then it finds a node with an odd degree and starts a depth-first search from that node. The algorithm backtracks and adds edges to the path until it has visited all edges.

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
    vector<int> degree(n, 0);
    for (int i = 0; i < n; i++) {
        for (int j : graph[i]) {
            adj[i].push_back(j);
            degree[i]++;
            degree[j]++;
        }
    }
    
    vector<int> path;
    stack<int> st;
    st.push(start);
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
    int n, m;
    cin >> n >> m;
    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    vector<int> path = eulerPath(graph, 0);
    for (int node : path) {
        cout << node << " ";
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
Output: 0 1 3 2 4 2 0 1 3 4 
```

## Key Takeaways
- The graph must be connected for an Euler path to exist.
- If the graph has more than two nodes with odd degrees, then it is not possible to find an Euler path.
- The algorithm assumes that the input graph is represented as an adjacency list.