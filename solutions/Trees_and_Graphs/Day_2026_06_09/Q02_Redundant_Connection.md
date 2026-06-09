# Redundant Connection

## Problem Statement
In this problem, we are given an undirected graph with n nodes and n-1 edges, along with one extra edge that creates a cycle. The task is to find this extra edge, also known as the redundant connection. The graph is represented as a list of edges, where each edge is a pair of nodes. The nodes are numbered from 1 to n. The function should return the redundant edge.

## Approach
We can solve this problem using the Union-Find algorithm, which is used to detect cycles in a graph. The idea is to iterate over the edges and use the Union-Find algorithm to check if adding an edge creates a cycle.

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
        int x = edge[0];
        int y = edge[1];
        if (uf.find(x) == uf.find(y)) {
            return edge;
        }
        uf.unionNodes(x, y);
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
- The Union-Find algorithm can be used to detect cycles in a graph.
- The time complexity of the Union-Find algorithm is O(n) for n nodes.
- The space complexity of the Union-Find algorithm is O(n) for n nodes.