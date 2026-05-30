# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not increase the number of connected components in the graph. The graph is represented as an adjacency list, where each edge is a pair of nodes. We can assume that the input graph is connected and has no self-loops or parallel edges. The function should return the redundant connection.

## Approach
We can use a union-find data structure to keep track of the connected components in the graph. We iterate over the edges and for each edge, we check if the two nodes are already in the same connected component. If they are, then this edge is the redundant connection. If not, we union the two nodes.

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

    void unionNodes(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
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
        uf.unionNodes(edge[0], edge[1]);
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
- The union-find data structure is used to keep track of the connected components in the graph.
- The time complexity is O(n alpha(n)) due to the use of the union-find data structure, where alpha(n) is the inverse Ackermann function.
- The space complexity is O(n) for storing the parent and rank arrays in the union-find data structure.