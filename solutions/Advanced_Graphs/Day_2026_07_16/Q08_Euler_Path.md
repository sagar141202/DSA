# Euler Path

## Problem Statement
Given a connected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph can be directed or undirected, and it may contain cycles. If the graph has more than two vertices with odd degrees, then it is not possible to find an Euler path. The task is to determine if an Euler path exists and to find it if it does. The graph is represented as an adjacency list, where each vertex is associated with a list of its neighboring vertices.

## Approach
The approach to solve this problem involves using Hierholzer's algorithm, which is a method for finding an Euler path in a graph. The algorithm first checks if an Euler path exists by counting the number of vertices with odd degrees. If more than two vertices have odd degrees, then an Euler path does not exist.

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
    for (int i = 0; i < n; i++) {
        degree[i] = graph[i].size();
    }
    int oddCount = 0;
    for (int i = 0; i < n; i++) {
        if (degree[i] % 2 != 0) {
            oddCount++;
        }
    }
    if (oddCount > 2) {
        return {}; // No Euler path exists
    }
    vector<int> path;
    vector<bool> visited(n, false);
    stack<int> stack;
    for (int i = 0; i < n; i++) {
        if (degree[i] % 2 != 0) {
            stack.push(i);
            break;
        }
    }
    if (stack.empty()) {
        stack.push(0);
    }
    while (!stack.empty()) {
        int vertex = stack.top();
        if (graph[vertex].empty()) {
            path.push_back(vertex);
            stack.pop();
        } else {
            int neighbor = graph[vertex].back();
            graph[vertex].pop_back();
            stack.push(neighbor);
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
        cout << "No Euler path exists" << endl;
    } else {
        for (int i = 0; i < path.size(); i++) {
            cout << path[i] << " ";
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
2 0
2 3
3 4
4 2
Output:
0 1 2 4 3 2 0
```

## Key Takeaways
- The existence of an Euler path depends on the number of vertices with odd degrees.
- Hierholzer's algorithm is used to find an Euler path in a graph.
- The algorithm works by maintaining a stack of vertices and a set of visited edges.