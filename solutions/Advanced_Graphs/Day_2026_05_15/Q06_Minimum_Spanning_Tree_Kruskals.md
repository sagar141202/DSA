# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list or edge list, where each edge is defined by two vertices (u, v) and a weight w. The goal is to find the MST with the minimum total weight.

## Approach
Kruskal's algorithm uses a greedy approach to find the MST by sorting the edges in non-decreasing order of their weights and then selecting the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently detect cycles.

## Complexity
- Time: O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices
- Space: O(V + E), for storing the graph and the disjoint-set data structure

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for an edge
struct Edge {
    int u, v, weight;
};

// Define the structure for a disjoint-set
struct DisjointSet {
    vector<int> parent, rank;
    DisjointSet(int V) : parent(V), rank(V, 0) {
        for (int i = 0; i < V; i++) {
            parent[i] = i;
        }
    }

    // Find the root of a vertex
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // Union two vertices
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

// Kruskal's algorithm to find the MST
vector<Edge> kruskal(vector<Edge>& edges, int V) {
    // Sort the edges in non-decreasing order of their weights
    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.weight < b.weight;
    });

    // Initialize the disjoint-set data structure
    DisjointSet ds(V);

    // Initialize the result vector
    vector<Edge> mst;

    // Iterate over the sorted edges
    for (const Edge& edge : edges) {
        // Check if the edge does not form a cycle
        if (ds.find(edge.u) != ds.find(edge.v)) {
            // Add the edge to the MST
            mst.push_back(edge);
            // Union the vertices
            ds.unionSet(edge.u, edge.v);
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

    // Print the MST edges
    for (const Edge& edge : mst) {
        cout << "Edge (" << edge.u << ", " << edge.v << ") with weight " << edge.weight << endl;
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
Edge (0, 3) with weight 5
Edge (2, 3) with weight 4
Edge (0, 2) with weight 6
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph by selecting the smallest edge that does not form a cycle.
- The algorithm uses a disjoint-set data structure to efficiently detect cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.