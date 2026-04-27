# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges `edges` where `edges[i] = [u, v]` represents a bidirectional edge between nodes `u` and `v`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles. The graph is assumed to be undirected and the nodes are numbered from 0 to `n - 1`. The function should return `true` if the graph is a valid tree, otherwise `false`. For example, given `n = 5` and `edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`, the function should return `true` because the graph is a valid tree.

## Approach
To solve this problem, we can use a depth-first search (DFS) or union-find algorithm to check if the graph is connected and has no cycles. The graph is connected if all nodes can be visited from any node, and it has no cycles if no node is visited more than once during the traversal. 

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
        // Create an adjacency list to represent the graph
        vector<vector<int>> graph(n);
        for (const auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        // Use a visited array to keep track of visited nodes
        vector<bool> visited(n, false);
        
        // Perform DFS from node 0
        if (!dfs(graph, 0, -1, visited)) {
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
    
    // Helper function to perform DFS
    bool dfs(const vector<vector<int>>& graph, int node, int parent, vector<bool>& visited) {
        visited[node] = true;
        
        for (int neighbor : graph[node]) {
            if (neighbor == parent) {
                continue;
            }
            if (visited[neighbor]) {
                return false;  // Cycle detected
            }
            if (!dfs(graph, neighbor, node, visited)) {
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
- Use DFS or union-find to check if a graph is connected and has no cycles.
- Keep track of visited nodes to avoid revisiting them during the traversal.
- Check if all nodes are visited after the traversal to ensure the graph is connected.