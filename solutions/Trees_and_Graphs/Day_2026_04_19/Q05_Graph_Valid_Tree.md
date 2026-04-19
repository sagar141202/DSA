# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of edges, determine if the given edges form a valid tree. A valid tree is a graph that is connected and has no cycles. The nodes are numbered from 0 to `n-1`. The edges are given as an array of pairs, where each pair represents an edge between two nodes.

## Approach
The approach is to use a Union-Find algorithm to check for connectivity and cycles. We iterate over the edges, and for each edge, we check if the two nodes are already connected. If they are, it means we have a cycle, and the graph is not a valid tree.

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
            return false;  // cycle detected
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
- The Union-Find algorithm is used to detect cycles and check connectivity in the graph.
- The `find` operation is used to find the root of a node, and the `unionSet` operation is used to merge two sets.
- The time complexity of the Union-Find algorithm is O(n + m * α(n)), where n is the number of nodes and m is the number of edges.