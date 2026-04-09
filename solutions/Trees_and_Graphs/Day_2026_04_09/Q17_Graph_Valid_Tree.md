# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges `edges` where `edges[i] = [u, v]`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles, and it has `n-1` edges. The nodes are numbered from 0 to `n-1`. Return `true` if the graph is a valid tree, otherwise return `false`. For example, given `n = 5` and `edges = [[0,1],[0,2],[0,3],[1,4]]`, the function should return `true` because the graph is a valid tree.

## Approach
The algorithm uses a Union-Find data structure to check for cycles and connectivity. It iterates over the edges, adding them to the Union-Find data structure. If a cycle is detected, the function returns `false`. After iterating over all edges, the function checks if all nodes are connected.

## Complexity
- Time: O(n + m * alpha(n))
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;

    UnionFind(int n) : parent(n), rank(n, 0) {
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

    for (const auto& edge : edges) {
        int x = edge[0];
        int y = edge[1];

        if (uf.find(x) == uf.find(y)) {
            return false;
        }

        uf.unionSet(x, y);
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
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

## Key Takeaways
- Use Union-Find data structure to detect cycles and check connectivity in a graph.
- The number of edges in a valid tree is `n-1`, where `n` is the number of nodes.
- A valid tree must be connected and have no cycles.