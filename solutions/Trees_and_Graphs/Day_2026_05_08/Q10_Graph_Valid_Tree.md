# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges `edges` where `edges[i] = [u, v]` represents a connection between nodes `u` and `v`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles, and it has `n-1` edges. The nodes are numbered from 0 to `n-1`.

## Approach
To solve this problem, we can use a union-find algorithm to check if the graph is connected and has no cycles. We will iterate through the edges and use the union-find algorithm to union the nodes. If we find a cycle, we will return false. If we have iterated through all the edges and the number of connected components is 1, we will return true.

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

bool isValidTree(int n, vector<vector<int>>& edges) {
    UnionFind uf(n);
    for (auto& edge : edges) {
        int x = edge[0];
        int y = edge[1];
        if (uf.find(x) == uf.find(y)) {
            return false;
        }
        uf.unionNodes(x, y);
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (uf.parent[i] == i) {
            count++;
        }
    }
    return count == 1 && edges.size() == n - 1;
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
- The union-find algorithm can be used to detect cycles in a graph.
- The time complexity of the union-find algorithm is O(n + m * alpha(n)), where `alpha(n)` is the inverse Ackermann function.