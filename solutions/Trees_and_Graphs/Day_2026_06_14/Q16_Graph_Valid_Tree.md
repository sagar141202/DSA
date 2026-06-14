# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of edges, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles. The nodes are labeled from 0 to `n-1`, and the edges are given as pairs of node indices. The graph has `n-1` edges. If the graph is a valid tree, return `true`; otherwise, return `false`. For example, given `n = 5` and `edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`, the function should return `true`, but given `n = 5` and `edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]`, the function should return `false` because the graph has a cycle.

## Approach
The approach is to use a Union-Find data structure to check for cycles and to verify that all nodes are connected. If we encounter an edge that connects two nodes that are already in the same set, then there is a cycle. We also need to check that all nodes are in the same set after processing all edges.

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

bool validTree(int n, vector<vector<int>>& edges) {
    UnionFind uf(n);
    for (auto& edge : edges) {
        int x = edge[0];
        int y = edge[1];
        if (uf.find(x) == uf.find(y)) {
            return false; // cycle detected
        }
        uf.unionSet(x, y);
    }
    // check if all nodes are in the same set
    int root = uf.find(0);
    for (int i = 1; i < n; i++) {
        if (uf.find(i) != root) {
            return false; // not all nodes are connected
        }
    }
    return true;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0, 1}, {0, 2}, {0, 3}, {1, 4}};
    cout << boolalpha << validTree(n, edges) << endl;
    return 0;
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
- Use a Union-Find data structure to detect cycles and verify connectivity in a graph.
- The time complexity of the Union-Find operations (find and union) is nearly constant, thanks to path compression and union by rank.
- Always check for both cycle detection and connectivity verification to ensure the graph is a valid tree.