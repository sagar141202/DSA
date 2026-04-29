# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as a list of edges, where each edge is a tuple of (u, v, w) representing an edge between vertices u and v with weight w. The goal is to find the minimum spanning tree and calculate its total weight.

## Approach
Kruskal's algorithm sorts all edges in non-decreasing order of their weights and then selects the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

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

// Compare function to sort edges by weight
bool compareEdges(const Edge& a, const Edge& b) {
    return a.w < b.w;
}

// Disjoint-set data structure
class DisjointSet {
public:
    vector<int> parent, rank;

    DisjointSet(int n) {
        parent.resize(n + 1);
        rank.resize(n + 1, 0);
        for (int i = 0; i <= n; i++) {
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

int kruskal(vector<Edge>& edges, int V) {
    // Sort the edges by weight
    sort(edges.begin(), edges.end(), compareEdges);

    // Initialize the disjoint-set data structure
    DisjointSet ds(V);

    int mstWeight = 0;
    vector<Edge> mstEdges;

    // Iterate through the sorted edges and select the smallest edge that does not form a cycle
    for (const Edge& edge : edges) {
        if (ds.find(edge.u) != ds.find(edge.v)) {
            ds.unionSets(edge.u, edge.v);
            mstWeight += edge.w;
            mstEdges.push_back(edge);
        }
    }

    return mstWeight;
}

int main() {
    int V = 4;
    vector<Edge> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};

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
- Kruskal's algorithm is a greedy algorithm that finds the minimum spanning tree of a graph by selecting the smallest edge that does not form a cycle.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.