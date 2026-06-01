# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as an undirected graph, and the edges are given as pairs of nodes. The nodes are numbered from 1 to n, where n is the number of nodes in the graph. The edges are given as a list of pairs, where each pair represents an edge between two nodes. We need to find the first redundant connection in the list of edges. If there are multiple redundant connections, we need to find the first one.

## Approach
We can use a union-find algorithm to solve this problem. The idea is to iterate over the edges and add them to the graph one by one. If adding an edge does not change the connectivity of the graph, then it is a redundant connection. We can use a union-find data structure to keep track of the connectivity of the graph.

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

    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
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
        uf.unionSet(x, y);
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
- We can use a union-find algorithm to solve this problem.
- The union-find algorithm helps us to keep track of the connectivity of the graph.
- We need to iterate over the edges and add them to the graph one by one to find the first redundant connection.