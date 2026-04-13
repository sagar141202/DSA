# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as an undirected graph, and we are given a list of edges, where each edge is represented as a pair of nodes. The nodes are numbered from 1 to n, where n is the number of nodes in the graph. The input is a 2D vector of size n, where each element is a pair of nodes. The output is the redundant connection, which is the last edge that causes a cycle in the graph. If there are multiple redundant connections, we return the last one.

## Approach
We can use a union-find algorithm to detect the cycle in the graph. The union-find algorithm keeps track of the connected components in the graph. When we add an edge to the graph, we check if the two nodes are already in the same connected component. If they are, it means that adding this edge will create a cycle, so we return this edge as the redundant connection.

## Complexity
- Time: O(n * alpha(n))
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
    UnionFind uf(edges.size() + 1);
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
    cout << result[0] << " " << result[1] << endl;
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
- The union-find algorithm is used to detect cycles in the graph.
- The `find` function is used to find the root of a node, and the `unionNodes` function is used to union two nodes.
- The time complexity of the union-find algorithm is O(n * alpha(n)), where alpha(n) is the inverse Ackermann function, which grows very slowly.