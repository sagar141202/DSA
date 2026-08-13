# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges `edges` where `edges[i] = [ui, vi]` represents an edge between nodes `ui` and `vi`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles, and it has `n-1` edges. The nodes are numbered from 0 to `n-1`.

## Approach
To solve this problem, we can use a union-find data structure to check if the graph is connected and has no cycles. We iterate over the edges and for each edge, we check if the two nodes are in the same connected component. If they are, then the graph has a cycle. If not, we union the two components.

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
- A valid tree is a connected graph with no cycles and `n-1` edges.
- We can use a union-find data structure to check if a graph is a valid tree.
- The time complexity of the solution is O(n + m * α(n)) where α(n) is the inverse Ackermann function.