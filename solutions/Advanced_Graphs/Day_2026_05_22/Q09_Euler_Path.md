# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, it must have at most two vertices with odd degree (in the case of an undirected graph) or at most two vertices with odd out-degree or odd in-degree (in the case of a directed graph). The task is to find an Euler path in the given graph, if one exists.

## Approach
The algorithm to find an Euler path involves using a depth-first search (DFS) to traverse the graph and find a path that visits every edge exactly once. We start the DFS from a vertex with an odd degree (if any). If the graph has more than two vertices with odd degree, we cannot find an Euler path.

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph, int start) {
    int n = graph.size();
    vector<int> path;
    stack<int> st;
    st.push(start);
    
    while (!st.empty()) {
        int u = st.top();
        if (graph[u].empty()) {
            path.push_back(u);
            st.pop();
        } else {
            int v = graph[u].back();
            graph[u].pop_back();
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
        graph[v].push_back(u); // for undirected graph
    }
    
    vector<int> path = eulerPath(graph, 0);
    for (int u : path) {
        cout << u << " ";
    }
    cout << endl;
    
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
2 4
3 4
4 0
Output: 
0 1 3 4 2 0
```

## Key Takeaways
- To find an Euler path, we need to start the DFS from a vertex with an odd degree (if any).
- If the graph has more than two vertices with odd degree, we cannot find an Euler path.
- The algorithm involves using a DFS to traverse the graph and find a path that visits every edge exactly once.