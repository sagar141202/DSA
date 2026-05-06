# Redundant Connection

## Problem Statement
In this problem, we are given an undirected graph with `n` nodes and `n` edges. The task is to find the redundant connection in the graph, which is the edge that, when removed, will make the graph a tree (i.e., connected and acyclic). We can assume that the input graph is connected. The graph is represented as a list of edges, where each edge is a pair of nodes.

## Approach
We can use a Union-Find algorithm to solve this problem. The idea is to iterate over the edges and check if the two nodes of an edge are already in the same connected component. If they are, then this edge is the redundant connection.

## Complexity
- Time: O(n alpha(n))
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
        parent.resize(n + 1);
        rank.resize(n + 1, 0);
        for (int i = 0; i <= n; i++) {
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

vector<int> findRedundantConnection(vector<vector<int>>& edges) {
    UnionFind uf(edges.size() + 1);
    for (auto& edge : edges) {
        int x = edge[0];
        int y = edge[1];
        if (uf.find(x) == uf.find(y)) {
            return edge;
        }
        uf.unionSet(x, y);
    }
    return {};
}

int main() {
    vector<vector<int>> edges = {{1, 2}, {1, 3}, {2, 3}};
    vector<int> result = findRedundantConnection(edges);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}
```

## Test Cases
```
Input: [[1, 2], [1, 3], [2, 3]]
Output: [2, 3]
```

## Key Takeaways
- The Union-Find algorithm is used to detect cycles in a graph.
- The `find` operation is used to find the representative of a set, and the `union` operation is used to merge two sets.
- The `rank` array is used to optimize the `union` operation by always attaching the smaller tree to the larger tree.