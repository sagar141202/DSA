# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list or edge list, where each edge is a tuple of (u, v, weight). The vertices are numbered from 0 to V-1.

## Approach
Kruskal's algorithm works by sorting all edges in non-decreasing order of their weights and then selecting the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently detect cycles.

## Complexity
- Time: O(E log E) or O(E log V) due to sorting
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

vector<pair<int, pair<int, int>>> kruskal(vector<pair<int, pair<int, int>>> edges, int V) {
    sort(edges.begin(), edges.end());
    DisjointSet ds(V);
    vector<pair<int, pair<int, int>>> mst;
    for (auto edge : edges) {
        int weight = edge.first;
        int u = edge.second.first;
        int v = edge.second.second;
        if (ds.find(u) != ds.find(v)) {
            ds.unionSet(u, v);
            mst.push_back(edge);
        }
    }
    return mst;
}

int main() {
    int V = 4;
    vector<pair<int, pair<int, int>>> edges = {{1, {0, 1}}, {2, {0, 3}}, {2, {1, 2}}, {3, {1, 3}}, {4, {2, 3}}};
    vector<pair<int, pair<int, int>>> mst = kruskal(edges, V);
    cout << "Minimum Spanning Tree:" << endl;
    for (auto edge : mst) {
        cout << "Edge: (" << edge.second.first << ", " << edge.second.second << "), Weight: " << edge.first << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
V = 4
edges = [(1, (0, 1)), (2, (0, 3)), (2, (1, 2)), (3, (1, 3)), (4, (2, 3))]
Output: 
Minimum Spanning Tree:
Edge: (0, 1), Weight: 1
Edge: (1, 2), Weight: 2
Edge: (0, 3), Weight: 2
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that selects the smallest edge that does not form a cycle.
- The disjoint-set data structure is used to efficiently detect cycles in the graph.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V) due to sorting, where E is the number of edges and V is the number of vertices.