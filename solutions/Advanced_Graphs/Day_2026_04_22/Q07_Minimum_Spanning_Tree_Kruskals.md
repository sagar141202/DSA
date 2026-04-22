# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) of the graph using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list or edge list, where each edge is a tuple of (u, v, w) denoting an edge between vertices u and v with weight w.

## Approach
Kruskal's algorithm sorts all edges by weight, then iteratively adds the smallest edge to the MST if it doesn't form a cycle. This process continues until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

## Complexity
- Time: O(E log E) or O(E log V) due to sorting the edges
- Space: O(V + E) for storing the graph and disjoint-set data structure

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for an edge
struct Edge {
    int u, v, weight;
};

// Compare function for sorting edges by weight
bool compareEdges(const Edge& a, const Edge& b) {
    return a.weight < b.weight;
}

// Disjoint-set data structure
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

// Kruskal's algorithm to find the Minimum Spanning Tree
int kruskal(vector<Edge>& edges, int V) {
    sort(edges.begin(), edges.end(), compareEdges);
    DisjointSet ds(V);
    int mstWeight = 0;

    for (const Edge& edge : edges) {
        if (ds.find(edge.u) != ds.find(edge.v)) {
            ds.unionSets(edge.u, edge.v);
            mstWeight += edge.weight;
        }
    }

    return mstWeight;
}

int main() {
    int V = 4; // Number of vertices
    vector<Edge> edges = {
        {0, 1, 10},
        {0, 2, 6},
        {0, 3, 5},
        {1, 3, 15},
        {2, 3, 4}
    };

    int mstWeight = kruskal(edges, V);
    cout << "Minimum Spanning Tree Weight: " << mstWeight << endl;
    return 0;
}
```

## Test Cases
```
Input: 
V = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
Output: 
Minimum Spanning Tree Weight: 19
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph.
- It uses a disjoint-set data structure to efficiently check for cycles.
- The algorithm has a time complexity of O(E log E) or O(E log V) due to sorting the edges.