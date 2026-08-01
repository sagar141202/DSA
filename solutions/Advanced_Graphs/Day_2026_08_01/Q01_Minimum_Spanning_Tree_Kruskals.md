# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The graph is represented as an adjacency list or edge list, where each edge is associated with a weight. The goal is to find the subset of edges with the minimum total weight that connects all vertices in the graph. For example, consider a graph with vertices {0, 1, 2, 3} and edges {(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)}. The minimum spanning tree should have edges {(0, 3, 5), (2, 3, 4), (0, 1, 10)}.

## Approach
Kruskal's algorithm sorts the edges in non-decreasing order of their weights and then selects the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

## Complexity
- Time: O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices
- Space: O(V + E), for storing the graph and the disjoint-set data structure

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for an edge
struct Edge {
    int src, dest, weight;
};

// Define the structure for a disjoint-set
struct DisjointSet {
    vector<int> parent, rank;
    DisjointSet(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    // Find the root of a set
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // Union two sets
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

// Compare edges based on their weights
bool compareEdges(const Edge& a, const Edge& b) {
    return a.weight < b.weight;
}

// Kruskal's algorithm to find the minimum spanning tree
vector<Edge> kruskal(vector<Edge>& edges, int n) {
    sort(edges.begin(), edges.end(), compareEdges);
    DisjointSet ds(n);
    vector<Edge> mst;
    for (const auto& edge : edges) {
        if (ds.find(edge.src) != ds.find(edge.dest)) {
            mst.push_back(edge);
            ds.unionSet(edge.src, edge.dest);
        }
    }
    return mst;
}

int main() {
    int n = 4;  // Number of vertices
    vector<Edge> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    vector<Edge> mst = kruskal(edges, n);
    cout << "Minimum Spanning Tree:" << endl;
    for (const auto& edge : mst) {
        cout << "(" << edge.src << ", " << edge.dest << ", " << edge.weight << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
Vertices: 4
Edges: {(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)}
Output: 
Minimum Spanning Tree:
(0, 3, 5)
(2, 3, 4)
(0, 1, 10)
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the minimum spanning tree of a connected, undirected, and weighted graph.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.