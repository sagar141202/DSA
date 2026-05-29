# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of `edges` where `edges[i] = [ui, vi]` represents a bidirectional edge between nodes `ui` and `vi`, determine if the graph is a valid tree. A valid tree is a graph that satisfies the following conditions: (1) the graph is connected, and (2) the graph has no cycles. The graph is undirected, and the nodes are numbered from 0 to `n - 1`.

## Approach
We can solve this problem by checking if the graph is connected and has no cycles using a depth-first search (DFS) or union-find algorithm. The key idea is to count the number of edges and nodes, and if the number of edges is one less than the number of nodes, it could be a tree.

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
        // Check if the number of edges is one less than the number of nodes
        if (edges.size() != n - 1) return false;
        
        // Create an adjacency list representation of the graph
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        // Perform DFS to check if the graph is connected and has no cycles
        vector<bool> visited(n, false);
        if (!dfs(graph, 0, -1, visited)) return false;
        
        // Check if all nodes are visited
        for (bool visit : visited) {
            if (!visit) return false;
        }
        
        return true;
    }
    
    bool dfs(vector<vector<int>>& graph, int node, int parent, vector<bool>& visited) {
        visited[node] = true;
        for (int neighbor : graph[node]) {
            if (neighbor == parent) continue;
            if (visited[neighbor]) return false;
            if (!dfs(graph, neighbor, node, visited)) return false;
        }
        return true;
    }
};
```

## Test Cases
```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

## Key Takeaways
- To determine if a graph is a valid tree, we need to check if it is connected and has no cycles.
- We can use DFS or union-find algorithm to solve this problem.
- The number of edges in a valid tree is one less than the number of nodes.