# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as a list of edges, where each edge is a pair of nodes. The nodes are numbered from 1 to n, where n is the number of nodes. The graph is guaranteed to be connected. The input is a 2D vector of integers, where each integer represents a node in the graph. The output is a vector of two integers, representing the redundant connection.

## Approach
We can solve this problem using the Union-Find algorithm, which is a data structure that keeps track of the connected components in a graph. We iterate over the edges and add them to the graph one by one, checking if the two nodes of the edge are already in the same connected component. If they are, then the edge is redundant.

## Complexity
- Time: O(n^2)
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
        for (int i = 1; i <= n; i++) {
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
        int root_x = find(x);
        int root_y = find(y);
        if (root_x != root_y) {
            parent[root_x] = root_y;
        }
    }
};

vector<int> findRedundantConnection(vector<vector<int>>& edges) {
    int n = edges.size();
    UnionFind uf(n);
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
```

## Key Takeaways
- The Union-Find algorithm is useful for solving problems that involve connected components in a graph.
- The time complexity of the Union-Find algorithm can be improved using path compression and union by rank.
- The problem can be solved by iterating over the edges and checking if the two nodes of the edge are already in the same connected component.