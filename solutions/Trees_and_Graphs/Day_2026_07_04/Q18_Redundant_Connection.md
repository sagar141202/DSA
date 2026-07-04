# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as an adjacency list, where each edge is represented as a pair of nodes. The input is a 2D vector of integers, where each integer represents a node in the graph. The output should be a vector of two integers representing the redundant connection. For example, given the input `[[1,2],[1,3],[2,3]]`, the output should be `[2,3]`. The constraints are that the input graph is connected, and the number of nodes is equal to the number of edges.

## Approach
We can use a union-find algorithm to solve this problem. The idea is to iterate over the edges and check if the two nodes are already connected. If they are, then the current edge is the redundant connection. We can use a parent array to keep track of the parent of each node.

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

    void union_(int x, int y) {
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
        uf.union_(x, y);
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
- Use union-find algorithm to solve the problem
- Keep track of the parent of each node using a parent array
- Check if the two nodes are already connected before adding the edge to the graph