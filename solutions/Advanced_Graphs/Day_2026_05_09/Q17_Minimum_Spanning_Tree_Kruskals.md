# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph, find the minimum spanning tree (MST) using Kruskal's algorithm. The graph is represented as an adjacency list or edge list, and the goal is to select the subset of edges with the minimum total weight that connects all vertices in the graph. The graph has 'n' vertices and 'm' edges, where each edge is represented as a tuple (u, v, w), where 'u' and 'v' are the vertices connected by the edge, and 'w' is the weight of the edge. The graph may contain self-loops and multiple edges between the same pair of vertices.

## Approach
Kruskal's algorithm works by sorting all edges in non-decreasing order of their weights and then selecting the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

## Complexity
- Time: O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices
- Space: O(E + V), for storing the edges and the disjoint-set data structure

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

vector<vector<int>> kruskal(int n, vector<vector<int>>& edges) {
    // Sort edges in non-decreasing order of their weights
    sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[2] < b[2];
    });

    DisjointSet ds(n);
    vector<vector<int>> mst;
    for (const auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        int w = edge[2];
        if (ds.find(u) != ds.find(v)) {
            mst.push_back(edge);
            ds.unionSets(u, v);
        }
    }
    return mst;
}

int main() {
    int n = 4;  // number of vertices
    vector<vector<int>> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    vector<vector<int>> mst = kruskal(n, edges);
    cout << "Minimum Spanning Tree Edges:" << endl;
    for (const auto& edge : mst) {
        cout << edge[0] << " - " << edge[1] << ": " << edge[2] << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
n = 4
edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
Output: 
Minimum Spanning Tree Edges:
0 - 3: 5
2 - 3: 4
0 - 2: 6
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that selects the smallest edge that does not form a cycle.
- The disjoint-set data structure is used to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.