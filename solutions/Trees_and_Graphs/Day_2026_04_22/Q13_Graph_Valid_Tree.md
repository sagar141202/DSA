# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges `edges` where `edges[i] = [u, v]` represents a connection between nodes `u` and `v`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles, and it has `n-1` edges. The nodes are numbered from 0 to `n-1`.

## Approach
To determine if a graph is a valid tree, we can use a depth-first search (DFS) or union-find algorithm to check for connectivity and cycles. If the graph is connected and has no cycles, and it has `n-1` edges, then it is a valid tree. We will use the union-find algorithm in this solution.

## Complexity
- Time: O(n + m)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;

    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionNodes(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (edges.size() != n - 1) return false;
        UnionFind uf(n);
        for (auto& edge : edges) {
            int x = edge[0];
            int y = edge[1];
            if (uf.find(x) == uf.find(y)) return false;
            uf.unionNodes(x, y);
        }
        // Check if all nodes are connected
        int root = uf.find(0);
        for (int i = 1; i < n; i++) {
            if (uf.find(i) != root) return false;
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
- A valid tree is a connected graph with no cycles and `n-1` edges.
- The union-find algorithm can be used to check for connectivity and cycles in a graph.
- Checking if all nodes are connected after union operations ensures the graph is a valid tree.