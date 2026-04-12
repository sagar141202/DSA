# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) of the graph using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list or edge list, where each edge is a tuple of (u, v, w) representing the vertices u and v connected by an edge with weight w.

## Approach
Kruskal's algorithm works by sorting all edges in non-decreasing order of their weights and then selecting the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

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

int main() {
    int V, E;
    cin >> V >> E;
    vector<tuple<int, int, int>> edges;
    for (int i = 0; i < E; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back({u, v, w});
    }
    sort(edges.begin(), edges.end(), [](tuple<int, int, int> a, tuple<int, int, int> b) {
        return get<2>(a) < get<2>(b);
    });
    DisjointSet ds(V);
    int mstWeight = 0;
    vector<tuple<int, int, int>> mstEdges;
    for (auto& edge : edges) {
        int u, v, w;
        tie(u, v, w) = edge;
        if (ds.find(u) != ds.find(v)) {
            ds.unionSets(u, v);
            mstWeight += w;
            mstEdges.push_back(edge);
        }
    }
    cout << "Minimum Spanning Tree Weight: " << mstWeight << endl;
    for (auto& edge : mstEdges) {
        int u, v, w;
        tie(u, v, w) = edge;
        cout << "Edge: (" << u << ", " << v << ", " << w << ")" << endl;
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
Minimum Spanning Tree Weight: 19
Edge: (0, 3, 5)
Edge: (2, 3, 4)
Edge: (0, 1, 10)
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph by selecting the smallest edge that does not form a cycle.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.