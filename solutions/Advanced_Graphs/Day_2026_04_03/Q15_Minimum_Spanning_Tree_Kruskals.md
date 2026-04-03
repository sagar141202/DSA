# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph, find the minimum spanning tree (MST) using Kruskal's algorithm. The graph is represented as an adjacency list or adjacency matrix, and the MST is a subgraph that connects all vertices with the minimum total edge weight. The graph has 'n' vertices and 'm' edges, and each edge has a weight 'w'. The goal is to find the MST with the minimum total weight.

## Approach
Kruskal's algorithm uses a greedy approach to find the MST by sorting all edges in non-decreasing order of their weights and then selecting the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

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

// Compare function to sort edges in non-decreasing order of their weights
bool compareEdges(const Edge& a, const Edge& b) {
    return a.weight < b.weight;
}

// Disjoint-set data structure
class DisjointSet {
public:
    vector<int> parent, rank;

    DisjointSet(int n) {
        parent.resize(n);
        rank.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }

    // Find the parent of a node
    int find(int node) {
        if (parent[node] != node) {
            parent[node] = find(parent[node]);
        }
        return parent[node];
    }

    // Union of two nodes
    void unionNodes(int u, int v) {
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

// Function to find the minimum spanning tree using Kruskal's algorithm
vector<Edge> kruskalMST(vector<Edge>& edges, int n) {
    sort(edges.begin(), edges.end(), compareEdges);
    DisjointSet ds(n);
    vector<Edge> mst;

    for (const auto& edge : edges) {
        if (ds.find(edge.src) != ds.find(edge.dest)) {
            mst.push_back(edge);
            ds.unionNodes(edge.src, edge.dest);
        }
    }

    return mst;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].src >> edges[i].dest >> edges[i].weight;
    }

    vector<Edge> mst = kruskalMST(edges, n);

    cout << "Minimum Spanning Tree Edges:\n";
    for (const auto& edge : mst) {
        cout << edge.src << " - " << edge.dest << " : " << edge.weight << "\n";
    }

    return 0;
}
```

## Test Cases
```
Input:
4 5
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4

Output:
Minimum Spanning Tree Edges:
2 3 : 4
0 3 : 5
0 1 : 10
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm used to find the minimum spanning tree of a connected, undirected, and weighted graph.
- The algorithm sorts all edges in non-decreasing order of their weights and then selects the smallest edge that does not form a cycle.
- A disjoint-set data structure is used to efficiently check for cycles and union nodes.