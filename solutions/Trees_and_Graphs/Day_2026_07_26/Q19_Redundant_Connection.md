# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as a list of edges, where each edge is a pair of nodes. The nodes are numbered from 1 to n, where n is the number of nodes. The edges are undirected. The input is a 2D vector of integers, where each integer represents a node in the graph. The output is a vector of two integers, representing the redundant connection.

## Approach
We can solve this problem using a Union-Find algorithm, which keeps track of the connected components in the graph. We iterate over the edges and check if the two nodes are already in the same connected component. If they are, then the current edge is the redundant connection.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) : parent(n + 1) {
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

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        UnionFind uf(n);
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
};
```

## Test Cases
```
Input: [[1,2],[1,3],[2,3]]
Output: [2,3]
Input: [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

## Key Takeaways
- The Union-Find algorithm is useful for solving problems involving connected components in a graph.
- The `find` operation in the Union-Find algorithm can be optimized using path compression.
- The `union` operation in the Union-Find algorithm can be optimized using union by rank.