# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of edges, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles. The input is an integer `n` representing the number of nodes, and an array `edges` of size `m` where `edges[i] = [u, v]` represents an edge between nodes `u` and `v`. The nodes are numbered from 0 to `n-1`. The graph is undirected.

## Approach
To solve this problem, we can use a union-find algorithm to check for connectivity and detect cycles. We iterate over the edges and union the nodes. If we encounter an edge where the two nodes are already in the same set, it means there's a cycle.

## Complexity
- Time: O(n + m * α(n))
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
        rank.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionSets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
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
        if (edges.size() != n - 1) {
            return false;
        }
        UnionFind uf(n);
        for (auto& edge : edges) {
            int x = edge[0];
            int y = edge[1];
            if (uf.find(x) == uf.find(y)) {
                return false;
            }
            uf.unionSets(x, y);
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
- A valid tree is a connected graph with no cycles.
- The union-find algorithm can be used to detect cycles and check for connectivity in a graph.
- The time complexity of the union-find algorithm is O(n + m * α(n)), where n is the number of nodes and m is the number of edges.