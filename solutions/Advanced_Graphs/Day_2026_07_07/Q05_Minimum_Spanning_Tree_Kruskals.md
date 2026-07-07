# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list or edge list, where each edge is a tuple of (u, v, w) representing the vertices u and v connected by an edge with weight w. The constraints are 1 ≤ V ≤ 10^5 and 1 ≤ E ≤ 10^6.

## Approach
Kruskal's algorithm sorts the edges by weight and iterates over them, adding each edge to the MST if it does not form a cycle. This is achieved using a disjoint-set data structure to keep track of connected components. The algorithm runs until all vertices are connected or all edges have been considered.

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

int kruskal(vector<vector<int>>& edges, int V) {
    sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[2] < b[2];
    });

    DisjointSet ds(V);
    int totalWeight = 0;
    for (const auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        int w = edge[2];
        if (ds.find(u) != ds.find(v)) {
            ds.unionSet(u, v);
            totalWeight += w;
        }
    }
    return totalWeight;
}

int main() {
    int V = 4;
    vector<vector<int>> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    cout << "Minimum Spanning Tree weight: " << kruskal(edges, V) << endl;
    return 0;
}
```

## Test Cases
```
Input: V = 4, edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
Output: Minimum Spanning Tree weight: 19
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph by sorting the edges and adding them to the MST if they do not form a cycle.
- The disjoint-set data structure is used to keep track of connected components in the graph.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V) due to sorting the edges.