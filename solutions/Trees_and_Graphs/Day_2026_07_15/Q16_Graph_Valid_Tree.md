# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of edges, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles. The input array `edges` is of size `n-1` where `edges[i] = [u, v]` represents a bidirectional edge between nodes `u` and `v`. The nodes are numbered from 0 to `n-1`. The function should return `true` if the graph is a valid tree, otherwise `false`. For example, given `n = 5` and `edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`, the function should return `true` because the graph is a valid tree.

## Approach
The algorithm uses a Union-Find data structure to check if the graph is connected and has no cycles. It iterates over the edges and checks if the two nodes of each edge are in the same connected component. If they are, it means there is a cycle in the graph. If not, it merges the two components.

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
    for (auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        if (uf.find(u) == uf.find(v)) {
            return false; // cycle detected
        }
        uf.unionNodes(u, v);
    }
    // check if all nodes are connected
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
Input: n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true
Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false
```

## Key Takeaways
- Use Union-Find data structure to detect cycles in the graph.
- Check if all nodes are connected by verifying that all nodes have the same root.
- The algorithm has a time complexity of O(n + m * α(n)) where n is the number of nodes and m is the number of edges.