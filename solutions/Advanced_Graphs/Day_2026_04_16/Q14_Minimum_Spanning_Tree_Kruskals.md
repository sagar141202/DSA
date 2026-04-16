# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The MST is a subgraph that is a tree and includes all the vertices of the original graph, with the minimum possible total edge weight. The graph is represented as an adjacency list or edge list, where each edge is a tuple of (u, v, w) representing an edge between vertices u and v with weight w.

## Approach
Kruskal's algorithm works by sorting all the edges in non-decreasing order of their weights and then selecting the smallest edge that does not form a cycle. This process is repeated until V-1 edges are selected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

## Complexity
- Time: O(E log E) or O(E log V)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for an edge
struct Edge {
    int u, v, w;
};

// Define a custom comparator for sorting edges
bool compareEdges(const Edge& a, const Edge& b) {
    return a.w < b.w;
}

// Define the structure for a disjoint-set
class DisjointSet {
public:
    vector<int> parent, rank;

    // Initialize the disjoint-set
    DisjointSet(int n) {
        parent.resize(n);
        rank.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
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
    // Sort the edges in non-decreasing order of their weights
    sort(edges.begin(), edges.end(), compareEdges);

    // Initialize the disjoint-set
    DisjointSet dsu(V);

    // Initialize the Minimum Spanning Tree
    vector<Edge> mst;

    // Iterate over the sorted edges and select the smallest edge that does not form a cycle
    for (const Edge& edge : edges) {
        if (dsu.find(edge.u) != dsu.find(edge.v)) {
            mst.push_back(edge);
            dsu.unionSets(edge.u, edge.v);
        }
    }

    return mst;
}

int main() {
    int V = 4;
    vector<Edge> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};

    vector<Edge> mst = kruskal(edges, V);

    cout << "Minimum Spanning Tree:" << endl;
    for (const Edge& edge : mst) {
        cout << "Edge: (" << edge.u << ", " << edge.v << "), Weight: " << edge.w << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: V = 4, edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
Output: Minimum Spanning Tree:
Edge: (0, 3), Weight: 5
Edge: (2, 3), Weight: 4
Edge: (0, 2), Weight: 6
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that works by selecting the smallest edge that does not form a cycle.
- The disjoint-set data structure is used to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.