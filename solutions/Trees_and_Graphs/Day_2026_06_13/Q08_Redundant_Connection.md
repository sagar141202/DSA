# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as an adjacency list, where each edge is represented as a pair of nodes. The input is a 2D vector of integers, where each integer represents a node in the graph. The output is a vector of two integers representing the redundant connection. The graph is guaranteed to be connected, and there are no self-loops or multiple edges between the same pair of nodes. For example, given the input `[[1,2],[1,3],[2,3]]`, the output should be `[2,3]`, because the edge between nodes 2 and 3 is redundant.

## Approach
We can solve this problem by using a union-find data structure to keep track of the connected components in the graph. We iterate over the edges and use the union-find data structure to check if the two nodes of an edge are already in the same connected component. If they are, then the edge is redundant.

## Complexity
- Time: O(n alpha(n))
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
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
    for (const auto& edge : edges) {
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
- The union-find data structure is useful for solving problems that involve finding connected components in a graph.
- The `find` operation in the union-find data structure returns the representative of the set that contains a given element.
- The `union` operation in the union-find data structure merges two sets into a single set.