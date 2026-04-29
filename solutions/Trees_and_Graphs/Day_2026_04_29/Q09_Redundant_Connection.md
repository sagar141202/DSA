# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as an adjacency list, where each edge is represented as a pair of nodes. The input is a 2D vector of integers, where each integer represents a node in the graph. The output should be a vector of two integers representing the redundant connection. The graph is guaranteed to be connected, and there will be exactly one redundant connection.

## Approach
We can solve this problem using a Union-Find algorithm, which keeps track of the connected components in the graph. We iterate over the edges and union the nodes. If the nodes are already in the same connected component, then the current edge is the redundant connection.

## Complexity
- Time: O(n * α(n))
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
    // example usage
    vector<vector<int>> edges = {{1, 2}, {1, 3}, {2, 3}};
    vector<int> result = findRedundantConnection(edges);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}
```

## Test Cases
```
Input: [[1,2],[1,3],[2,3]]
Output: [2,3]
```

## Key Takeaways
- Use Union-Find algorithm to keep track of connected components in the graph.
- Iterate over the edges and union the nodes to find the redundant connection.
- The time complexity is O(n * α(n)) due to the Union-Find operations, where α(n) is the inverse Ackermann function.