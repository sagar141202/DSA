# Redundant Connection

## Problem Statement
In this problem, we are given an undirected graph with n nodes and n - 1 edges, and an additional edge that creates a cycle. The task is to find the redundant edge that causes the cycle. The graph is represented as a list of edges, where each edge is a pair of nodes. The nodes are numbered from 1 to n. The function should return the redundant edge.

## Approach
We can use a Union-Find algorithm to detect the cycle. The algorithm works by iterating over the edges and checking if the two nodes of an edge are already in the same set. If they are, it means that the edge is redundant and creates a cycle.

## Complexity
- Time: O(n alpha(n))
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;

    UnionFind(int n) {
        parent.resize(n + 1);
        rank.resize(n + 1);
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
            rank[i] = 0;
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
            if (rank[rootx] < rank[rooty]) {
                parent[rootx] = rooty;
            } else if (rank[rootx] > rank[rooty]) {
                parent[rooty] = rootx;
            } else {
                parent[rooty] = rootx;
                rank[rootx]++;
            }
        }
    }
};

vector<int> findRedundantConnection(vector<vector<int>>& edges) {
    UnionFind uf(edges.size());
    for (auto& edge : edges) {
        if (uf.find(edge[0]) == uf.find(edge[1])) {
            return edge;
        }
        uf.unionSet(edge[0], edge[1]);
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
- The Union-Find algorithm can be used to detect cycles in a graph.
- The algorithm has a time complexity of O(n alpha(n)) due to the path compression and union by rank optimizations.
- The space complexity is O(n) for storing the parent and rank arrays.