# Euler Path

## Problem Statement
Given an undirected graph, find an Euler path if it exists. An Euler path is a path that visits every edge in the graph exactly once. The graph can have multiple connected components, but an Euler path must visit all edges in a single connected component. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of nodes representing the Euler path.

## Approach
The algorithm uses Hierholzer's algorithm to find the Euler path. It first checks if all nodes have even degrees, then it finds a node with an odd degree and starts a depth-first search from that node. If no such node exists, it starts the search from any node.

## Complexity
- Time: O(E + V)
- Space: O(E + V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> degrees(n, 0);
    for (int i = 0; i < n; i++) {
        degrees[i] = graph[i].size();
    }
    int oddCount = 0;
    int startNode = 0;
    for (int i = 0; i < n; i++) {
        if (degrees[i] % 2 != 0) {
            oddCount++;
            startNode = i;
        }
    }
    if (oddCount > 2) {
        return {}; // no Euler path
    }
    vector<int> path;
    stack<int> stack;
    stack.push(startNode);
    while (!stack.empty()) {
        int node = stack.top();
        if (!graph[node].empty()) {
            int neighbor = graph[node].back();
            graph[node].pop_back();
            stack.push(neighbor);
        } else {
            path.push_back(node);
            stack.pop();
        }
    }
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    vector<vector<int>> graph = {{1}, {0, 2}, {1}};
    vector<int> path = eulerPath(graph);
    for (int node : path) {
        cout << node << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [[1], [0, 2], [1]]
Output: [0, 1, 2]
Input: [[1, 2], [0, 2], [0, 1]]
Output: [0, 1, 2, 0]
```

## Key Takeaways
- An Euler path exists if and only if at most two nodes have odd degrees.
- Hierholzer's algorithm can be used to find an Euler path in a graph.
- The algorithm starts a depth-first search from a node with an odd degree, if such a node exists.