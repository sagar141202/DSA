# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as a list of edges, where each edge is a pair of nodes. The nodes are numbered from 1 to n, where n is the number of nodes in the graph. The edges are undirected and unweighted. We need to find the redundant connection in the graph.

## Approach
We can use a Union-Find algorithm to solve this problem. The idea is to iterate over the edges and add them to the Union-Find data structure. If an edge connects two nodes that are already in the same set, then it is a redundant connection.

## Complexity
- Time: O(n)
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
    UnionFind uf(edges.size() + 1);
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
- The Union-Find algorithm is useful for solving problems involving connectivity in graphs.
- The time complexity of the Union-Find algorithm is O(n) for n operations, making it efficient for large graphs.
- The space complexity of the Union-Find algorithm is O(n) for storing the parent array.