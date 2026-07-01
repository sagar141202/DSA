# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges `edges` where `edges[i] = [u_i, v_i]`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles. The graph is undirected and has `n` nodes numbered from 0 to `n-1`. The array `edges` represents the edges of the graph, where `edges[i] = [u_i, v_i]` means there is an edge between nodes `u_i` and `v_i`. The input will always be a simple graph (no self-loops or multiple edges between the same nodes). Return `true` if the graph is a valid tree, and `false` otherwise. For example, given `n = 5` and `edges = [[0,1],[0,2],[0,3],[1,4]]`, the output should be `true` because the graph is a valid tree. However, given `n = 5` and `edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]`, the output should be `false` because the graph contains a cycle.

## Approach
To solve this problem, we can use a union-find algorithm to check for connectivity and a depth-first search (DFS) to detect cycles. We will iterate over all edges, adding them to our union-find data structure and checking for cycles using DFS.

## Complexity
- Time: O(n + m * α(n))
- Space: O(n + m)

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

    void unionSet(int x, int y) {
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
        if (n == 0 || edges.size() != n - 1) return false;

        UnionFind uf(n);
        for (auto& edge : edges) {
            int x = edge[0];
            int y = edge[1];
            if (uf.find(x) == uf.find(y)) return false; // cycle detected
            uf.unionSet(x, y);
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
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

## Key Takeaways
- A union-find data structure can be used to efficiently check for connectivity in a graph.
- DFS can be used to detect cycles in a graph, but in this case, the union-find approach is more efficient.
- The time complexity of the union-find operations (find and union) is nearly constant, making it suitable for large inputs.