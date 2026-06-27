# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list or edge list, where each edge is a tuple of (u, v, weight). The goal is to find the MST with the minimum total weight.

## Approach
Kruskal's algorithm uses a greedy approach, sorting all edges by weight and selecting the smallest edge that does not form a cycle. This process continues until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

## Complexity
- Time: O(E log E) or O(E log V) due to sorting the edges
- Space: O(V + E) for storing the graph and disjoint-set data structure

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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

struct Edge {
    int u, v, weight;
    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

vector<Edge> kruskal(vector<Edge>& edges, int V) {
    sort(edges.begin(), edges.end());
    DisjointSet ds(V);
    vector<Edge> mst;
    for (Edge& edge : edges) {
        if (ds.find(edge.u) != ds.find(edge.v)) {
            ds.unionSet(edge.u, edge.v);
            mst.push_back(edge);
        }
    }
    return mst;
}

int main() {
    int V = 4;
    vector<Edge> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    vector<Edge> mst = kruskal(edges, V);
    int totalWeight = 0;
    for (Edge& edge : mst) {
        totalWeight += edge.weight;
        cout << "Edge: (" << edge.u << ", " << edge.v << "), Weight: " << edge.weight << endl;
    }
    cout << "Total Weight: " << totalWeight << endl;
    return 0;
}
```

## Test Cases
```
Input: 
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
V = 4
Output: 
Edge: (0, 3), Weight: 5
Edge: (2, 3), Weight: 4
Edge: (0, 2), Weight: 6
Total Weight: 15
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V) due to sorting the edges.