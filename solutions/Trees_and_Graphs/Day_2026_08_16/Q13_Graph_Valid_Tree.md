# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of edges, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles. The input array `edges` is of size `n-1` where `edges[i] = [ui, vi]` represents a bidirectional edge between node `ui` and node `vi`. The nodes are numbered from 0 to `n-1`.

## Approach
To check if the graph is a valid tree, we can use a union-find algorithm to detect cycles. If we can connect all nodes without finding a cycle, the graph is a valid tree. We iterate over all edges, and for each edge, we check if the two nodes are already in the same connected component.

## Complexity
- Time: O(n + m * α(n))
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) : parent(n) {
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
                return false; // cycle detected
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
- Use union-find algorithm to detect cycles in the graph.
- Check if all nodes are connected by verifying that all nodes have the same root.
- The time complexity is nearly linear due to the use of path compression in the union-find algorithm.