# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of edges, determine if the given graph is a valid tree. A valid tree is a graph that is connected and has no cycles. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of neighboring nodes. The function should return `true` if the graph is a valid tree and `false` otherwise. The constraints are: `1 <= n <= 10^5` and `0 <= edges.length <= n - 1`.

## Approach
To solve this problem, we can use a depth-first search (DFS) algorithm to traverse the graph and check for cycles. If we encounter a node that has already been visited and it's not the parent of the current node, then the graph has a cycle. We also need to check if all nodes are connected.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        // Create an adjacency list
        vector<vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        // Check if the graph is connected
        vector<bool> visited(n, false);
        if (!dfs(0, -1, adj, visited)) return false;

        // Check if all nodes are visited
        for (bool visit : visited) {
            if (!visit) return false;
        }

        return true;
    }

    bool dfs(int node, int parent, vector<vector<int>>& adj, vector<bool>& visited) {
        visited[node] = true;
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                if (!dfs(neighbor, node, adj, visited)) return false;
            } else if (neighbor != parent) {
                return false;
            }
        }
        return true;
    }
};
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true

Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false
```

## Key Takeaways
- A graph is a valid tree if it is connected and has no cycles.
- We can use DFS to traverse the graph and check for cycles.
- Checking if all nodes are visited ensures the graph is connected.