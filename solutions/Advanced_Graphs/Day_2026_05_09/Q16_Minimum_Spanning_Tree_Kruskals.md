# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The graph is represented as an adjacency list, where each edge is a tuple of (u, v, w) denoting an edge between vertices u and v with weight w. The MST is a subgraph that connects all vertices with the minimum total weight. The constraints are 1 ≤ V ≤ 10^5 and 1 ≤ E ≤ 10^5.

## Approach
Kruskal's algorithm sorts all edges by weight and iterates over them, adding each edge to the MST if it does not form a cycle. This is achieved using a disjoint-set data structure to keep track of connected components. The algorithm runs until all vertices are connected or all edges have been considered.

## Complexity
- Time: O(E log E) or O(E log V) due to sorting the edges
- Space: O(V + E) for storing the graph and disjoint-set data structure

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class DisjointSet {
public:
    vector<int> parent, rank;
    DisjointSet(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    void unionSets(int x, int y) {
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

int kruskal(vector<vector<int>>& edges, int V) {
    sort(edges.begin(), edges.end(), [](vector<int>& a, vector<int>& b) {
        return a[2] < b[2];
    });
    DisjointSet ds(V);
    int mstWeight = 0;
    for (auto& edge : edges) {
        int u = edge[0], v = edge[1], w = edge[2];
        if (ds.find(u) != ds.find(v)) {
            ds.unionSets(u, v);
            mstWeight += w;
        }
    }
    return mstWeight;
}

int main() {
    int V = 4;
    vector<vector<int>> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    cout << "Minimum Spanning Tree Weight: " << kruskal(edges, V) << endl;
    return 0;
}
```

## Test Cases
```
Input: V = 4, edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
Output: Minimum Spanning Tree Weight: 19
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that always chooses the next edge with the smallest weight that does not form a cycle.
- The disjoint-set data structure is used to efficiently manage the connected components of the graph.
- The time complexity of Kruskal's algorithm is dominated by the sorting of edges, which can be improved using more efficient sorting algorithms or data structures.