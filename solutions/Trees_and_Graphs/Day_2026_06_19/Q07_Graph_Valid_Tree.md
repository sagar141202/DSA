# Graph Valid Tree

## Problem Statement
Given `n` nodes labeled from `1` to `n`, and an array of undirected edges `edges` where `edges[i] = [ui, vi]`, determine if the graph is a valid tree. A valid tree is a graph where all nodes are connected and there are no cycles. The constraints are: `1 <= n <= 10^4` and `0 <= edges.length <= 10^4`. For example, if `n = 5` and `edges = [[0,1],[0,2],[0,3],[1,4]]`, the graph is a valid tree.

## Approach
We can use a depth-first search (DFS) or union-find algorithm to check if the graph is connected and has no cycles. The key idea is to traverse the graph and keep track of visited nodes. If we encounter a node that is already visited and not the parent of the current node, then there is a cycle.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

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
        UnionFind uf(n);
        for (auto& edge : edges) {
            int x = edge[0];
            int y = edge[1];
            if (uf.find(x) == uf.find(y)) {
                return false;
            }
            uf.unionNodes(x, y);
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
- Use union-find algorithm to check if the graph is connected and has no cycles.
- Keep track of visited nodes to detect cycles.
- Check if all nodes are connected by verifying that all nodes have the same root in the union-find data structure.