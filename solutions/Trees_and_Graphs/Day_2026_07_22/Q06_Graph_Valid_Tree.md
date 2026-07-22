# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges `edges` where `edges[i] = [u, v]` represents a bidirectional edge between node `u` and node `v`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles, and it has `n-1` edges. The nodes are numbered from 0 to `n-1`.

## Approach
We can use a Union-Find algorithm to detect cycles and check if all nodes are connected. If the number of edges is `n-1` and there are no cycles, then the graph is a valid tree. The algorithm iterates over the edges, adding them to the Union-Find data structure and checking for cycles.

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

bool validTree(int n, vector<vector<int>>& edges) {
    if (edges.size() != n - 1) {
        return false;
    }
    UnionFind uf(n);
    for (auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        if (uf.find(u) == uf.find(v)) {
            return false;
        }
        uf.unionNodes(u, v);
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
- Use Union-Find algorithm to detect cycles and check connectivity.
- The number of edges in a valid tree is `n-1`.
- All nodes must be connected in a valid tree.