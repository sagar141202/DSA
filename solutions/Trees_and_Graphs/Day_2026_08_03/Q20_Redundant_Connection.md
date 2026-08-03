# Redundant Connection

## Problem Statement
In a graph, a redundant connection is an edge that can be removed without affecting the connectivity of the graph. Given a list of edges in a graph, find the redundant connection. The graph is represented as an adjacency list, where each edge is a pair of nodes. The input is a 2D vector of integers, where each integer represents a node in the graph. The output is a vector of two integers representing the redundant connection. The graph is guaranteed to have a redundant connection. For example, given the input `[[1,2],[1,3],[2,3]]`, the output should be `[2,3]`.

## Approach
The approach is to use a union-find data structure to detect cycles in the graph. We iterate through the edges and for each edge, we check if the two nodes are already connected. If they are, then the current edge is the redundant connection.

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
            if (rank[rootx] > rank[rooty]) {
                parent[rooty] = rootx;
            } else if (rank[rootx] < rank[rooty]) {
                parent[rootx] = rooty;
            } else {
                parent[rooty] = rootx;
                rank[rootx]++;
            }
        }
    }
};

vector<int> findRedundantConnection(vector<vector<int>>& edges) {
    UnionFind uf(1001);
    for (auto& edge : edges) {
        int x = edge[0];
        int y = edge[1];
        if (uf.find(x) == uf.find(y)) {
            return edge;
        }
        uf.unionSet(x, y);
    }
    return vector<int>();
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
- The union-find data structure is useful for detecting cycles in a graph.
- The `find` operation in union-find data structure can be optimized using path compression.
- The `union` operation in union-find data structure can be optimized using union by rank.