# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list or edge list. The algorithm should handle disjoint sets and union operations efficiently.

## Approach
Kruskal's algorithm works by sorting the edges in non-decreasing order of their weights and then selecting the smallest edge that does not form a cycle. This is achieved using a disjoint set data structure to keep track of connected components. The algorithm iterates through the sorted edges, adding them to the MST if they do not form a cycle.

## Complexity
- Time: O(E log E) or O(E log V) due to sorting the edges
- Space: O(V + E) for storing the graph and disjoint set data structure

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an edge
struct Edge {
    int src, dest, weight;
};

// Define a structure to represent a disjoint set
struct DisjointSet {
    vector<int> parent, rank;
    DisjointSet(int n) {
        parent.resize(n);
        rank.resize(n, 0);
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

// Function to find the Minimum Spanning Tree using Kruskal's algorithm
vector<Edge> kruskal(vector<Edge>& edges, int V) {
    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.weight < b.weight;
    });
    DisjointSet ds(V);
    vector<Edge> mst;
    for (const auto& edge : edges) {
        if (ds.find(edge.src) != ds.find(edge.dest)) {
            mst.push_back(edge);
            ds.unionSets(edge.src, edge.dest);
        }
    }
    return mst;
}

int main() {
    int V = 4;
    vector<Edge> edges = {
        {0, 1, 10},
        {0, 2, 6},
        {0, 3, 5},
        {1, 3, 15},
        {2, 3, 4}
    };
    vector<Edge> mst = kruskal(edges, V);
    cout << "Minimum Spanning Tree:" << endl;
    for (const auto& edge : mst) {
        cout << "Edge: " << edge.src << " - " << edge.dest << ", Weight: " << edge.weight << endl;
    }
    return 0;
}
```

## Test Cases
```
Input:
V = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
Output:
Minimum Spanning Tree:
Edge: 0 - 3, Weight: 5
Edge: 2 - 3, Weight: 4
Edge: 0 - 2, Weight: 6
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree by selecting the smallest edge that does not form a cycle.
- The disjoint set data structure is used to keep track of connected components and union operations.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V) due to sorting the edges.