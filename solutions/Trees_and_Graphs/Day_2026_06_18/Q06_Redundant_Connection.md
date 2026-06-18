# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as a list of edges, where each edge is a pair of nodes. The nodes are numbered from 1 to n, where n is the number of nodes. The edges are undirected. The input is a 2D vector of integers, where each inner vector represents an edge. The output is a vector of two integers representing the redundant connection.

## Approach
We can use a union-find data structure to solve this problem. The idea is to iterate over the edges and add them to the union-find data structure. If an edge is added and the two nodes are already connected, then this edge is the redundant connection.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) {
        parent.resize(n + 1);
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
    void unionNodes(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
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
        uf.unionNodes(x, y);
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
- Use a union-find data structure to keep track of connected components in the graph.
- Iterate over the edges and add them to the union-find data structure.
- If an edge is added and the two nodes are already connected, then this edge is the redundant connection.