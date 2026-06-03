# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges `edges` where `edges[i] = [u, v]` represents a connection between nodes `u` and `v`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles, and it should have `n-1` edges. The nodes are numbered from 0 to `n-1`.

## Approach
The algorithm uses a union-find data structure to check if the graph is connected and has no cycles. We iterate through the edges, and for each edge, we check if the two nodes are already in the same connected component. If they are, then the graph has a cycle, and we return false.

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

bool validTree(int n, vector<vector<int>>& edges) {
    UnionFind uf(n);
    if (edges.size() != n - 1) {
        return false;
    }
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
```

## Test Cases
```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

## Key Takeaways
- A valid tree must have `n-1` edges.
- We can use a union-find data structure to check if a graph is connected and has no cycles.
- The `find` operation in the union-find data structure can be optimized using path compression.