# Graph Valid Tree

## Problem Statement
Given `n` nodes labeled from `1` to `n`, and an array of undirected edges `edges` where `edges[i] = [u, v]` represents a bidirectional edge between node `u` and node `v`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles, and it has `n-1` edges. The function should return `true` if the graph is a valid tree, otherwise return `false`. The constraints are `1 <= n <= 10^5` and `0 <= edges.length <= 10^5`.

## Approach
The approach is to use a Union-Find algorithm to check for connectivity and cycles. We iterate over the edges and use the Union-Find algorithm to union the two nodes of each edge. If we find a cycle (i.e., the two nodes are already in the same set), we return `false`. After iterating over all edges, we check if all nodes are in the same set. If they are, and we have `n-1` edges, we return `true`, otherwise we return `false`.

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
    UnionFind(int n) {
        parent.resize(n);
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
            parent[rootX] = rootY;
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
            uf.unionNodes(x, y);
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
- A graph is a valid tree if it is connected and has no cycles.
- The Union-Find algorithm can be used to check for connectivity and cycles in a graph.
- The time complexity of the Union-Find algorithm is O(n + m * α(n)), where n is the number of nodes and m is the number of edges.