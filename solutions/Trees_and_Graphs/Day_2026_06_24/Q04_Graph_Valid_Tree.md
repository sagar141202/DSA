# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges `edges` where `edges[i] = [u, v]` represents a connection between nodes `u` and `v`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles, i.e., it is possible to reach every node from every other node, and there are no redundant edges. The graph has `n` nodes labeled from `0` to `n - 1`. The array `edges` has a length of `n - 1` and `edges[i] = [u, v]` represents a connection between nodes `u` and `v`. The constraints are: `1 <= n <= 2000`, `0 <= u, v <= n - 1`, and for any `u, v`, `u != v`.

## Approach
To determine if the graph is a valid tree, we use a depth-first search (DFS) or union-find algorithm to check for connectivity and cycles. The DFS approach involves traversing the graph and checking if all nodes are reachable from an arbitrary starting node and if there are any back edges that would indicate a cycle. The union-find approach involves maintaining a set of connected components and checking if adding each edge would merge two separate components or create a cycle within a single component.

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

    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
};

bool validTree(int n, vector<vector<int>>& edges) {
    UnionFind uf(n);
    for (const auto& edge : edges) {
        int u = edge[0], v = edge[1];
        if (uf.find(u) == uf.find(v)) {
            return false; // Cycle detected
        }
        uf.unionSet(u, v);
    }
    // Check if all nodes are connected
    int root = uf.find(0);
    for (int i = 1; i < n; i++) {
        if (uf.find(i) != root) {
            return false; // Not all nodes are connected
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
- A graph is considered a valid tree if it is connected and has no cycles.
- The union-find algorithm can efficiently check for connectivity and cycles in a graph.
- The DFS approach can also be used but may have higher overhead due to the recursive calls or stack management.