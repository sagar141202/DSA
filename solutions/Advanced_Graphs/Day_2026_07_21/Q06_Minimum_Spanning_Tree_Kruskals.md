# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list or edge list, where each edge is a tuple of (u, v, w) representing the source vertex u, destination vertex v, and edge weight w. The goal is to find the MST with the minimum total edge weight.

## Approach
Kruskal's algorithm uses a greedy approach to find the MST by selecting the smallest edge that does not form a cycle. It uses a disjoint-set data structure to keep track of connected components. The algorithm sorts the edges by weight and iterates over them, adding each edge to the MST if it does not form a cycle.

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
    DisjointSet(int n) {
        parent.resize(n + 1);
        rank.resize(n + 1, 0);
        for (int i = 1; i <= n; i++) {
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
int kruskal(vector<Edge>& edges, int n) {
    sort(edges.begin(), edges.end(), [](Edge& a, Edge& b) {
        return a.w < b.w;
    });

    DisjointSet ds(n);
    int mstWeight = 0;
    for (Edge& edge : edges) {
        if (ds.find(edge.u) != ds.find(edge.v)) {
            ds.unionSet(edge.u, edge.v);
            mstWeight += edge.w;
        }
    }
    return mstWeight;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }
    int mstWeight = kruskal(edges, n);
    cout << "Minimum Spanning Tree Weight: " << mstWeight << endl;
    return 0;
}
```

## Test Cases
```
Input:
4 5
1 2 10
1 3 6
2 3 4
2 4 8
3 4 5
Output:
Minimum Spanning Tree Weight: 19
```

## Key Takeaways
- Kruskal's algorithm uses a greedy approach to find the Minimum Spanning Tree.
- The algorithm uses a disjoint-set data structure to keep track of connected components.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.