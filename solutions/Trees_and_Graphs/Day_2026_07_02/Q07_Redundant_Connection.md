# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not affect the connectivity of the graph. The graph is represented as an undirected graph, and it is guaranteed that the graph is connected. The input is a 2D vector of integers, where each integer represents a node in the graph. The output should be a vector of two integers representing the redundant connection. For example, given the input `[[1,2],[1,3],[2,3]]`, the output should be `[2,3]`.

## Approach
We can use the Union-Find algorithm to solve this problem. The Union-Find algorithm is a data structure that keeps track of the connected components in a graph. We iterate over the edges in the graph, and for each edge, we check if the two nodes are already connected. If they are, then the current edge is the redundant connection. If they are not, we union the two nodes.

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
- The `find` operation in the Union-Find algorithm returns the representative of the set that the given element belongs to.
- The `unionSet` operation in the Union-Find algorithm merges two sets into one.