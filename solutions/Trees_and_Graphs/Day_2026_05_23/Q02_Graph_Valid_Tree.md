# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of edges, determine if the given edges form a valid tree. A valid tree is a graph that is connected and has no cycles. The input array `edges` is of size `n-1`, where `edges[i] = [u, v]` represents a bidirectional edge between nodes `u` and `v`. The nodes are numbered from 0 to `n-1`. The function should return `true` if the edges form a valid tree and `false` otherwise.

## Approach
We can use a Union-Find algorithm to check if the graph is connected and has no cycles. The algorithm works by maintaining a set of connected components and merging them as we iterate through the edges. If we encounter an edge that connects two nodes in the same component, then the graph has a cycle.

## Complexity
- Time: O(n α(n))
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
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

## Key Takeaways
- Use Union-Find algorithm to check for connectivity and cycles in a graph.
- The time complexity of the Union-Find algorithm is O(n α(n)) due to the use of path compression and union by rank.
- The space complexity is O(n) for storing the parent and rank arrays.