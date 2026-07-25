# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The graph is represented as an adjacency list or edge list. The MST is a subgraph that connects all vertices with the minimum total edge weight. The input graph may contain multiple edges between the same pair of vertices, and the graph may contain self-loops. The algorithm should handle these cases correctly.

## Approach
Kruskal's algorithm uses a greedy approach to find the MST by selecting the smallest edge that does not form a cycle. It utilizes a disjoint-set data structure to efficiently check for cycles. The algorithm sorts all edges by weight and iterates over them, adding each edge to the MST if it does not form a cycle.

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

int kruskal(vector<vector<int>>& edges, int V) {
    sort(edges.begin(), edges.end(), [](vector<int>& a, vector<int>& b) {
        return a[2] < b[2];
    });
    DisjointSet ds(V);
    int mstWeight = 0;
    for (auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        int weight = edge[2];
        if (ds.find(u) != ds.find(v)) {
            ds.unionSet(u, v);
            mstWeight += weight;
        }
    }
    return mstWeight;
}

int main() {
    int V = 4;
    vector<vector<int>> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    cout << "MST Weight: " << kruskal(edges, V) << endl;
    return 0;
}
```

## Test Cases
```
Input: V = 4, edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
Output: MST Weight: 19
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The disjoint-set data structure is used to efficiently check for cycles in the graph.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.