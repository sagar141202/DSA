# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as an adjacency list, where each edge is a pair of nodes. The input will be a 2D vector of integers, where each integer represents a node in the graph. The graph is undirected and connected, and it may contain cycles. The goal is to find the redundant connection, which is the edge that can be removed without affecting the connectivity of the graph. For example, given the input `[[1,2],[1,3],[2,3]]`, the output should be `[2,3]`, because removing this edge does not affect the connectivity of the graph.

## Approach
We can use the Union-Find algorithm to solve this problem. The Union-Find algorithm is a data structure that keeps track of the connected components in a graph. We can iterate over the edges and use the Union-Find algorithm to check if the two nodes are already connected. If they are, then the current edge is the redundant connection.

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
        int rootx = find(x);
        int rooty = find(y);
        if (rootx != rooty) {
            parent[rootx] = rooty;
        }
    }
};

vector<int> findRedundantConnection(vector<vector<int>>& edges) {
    UnionFind uf(1001); // assuming the maximum number of nodes is 1000
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
    vector<vector<int>> edges = {{1,2},{1,3},{2,3}};
    vector<int> result = findRedundantConnection(edges);
    cout << "[" << result[0] << "," << result[1] << "]" << endl;
    return 0;
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
- The Union-Find algorithm is useful for finding connected components in a graph.
- We can use the Union-Find algorithm to find the redundant connection in a graph by checking if the two nodes are already connected before adding the edge.
- The time complexity of the Union-Find algorithm is O(n alpha(n)), where n is the number of nodes and alpha(n) is the inverse Ackermann function.