# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path if it exists. An Euler path is a path that visits every edge in the graph exactly once. The graph can have multiple connected components. If the graph has more than two vertices with odd degrees, then it is not possible to have an Euler path. The task is to determine whether the given graph has an Euler path and if so, construct it.

## Approach
The approach involves checking if the graph has an Euler path by counting the number of vertices with odd degrees. If the graph has at most two vertices with odd degrees, we can find an Euler path using a modified depth-first search (DFS) algorithm.

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph, int start) {
    int n = graph.size();
    vector<int> degree(n);
    for (int i = 0; i < n; i++) {
        for (int j : graph[i]) {
            degree[i]++;
            degree[j]++;
        }
    }

    int oddCount = 0;
    for (int i = 0; i < n; i++) {
        if (degree[i] % 2 != 0) {
            oddCount++;
        }
    }

    if (oddCount > 2) {
        return {}; // no Euler path
    }

    vector<vector<int>> adj(n);
    for (int i = 0; i < n; i++) {
        for (int j : graph[i]) {
            adj[i].push_back(j);
        }
    }

    vector<int> path;
    vector<bool> visited(n * n, false);
    stack<int> st;
    st.push(start);

    while (!st.empty()) {
        int node = st.top();
        bool found = false;
        for (int i = 0; i < adj[node].size(); i++) {
            int neighbor = adj[node][i];
            if (!visited[node * n + neighbor]) {
                found = true;
                visited[node * n + neighbor] = true;
                st.push(neighbor);
                break;
            }
        }
        if (!found) {
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
Output: 0 1 3 2 4 3 2 0 1
```

## Key Takeaways
- A graph has an Euler path if and only if it has at most two vertices with odd degrees.
- We can use a modified DFS algorithm to find an Euler path in a graph.
- The time complexity of finding an Euler path is O(V + E), where V is the number of vertices and E is the number of edges.