# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as an undirected graph, and the edges are given as pairs of nodes. The graph may contain cycles, and we need to find the edge that is part of a cycle. The input is a 2D vector of integers, where each integer represents a node in the graph. The output is a vector of two integers, representing the nodes of the redundant connection. For example, given the input `[[1,2],[1,3],[2,3]]`, the output should be `[2,3]`, because the edge between nodes 2 and 3 is redundant.

## Approach
We can use a Union-Find algorithm to solve this problem, where we iterate over the edges and check if the two nodes are already connected. If they are, then the current edge is redundant. We can use a parent array to keep track of the connected components.

## Complexity
- Time: O(n*α(n))
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
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
    UnionFind uf(edges.size());
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
```

## Test Cases
```
Input: [[1,2],[1,3],[2,3]]
Output: [2,3]
Input: [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

## Key Takeaways
- Use a Union-Find algorithm to keep track of connected components in the graph.
- Iterate over the edges and check if the two nodes are already connected using the `find` method.
- If the nodes are already connected, then the current edge is redundant and can be returned as the result.