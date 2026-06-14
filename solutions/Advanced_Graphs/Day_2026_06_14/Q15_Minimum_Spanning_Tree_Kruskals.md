# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the minimum spanning tree (MST) of the graph using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an edge list, where each edge is a tuple of (u, v, w) denoting an edge between vertices u and v with weight w.

## Approach
Kruskal's algorithm works by sorting all edges in non-decreasing order of their weights and then selecting the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

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

// Compare function for sorting edges
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

// Kruskal's algorithm
int kruskal(vector<Edge>& edges, int V) {
    sort(edges.begin(), edges.end(), compareEdges);
    DisjointSet ds(V);
    int mstWeight = 0;
    int edgeCount = 0;

    for (const auto& edge : edges) {
        if (ds.find(edge.u) != ds.find(edge.v)) {
            ds.unionSet(edge.u, edge.v);
            mstWeight += edge.w;
            edgeCount++;
        }

        if (edgeCount == V - 1) {
            break;
        }
    }

    return mstWeight;
}

int main() {
    int V, E;
    cin >> V >> E;

    vector<Edge> edges(E);
    for (int i = 0; i < E; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    int mstWeight = kruskal(edges, V);
    cout << "Minimum Spanning Tree Weight: " << mstWeight << endl;

    return 0;
}
```

## Test Cases
```
Input: 
5 7
1 2 2
1 3 3
2 3 1
2 4 1
2 5 4
3 4 5
4 5 3
Output: 
Minimum Spanning Tree Weight: 8
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the minimum spanning tree of a graph by selecting the smallest edge that does not form a cycle.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.