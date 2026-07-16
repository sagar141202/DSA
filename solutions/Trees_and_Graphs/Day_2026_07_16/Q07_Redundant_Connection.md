# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as a list of edges, where each edge is a pair of nodes. The nodes are numbered from 1 to n, where n is the number of nodes. The goal is to find the redundant connection and return it as a pair of nodes. If there are multiple redundant connections, we can return any one of them. For example, given the edges [[1,2],[1,3],[2,3]], the redundant connection is [2,3] because removing it does not affect the connectivity of the graph.

## Approach
We can use a union-find algorithm to solve this problem. The idea is to iterate over the edges and use the union-find algorithm to check if the two nodes of an edge are already connected. If they are, then the edge is redundant. We can use a parent array to keep track of the parent of each node.

## Complexity
- Time: O(n)
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
- Use a union-find algorithm to keep track of connected components in the graph.
- Iterate over the edges and check if the two nodes of an edge are already connected using the union-find algorithm.
- If the two nodes are already connected, then the edge is redundant and we can return it.