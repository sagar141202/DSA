# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection, which is the edge that, when removed, will make the graph a tree (i.e., connected and acyclic). The graph is represented as an adjacency list, where each edge is a pair of nodes. The input is a 2D vector of integers, where each sub-vector represents an edge in the graph. The output should be a vector of two integers representing the redundant connection.

## Approach
We can use a Union-Find algorithm to detect the cycle in the graph. The idea is to iterate over the edges and for each edge, check if the two nodes are already connected. If they are, then this edge is the redundant connection.

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
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
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
Input: [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
Output: [1, 4]
```

## Key Takeaways
- Use Union-Find algorithm to detect cycle in the graph.
- The `find` function is used to find the root of a node, and the `unionSet` function is used to union two sets.
- The time complexity is O(n alpha(n)) due to the use of Union-Find algorithm, where alpha(n) is the inverse Ackermann function.