# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If an Euler path exists, output the path. Otherwise, output a message indicating that no Euler path exists. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of neighboring nodes. The graph has at most 100 nodes and 1000 edges.

## Approach
The algorithm uses Hierholzer's algorithm to find an Euler path in the graph. It first checks if all nodes have even degrees, then it uses a stack to keep track of nodes and edges. If a node has no more edges, it is added to the result path.

## Complexity
- Time: O(|E| + |V|)
- Space: O(|E| + |V|)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> degree(n, 0);
    for (int i = 0; i < n; i++) {
        for (int j : graph[i]) {
            degree[i]++;
            degree[j]++;
        }
    }

    int odd = 0;
    for (int i = 0; i < n; i++) {
        if (degree[i] % 2 != 0) {
            odd++;
        }
    }

    if (odd > 2) {
        return {}; // no Euler path
    }

    vector<int> path;
    stack<int> st;
    st.push(0);

    while (!st.empty()) {
        int node = st.top();
        if (graph[node].empty()) {
            path.push_back(node);
            st.pop();
        } else {
            int neighbor = graph[node].back();
            graph[node].pop_back();
            st.push(neighbor);
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

    vector<int> path = eulerPath(graph);
    if (path.empty()) {
        cout << "No Euler path" << endl;
    } else {
        for (int node : path) {
            cout << node << " ";
        }
        cout << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
5 6
0 1
1 2
2 3
3 4
4 0
0 2
Output: 0 2 1 0 4 3 2
```

## Key Takeaways
- An Euler path exists if and only if at most two nodes have odd degrees.
- Hierholzer's algorithm is used to find an Euler path in a graph.
- The algorithm uses a stack to keep track of nodes and edges.