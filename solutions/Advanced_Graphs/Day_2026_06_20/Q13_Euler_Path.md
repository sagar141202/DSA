# Euler Path

## Problem Statement
Given a connected graph, find an Euler path if it exists. An Euler path is a path that visits every edge in the graph exactly once. The graph can be directed or undirected, and it may contain self-loops and multiple edges between vertices. The input graph is represented as an adjacency list, where each index represents a vertex and the corresponding value is a list of its neighboring vertices. The graph has n vertices and m edges.

## Approach
To find an Euler path, we can use Hierholzer's algorithm, which states that a graph has an Euler path if and only if at most two vertices have odd degrees. We start at a vertex with an odd degree, if any, and keep traversing edges until we reach a vertex with no more untraversed edges.

## Complexity
- Time: O(m + n)
- Space: O(m + n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> degrees(n);
    for (int i = 0; i < n; i++) {
        degrees[i] = graph[i].size();
    }
    int oddCount = 0;
    int start = -1;
    for (int i = 0; i < n; i++) {
        if (degrees[i] % 2 != 0) {
            oddCount++;
            start = i;
        }
    }
    if (oddCount > 2) {
        return {}; // no Euler path
    }
    vector<int> path;
    vector<vector<int>> edges = graph;
    function<void(int)> dfs = [&](int vertex) {
        while (!edges[vertex].empty()) {
            int neighbor = edges[vertex].back();
            edges[vertex].pop_back();
            dfs(neighbor);
        }
        path.push_back(vertex);
    };
    if (start == -1) {
        start = 0;
    }
    dfs(start);
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    // example usage
    vector<vector<int>> graph = {{1, 2}, {0, 2}, {0, 1, 3}, {2}};
    vector<int> path = eulerPath(graph);
    for (int vertex : path) {
        cout << vertex << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: graph = [[1, 2], [0, 2], [0, 1, 3], [2]]
Output: [0, 1, 2, 3, 2, 0]
```

## Key Takeaways
- Hierholzer's algorithm can be used to find an Euler path in a graph.
- The graph must be connected and have at most two vertices with odd degrees.
- The algorithm starts at a vertex with an odd degree and traverses edges until it reaches a vertex with no more untraversed edges.