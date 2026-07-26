# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of edges, determine if the given edges form a valid tree. A valid tree is a graph that is connected and has no cycles. The input array `edges` is of size `n-1`, where `edges[i] = [u, v]` represents an edge between nodes `u` and `v`. The nodes are numbered from 0 to `n-1`. The function should return `true` if the given edges form a valid tree, and `false` otherwise.

## Approach
We can use a Union-Find algorithm to check if the graph is connected and has no cycles. The algorithm works by iterating over the edges and checking if the two nodes are already in the same set. If they are, it means a cycle is detected. If not, we merge the two sets.

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
    for (auto edge : edges) {
        int x = edge[0];
        int y = edge[1];
        if (uf.find(x) == uf.find(y)) {
            return false;
        }
        uf.unionSet(x, y);
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (uf.parent[i] == i) {
            count++;
        }
    }
    return count == 1;
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
- Use a Union-Find algorithm to check for cycles and connectivity in a graph.
- The Union-Find algorithm works by maintaining a set of nodes and their parents, and merging sets when edges are added.
- The time complexity of the Union-Find algorithm is O(n + m * α(n)), where n is the number of nodes and m is the number of edges.