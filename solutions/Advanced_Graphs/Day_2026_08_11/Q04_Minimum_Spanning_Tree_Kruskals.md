# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list or edge list, where each edge is a tuple of (u, v, w) representing the weight w of the edge between vertices u and v. The goal is to find the MST with the minimum total weight.

## Approach
Kruskal's algorithm uses a greedy approach to find the MST by sorting all edges in non-decreasing order of their weights and then selecting the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm utilizes a disjoint-set data structure to efficiently check for cycles.

## Complexity
- Time: O(E log E) or O(E log V)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
    int u, v, w;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

int kruskal(vector<Edge>& edges, int V) {
    sort(edges.begin(), edges.end());
    DisjointSet ds(V);
    int totalWeight = 0;
    for (const auto& edge : edges) {
        if (ds.find(edge.u) != ds.find(edge.v)) {
            ds.unionSet(edge.u, edge.v);
            totalWeight += edge.w;
        }
    }
    return totalWeight;
}

int main() {
    int V = 4;
    vector<Edge> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    int minWeight = kruskal(edges, V);
    cout << "Minimum Spanning Tree weight: " << minWeight << endl;
    return 0;
}
```

## Test Cases
```
Input: 
V = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
Output: 
Minimum Spanning Tree weight: 19
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm used to find the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles and select the smallest edge that does not form a cycle.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.