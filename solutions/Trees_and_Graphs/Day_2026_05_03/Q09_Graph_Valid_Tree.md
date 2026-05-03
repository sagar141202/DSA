# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of edges, determine if the given edges form a valid tree. A valid tree is a graph that is connected and has no cycles. The input array `edges` is of size `n-1` where `edges[i] = [u, v]` represents a bidirectional edge between node `u` and node `v`. The nodes are numbered from 0 to `n-1`. If the edges form a valid tree, return `true`; otherwise, return `false`. For example, given `n = 5` and `edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`, the function should return `true` because the given edges form a valid tree.

## Approach
We can use a Union-Find algorithm to check if the graph is connected and has no cycles. The Union-Find algorithm uses a disjoint-set data structure to keep track of the connected components in the graph. If the number of connected components is 1 after adding all the edges, then the graph is connected. We also check for cycles by verifying if two nodes are in the same connected component before adding an edge between them.

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
            return false; // cycle detected
        }
        uf.unionSet(x, y);
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (uf.parent[i] == i) {
            count++;
        }
    }
    return count == 1; // graph is connected
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
- Use Union-Find algorithm to detect cycles and check connectivity in a graph.
- The Union-Find algorithm has an average time complexity of O(α(n)) for both find and union operations, where α(n) is the inverse Ackermann function.
- The graph is connected if the number of connected components is 1 after adding all the edges.