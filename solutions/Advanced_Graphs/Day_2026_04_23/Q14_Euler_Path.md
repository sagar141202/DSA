# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, return one possible path. If the graph does not have an Euler path, return an empty list. The graph is represented as an adjacency list, where each key is a node and its corresponding value is a list of its neighboring nodes. The graph has at most 100 nodes and 1000 edges.

## Approach
To solve this problem, we use Hierholzer's algorithm, which is a method for finding an Euler path in a graph. The algorithm works by repeatedly finding a cycle in the graph and removing it until all edges have been visited. We start at an arbitrary node and explore as far as possible along each branch before backtracking.

## Complexity
- Time: O(E + V)
- Space: O(E + V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph, int start) {
    int n = graph.size();
    vector<vector<int>> adj(n);
    vector<int> inDegree(n, 0), outDegree(n, 0);
    for (int i = 0; i < n; i++) {
        for (int j : graph[i]) {
            adj[i].push_back(j);
            outDegree[i]++;
            inDegree[j]++;
        }
    }

    int oddIn = 0, oddOut = 0;
    for (int i = 0; i < n; i++) {
        if (inDegree[i] % 2 != outDegree[i] % 2) {
            if (inDegree[i] % 2 == 1) oddIn++;
            else oddOut++;
        }
    }

    if (oddIn > 1 || oddOut > 1) return {};

    vector<int> path;
    stack<int> st;
    st.push(start);

    while (!st.empty()) {
        int node = st.top();
        if (!adj[node].empty()) {
            st.push(adj[node].back());
            adj[node].pop_back();
        } else {
            path.push_back(node);
            st.pop();
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
    for (int node : path) cout << node << " ";
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
Output: 0 1 3 2 4
```

## Key Takeaways
- The graph must be connected to have an Euler path.
- If the graph has more than two nodes with odd degree, it does not have an Euler path.
- Hierholzer's algorithm is used to find an Euler path in a graph.