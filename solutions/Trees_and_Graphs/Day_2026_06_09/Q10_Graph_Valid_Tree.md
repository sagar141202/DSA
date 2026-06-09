# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of edges `edges` where `edges[i] = [u, v]` represents a bidirectional edge between node `u` and node `v`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles. The graph is undirected, and the nodes are numbered from 0 to `n - 1`.

## Approach
To solve this problem, we can use a union-find algorithm to check for connectivity and cycles. We iterate over the edges, and for each edge, we check if the two nodes are already connected. If they are, it means we have a cycle, and the graph is not a valid tree.

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
            return false; // not all nodes are connected
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
- Use a union-find algorithm to detect cycles and check connectivity in a graph.
- The time complexity of the union-find algorithm is nearly constant time, O(α(n)), where α(n) is the inverse Ackermann function, which grows very slowly.
- The space complexity of the algorithm is O(n), where n is the number of nodes in the graph.