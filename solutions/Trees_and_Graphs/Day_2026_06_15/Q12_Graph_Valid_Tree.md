# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles. The input is an integer `n` representing the number of nodes and a 2D vector `edges` where each sub-vector represents an edge between two nodes. The nodes are numbered from 0 to `n-1`. Return `true` if the graph is a valid tree, otherwise return `false`.

## Approach
We can use depth-first search (DFS) or union-find algorithm to check if the graph is connected and has no cycles. Here, we'll use the union-find approach for its simplicity and efficiency. The idea is to iterate over all edges, and for each edge, check if the two nodes are in the same connected component. If they are, it means we have a cycle, so we return `false`. If not, we merge the two components.

## Complexity
- Time: O(n + m * α(n))
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;

    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
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
        int rootx = find(x);
        int rooty = find(y);
        if (rootx != rooty) {
            if (rank[rootx] > rank[rooty]) {
                parent[rooty] = rootx;
            } else if (rank[rootx] < rank[rooty]) {
                parent[rootx] = rooty;
            } else {
                parent[rooty] = rootx;
                rank[rootx]++;
            }
        }
    }
};

class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (n - 1 != edges.size()) return false;
        UnionFind uf(n);
        for (auto& edge : edges) {
            int x = edge[0], y = edge[1];
            if (uf.find(x) == uf.find(y)) return false;
            uf.unionSet(x, y);
        }
        return true;
    }
};
```

## Test Cases
```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

## Key Takeaways
- Use union-find to efficiently check for cycles and connectivity in a graph.
- The time complexity is dominated by the union-find operations, which take `α(n)` time per operation, where `α(n)` is the inverse Ackermann function, growing very slowly.
- Always consider the base case where the number of edges is not `n-1`, which immediately indicates the graph is not a tree.