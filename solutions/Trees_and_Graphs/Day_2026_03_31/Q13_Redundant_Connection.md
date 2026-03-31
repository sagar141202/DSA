# Redundant Connection

## Problem Statement
In a graph, a redundant connection is an edge that, when removed, does not affect the connectivity of the graph. Given an array of edges in a graph, where each edge is represented as a pair of nodes, find the redundant connection. The graph is represented as an adjacency list, and the nodes are numbered from 1 to n. The input array edges is a 2D array where each sub-array represents an edge between two nodes. The function should return the redundant connection. If there are multiple redundant connections, return the last one.

## Approach
The algorithm uses a union-find data structure to keep track of the connected components in the graph. It iterates over the edges and checks if the two nodes are already connected. If they are, it means that the current edge is a redundant connection.

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
Input: [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
Output: [1, 4]
```

## Key Takeaways
- Use a union-find data structure to keep track of connected components.
- Iterate over the edges and check for redundant connections.
- Return the last redundant connection found.