# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given an undirected, connected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as a list of edges, where each edge is a tuple of (u, v, w) representing an edge between vertices u and v with weight w. The goal is to find the MST and calculate its total weight.

## Approach
Kruskal's algorithm uses a greedy approach to find the MST by sorting the edges by weight and then selecting the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

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
        parent.resize(n);
        rank.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
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

// Kruskal's algorithm to find the MST
int kruskal(vector<Edge>& edges, int V) {
    int mstWeight = 0;
    DisjointSet ds(V);
    sort(edges.begin(), edges.end(), compareEdges);

    for (const auto& edge : edges) {
        int u = edge.u;
        int v = edge.v;
        int w = edge.w;

        if (ds.find(u) != ds.find(v)) {
            ds.unionSet(u, v);
            mstWeight += w;
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
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph by selecting the smallest edge that does not form a cycle.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.