# Redundant Connection

## Problem Statement
In this problem, we are given a series of connections between nodes in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as an array of edges, where each edge is an array of two integers representing the nodes connected by the edge. The nodes are 1-indexed, and the edges are given in no particular order. The function should return the redundant connection.

## Approach
We can use a Union-Find algorithm to solve this problem. The algorithm works by iterating over the edges and checking if the two nodes are already connected. If they are, then the current edge is redundant.

## Complexity
- Time: O(n alpha(n))
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
    for (const auto& edge : edges) {
        if (uf.find(edge[0]) == uf.find(edge[1])) {
            return edge;
        }
        uf.unionNodes(edge[0], edge[1]);
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
- The Union-Find algorithm is useful for solving graph connectivity problems.
- The time complexity of the Union-Find algorithm can be optimized using path compression and union by rank.
- The space complexity of the algorithm is O(n), where n is the number of nodes in the graph.