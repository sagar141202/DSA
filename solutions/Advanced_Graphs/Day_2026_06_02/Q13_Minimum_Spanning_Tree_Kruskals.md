# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) of the graph using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list or edge list, where each edge is represented as a tuple (u, v, w) with u and v being the source and destination vertices, and w being the edge weight. The graph may contain multiple edges between the same pair of vertices, and the goal is to find the MST with the minimum total edge weight.

## Approach
Kruskal's algorithm uses a greedy approach to find the MST by selecting the smallest edge that does not form a cycle. The algorithm uses a disjoint-set data structure to keep track of connected components. It sorts the edges by weight and iterates over them, adding each edge to the MST if it does not form a cycle.

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

// Define the structure for a disjoint-set
struct DisjointSet {
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
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

// Kruskal's algorithm to find the Minimum Spanning Tree
vector<Edge> kruskal(vector<Edge>& edges, int V) {
    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.w < b.w;
    });

    DisjointSet ds(V);
    vector<Edge> mst;

    for (const Edge& edge : edges) {
        if (ds.find(edge.u) != ds.find(edge.v)) {
            mst.push_back(edge);
            ds.unionSet(edge.u, edge.v);
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
        cout << edge.u << " - " << edge.v << ": " << edge.w << endl;
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
Minimum Spanning Tree:
0 - 3: 5
2 - 3: 4
0 - 2: 6
```

## Key Takeaways
- Kruskal's algorithm uses a greedy approach to find the Minimum Spanning Tree.
- The disjoint-set data structure is used to keep track of connected components.
- The algorithm has a time complexity of O(E log E) or O(E log V) and a space complexity of O(V + E).