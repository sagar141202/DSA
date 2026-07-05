# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges `edges` where `edges[i] = [u, v]`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles. The graph will have `n` nodes numbered from 0 to `n - 1`. The array `edges` will have `m` edges. The constraints are: `1 <= n <= 10^5` and `0 <= m <= 10^5`. For example, if `n = 5` and `edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`, the function should return `true` because the graph is a valid tree.

## Approach
To solve this problem, we can use a union-find algorithm to check if the graph is connected and has no cycles. We iterate over each edge, and for each edge, we check if the two nodes are already in the same set. If they are, it means we have a cycle, and the graph is not a valid tree. If they are not, we union the two sets.

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

    void unionSets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
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
        uf.unionSets(x, y);
    }
    // Check if all nodes are connected
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
- Use a union-find algorithm to detect cycles in a graph.
- Check if all nodes are connected by verifying that they all belong to the same set.
- The time complexity of the union-find algorithm is nearly constant time, O(α(n)), where α(n) is the inverse Ackermann function, which grows very slowly.