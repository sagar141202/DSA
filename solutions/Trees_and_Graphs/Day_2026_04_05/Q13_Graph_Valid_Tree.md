# Graph Valid Tree

## Problem Statement
Given `n` nodes and a list of undirected edges, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of neighboring nodes. The number of nodes `n` will be in the range [1, 200], and the number of edges will be in the range [0, 200]. For example, given `n = 5` and `edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`, the output should be `true` because the graph is a valid tree.

## Approach
The approach to solve this problem is to use a depth-first search (DFS) algorithm to traverse the graph and check for connectivity and cycles. If the graph is connected and has no cycles, it is a valid tree. We can use a union-find algorithm as an alternative approach.

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
        for (auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        
        // Check for connectivity using DFS
        vector<bool> visited(n, false);
        if (!dfs(0, -1, adj, visited)) {
            return false;
        }
        
        // Check if all nodes are visited
        for (bool visit : visited) {
            if (!visit) {
                return false;
            }
        }
        
        return true;
    }
    
    bool dfs(int node, int parent, vector<vector<int>>& adj, vector<bool>& visited) {
        visited[node] = true;
        for (int neighbor : adj[node]) {
            if (neighbor == parent) {
                continue;
            }
            if (visited[neighbor]) {
                return false;  // Cycle detected
            }
            if (!dfs(neighbor, node, adj, visited)) {
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
- Use DFS to traverse the graph and check for connectivity and cycles.
- Create an adjacency list to represent the graph.
- Use a visited array to keep track of visited nodes during DFS.