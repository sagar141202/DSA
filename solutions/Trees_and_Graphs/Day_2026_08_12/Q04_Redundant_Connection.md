# Redundant Connection

## Problem Statement
In this problem, we are given a list of edges in a graph, and we need to find the redundant connection. A redundant connection is an edge that, when removed, does not increase the number of connected components in the graph. The graph is represented as an undirected graph, and it is guaranteed that the graph is connected. The input is a 2D vector of integers, where each integer represents a node in the graph, and the vector represents an edge between the two nodes. The output should be a vector of two integers, representing the redundant connection.

## Approach
We can solve this problem using a Union-Find data structure, which keeps track of the connected components in the graph. We iterate over the edges and use the Union-Find data structure to check if the two nodes are already in the same connected component. If they are, then the current edge is the redundant connection.

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
            if (rank[rootx] < rank[rooty]) {
                parent[rootx] = rooty;
            } else if (rank[rootx] > rank[rooty]) {
                parent[rooty] = rootx;
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
    cout << "Redundant connection: [" << result[0] << ", " << result[1] << "]" << endl;
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
- The Union-Find data structure is useful for keeping track of connected components in a graph.
- The `find` operation in Union-Find has an amortized time complexity of O(alpha(n)), where alpha(n) is the inverse Ackermann function.
- The `unionSet` operation in Union-Find has an amortized time complexity of O(alpha(n)), where alpha(n) is the inverse Ackermann function.