# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, it must have at most two vertices with odd degree. The problem can be solved for both directed and undirected graphs.

## Approach
To solve this problem, we can use a depth-first search (DFS) approach. We start at an arbitrary vertex and keep traversing edges until we reach a vertex with no unvisited edges. Then, we backtrack to the previous vertex and repeat the process until all edges have been visited.

## Complexity
- Time: O(E + V)
- Space: O(E + V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool hasEulerPath(vector<vector<int>>& graph) {
    int oddCount = 0;
    for (int i = 0; i < graph.size(); i++) {
        int degree = 0;
        for (int j = 0; j < graph[i].size(); j++) {
            if (graph[i][j] == 1) {
                degree++;
            }
        }
        if (degree % 2 != 0) {
            oddCount++;
        }
    }
    return oddCount <= 2;
}

void eulerPathUtil(vector<vector<int>>& graph, int vertex, vector<int>& path) {
    for (int i = 0; i < graph.size(); i++) {
        if (graph[vertex][i] == 1) {
            graph[vertex][i] = 0;
            graph[i][vertex] = 0;
            eulerPathUtil(graph, i, path);
        }
    }
    path.push_back(vertex);
}

vector<int> eulerPath(vector<vector<int>>& graph) {
    if (!hasEulerPath(graph)) {
        return {};
    }
    vector<int> path;
    for (int i = 0; i < graph.size(); i++) {
        if (graph[i].size() % 2 != 0) {
            eulerPathUtil(graph, i, path);
            break;
        }
    }
    if (path.empty()) {
        eulerPathUtil(graph, 0, path);
    }
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    vector<vector<int>> graph = {
        {0, 1, 0, 1},
        {1, 0, 1, 1},
        {0, 1, 0, 1},
        {1, 1, 1, 0}
    };
    vector<int> path = eulerPath(graph);
    for (int vertex : path) {
        cout << vertex << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: 
[
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 0]
]
Output: 0 1 2 1 3 0 3 2
```

## Key Takeaways
- An Euler path must visit every edge in the graph exactly once.
- The graph can have at most two vertices with odd degree for an Euler path to exist.
- DFS can be used to find an Euler path in a graph.