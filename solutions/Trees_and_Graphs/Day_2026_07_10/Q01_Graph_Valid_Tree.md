# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges `edges` where `edges[i] = [ui, vi]`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles, and it has `n-1` edges. The nodes are numbered from 0 to `n-1`. The function should return `true` if the graph is a valid tree, and `false` otherwise. For example, given `n = 5` and `edges = [[0,1],[0,2],[0,3],[1,4]]`, the function should return `true`. However, given `n = 5` and `edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]`, the function should return `false` because the graph has a cycle.

## Approach
The approach to solve this problem is to use a Union-Find algorithm to check if the graph is connected and has no cycles. We will also check if the number of edges is `n-1`. If the graph passes all these checks, it is a valid tree.

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

bool isValidTree(int n, vector<vector<int>>& edges) {
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

    // Check if all nodes are connected
    int root = uf.find(0);
    for (int i = 1; i < n; i++) {
        if (uf.find(i) != root) {
            return false;
        }
    }

    return true;
}
```

## Test Cases
```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

## Key Takeaways
- The Union-Find algorithm is used to check if the graph is connected and has no cycles.
- The number of edges in a valid tree is always `n-1`.
- We need to check if all nodes are connected to ensure the graph is a valid tree.