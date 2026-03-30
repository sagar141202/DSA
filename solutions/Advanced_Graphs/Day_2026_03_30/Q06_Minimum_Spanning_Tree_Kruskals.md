# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The MST is a subset of the edges in the graph that connects all the vertices together while minimizing the total edge cost. The graph is represented as an adjacency list or an edge list. The edge list is a set of edges, where each edge is represented as a tuple (u, v, w), where u and v are the source and destination vertices, and w is the weight of the edge. The constraints are 1 ≤ V ≤ 10^5 and 1 ≤ E ≤ 10^5.

## Approach
Kruskal's algorithm uses a greedy approach to find the MST. It sorts the edges in non-decreasing order of their weights, then iterates over the sorted edges and adds them to the MST if they do not form a cycle. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

## Complexity
- Time: O(E log E) or O(E log V)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for an edge
struct Edge {
    int src, dest, weight;
};

// Compare function for sorting edges
bool compareEdges(const Edge& a, const Edge& b) {
    return a.weight < b.weight;
}

// Disjoint-set data structure
class DisjointSet {
public:
    vector<int> parent, rank;

    DisjointSet(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int node) {
        if (parent[node] != node) {
            parent[node] = find(parent[node]);
        }
        return parent[node];
    }

    void unionSets(int u, int v) {
        int rootU = find(u);
        int rootV = find(v);

        if (rootU != rootV) {
            if (rank[rootU] < rank[rootV]) {
                parent[rootU] = rootV;
            } else if (rank[rootU] > rank[rootV]) {
                parent[rootV] = rootU;
            } else {
                parent[rootV] = rootU;
                rank[rootU]++;
            }
        }
    }
};

// Kruskal's algorithm
vector<Edge> kruskal(vector<Edge>& edges, int V) {
    // Sort the edges in non-decreasing order of their weights
    sort(edges.begin(), edges.end(), compareEdges);

    // Initialize the disjoint-set data structure
    DisjointSet ds(V);

    // Initialize the result vector
    vector<Edge> result;

    // Iterate over the sorted edges
    for (const Edge& edge : edges) {
        // Check if the edge does not form a cycle
        if (ds.find(edge.src) != ds.find(edge.dest)) {
            // Add the edge to the result
            result.push_back(edge);

            // Union the sets containing the source and destination vertices
            ds.unionSets(edge.src, edge.dest);
        }
    }

    return result;
}

int main() {
    int V = 4;
    vector<Edge> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};

    vector<Edge> mst = kruskal(edges, V);

    cout << "Edges in the Minimum Spanning Tree:" << endl;
    for (const Edge& edge : mst) {
        cout << "Source: " << edge.src << ", Destination: " << edge.dest << ", Weight: " << edge.weight << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
V = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

Output: 
Edges in the Minimum Spanning Tree:
Source: 0, Destination: 3, Weight: 5
Source: 2, Destination: 3, Weight: 4
Source: 0, Destination: 2, Weight: 6
```

## Key Takeaways
- Kruskal's algorithm is used to find the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), and the space complexity is O(V + E).