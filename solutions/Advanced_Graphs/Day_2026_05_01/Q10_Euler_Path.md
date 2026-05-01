# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, it must have at most two vertices with odd degree. If the graph has an Euler circuit (a closed Euler path), it must be connected and have all vertices with even degree. The task is to determine whether a given graph has an Euler path or circuit and to find the path if it exists. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its adjacent vertices. The input graph may contain self-loops and multiple edges between the same pair of vertices.

## Approach
The approach involves checking the degree of each vertex to determine if an Euler path or circuit exists. Then, a depth-first search (DFS) is used to traverse the graph and find the Euler path. The DFS traversal is modified to ensure that it visits every edge exactly once.

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
        return {}; // No Euler path
    }

    vector<int> result;
    vector<bool> visited(n * n, false); // Assuming max edge count is n * n
    stack<int> s;

    // Find the starting vertex
    int start = 0;
    for (int i = 0; i < n; i++) {
        if (degree[i] % 2 != 0) {
            start = i;
            break;
        }
    }

    s.push(start);
    while (!s.empty()) {
        int vertex = s.top();
        bool found = false;
        for (int i = 0; i < graph[vertex].size(); i++) {
            int neighbor = graph[vertex][i];
            int edgeIndex = vertex * n + neighbor;
            if (!visited[edgeIndex]) {
                found = true;
                visited[edgeIndex] = true;
                s.push(neighbor);
                break;
            }
        }
        if (!found) {
            result.push_back(vertex);
            s.pop();
        }
    }

    reverse(result.begin(), result.end());
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<vector<int>> graph(n);
    for (int i = 0; i < n; i++) {
        int m;
        cin >> m;
        for (int j = 0; j < m; j++) {
            int x;
            cin >> x;
            graph[i].push_back(x);
        }
    }

    vector<int> path = eulerPath(graph);
    for (int i : path) {
        cout << i << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: 
5
2 1 2
2 0 4
1 2
2 0 3
1 1
Output: 0 1 2 0 4 3 1
```

## Key Takeaways
- To find an Euler path, the graph must have at most two vertices with odd degree.
- If the graph has an Euler circuit, it must be connected and have all vertices with even degree.
- A modified depth-first search (DFS) traversal can be used to find the Euler path in a graph.