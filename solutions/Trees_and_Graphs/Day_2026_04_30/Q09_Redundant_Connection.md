# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as an undirected graph, and it is guaranteed that the graph is connected. The input is a 2D vector of integers, where each integer represents a node in the graph, and the size of the vector is the number of edges. The constraints are 1 <= n <= 1000, where n is the number of nodes, and 1 <= edges.length <= n - 1. For example, given the input [[1,2],[1,3],[2,3]], the output is [2,3] because removing the edge between nodes 2 and 3 does not affect the connectivity of the graph.

## Approach
The approach to solve this problem is to use the Union-Find algorithm to detect cycles in the graph. We iterate over each edge in the graph, and for each edge, we check if the two nodes are already connected. If they are, then the edge is redundant, and we return it. If not, we union the two nodes.

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
- The Union-Find algorithm is used to detect cycles in the graph.
- The time complexity is O(n * alpha(n)) due to the path compression in the Union-Find algorithm.
- The space complexity is O(n) for storing the parent array in the Union-Find algorithm.