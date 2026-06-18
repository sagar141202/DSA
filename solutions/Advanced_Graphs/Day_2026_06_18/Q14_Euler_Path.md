# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has more than two vertices with odd degree (for undirected graphs) or more than one vertex with odd in-degree and more than one vertex with odd out-degree (for directed graphs), then it is not possible to find an Euler path. The goal is to determine whether an Euler path exists and, if so, construct it.

## Approach
The approach involves checking if the graph has an Euler path by verifying the degree constraints, and then using Hierholzer's algorithm to construct the path. The algorithm works by repeatedly finding a cycle in the graph and removing it until no more cycles can be found.

## Complexity
- Time: O(E + V)
- Space: O(E + V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph, int start) {
    int V = graph.size();
    vector<int> degree(V, 0);
    for (int i = 0; i < V; i++) {
        for (int j : graph[i]) {
            degree[i]++;
        }
    }

    int oddCount = 0;
    for (int i = 0; i < V; i++) {
        if (degree[i] % 2 != 0) {
            oddCount++;
        }
    }

    if (oddCount > 2) {
        return {}; // No Euler path exists
    }

    stack<int> st;
    st.push(start);
    vector<int> path;

    while (!st.empty()) {
        int u = st.top();
        if (!graph[u].empty()) {
            int v = graph[u].back();
            graph[u].pop_back();
            st.push(v);
        } else {
            path.push_back(u);
            st.pop();
        }
    }

    reverse(path.begin(), path.end());
    return path;
}

int main() {
    int V = 5;
    vector<vector<int>> graph(V);
    graph[0].push_back(1);
    graph[0].push_back(2);
    graph[1].push_back(0);
    graph[1].push_back(3);
    graph[2].push_back(0);
    graph[2].push_back(4);
    graph[3].push_back(1);
    graph[4].push_back(2);

    vector<int> path = eulerPath(graph, 0);
    for (int i : path) {
        cout << i << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: 
Graph:
0 -> 1, 2
1 -> 0, 3
2 -> 0, 4
3 -> 1
4 -> 2

Output: 
0 1 3 1 0 2 4 2 0
```

## Key Takeaways
- An Euler path in a graph visits every edge exactly once.
- A graph has an Euler path if and only if at most two vertices have odd degree (for undirected graphs) or at most one vertex has odd in-degree and at most one vertex has odd out-degree (for directed graphs).
- Hierholzer's algorithm is used to construct the Euler path in a graph.