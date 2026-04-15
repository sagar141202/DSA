# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as an array of pairs, where each pair represents an edge between two nodes. The nodes are numbered from 1 to n, where n is the number of nodes. The input is guaranteed to be a valid graph with n nodes and n-1 or more edges. We need to return the redundant connection, which is the last edge that causes a cycle in the graph.

## Approach
We can use a union-find data structure to solve this problem. The idea is to iterate over the edges and check if the two nodes of an edge are already connected. If they are, then the edge is redundant. We can use a parent array to keep track of the parent of each node.

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
- Use a union-find data structure to keep track of connected components in the graph.
- Iterate over the edges and check if the two nodes of an edge are already connected.
- If they are, then the edge is redundant and we can return it as the result.