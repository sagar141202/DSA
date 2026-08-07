# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of edges, determine if the given edges form a valid tree. A valid tree is a graph that is connected and has no cycles. The input array `edges` is of size `n-1` where `edges[i] = [u, v]` represents a bidirectional edge between node `u` and node `v`. The nodes are numbered from 0 to `n-1`. The function should return `true` if the edges form a valid tree and `false` otherwise. For example, given `n = 5` and `edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`, the function should return `true` because the given edges form a valid tree.

## Approach
We can use a union-find algorithm to check if the graph is connected and has no cycles. We iterate over each edge and union the two nodes. If the two nodes are already in the same set, it means there is a cycle and we return `false`. After iterating over all edges, we check if all nodes are in the same set. If they are, it means the graph is connected and we return `true`.

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

    void unionSet(int x, int y) {
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
        int x = edge[0];
        int y = edge[1];
        if (uf.find(x) == uf.find(y)) {
            return false;
        }
        uf.unionSet(x, y);
    }
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
- Use union-find algorithm to check for connectivity and cycles in a graph.
- The union-find algorithm has an average time complexity of O(α(n)) per operation, where α(n) is the inverse Ackermann function.
- The space complexity of the union-find algorithm is O(n), where n is the number of nodes in the graph.