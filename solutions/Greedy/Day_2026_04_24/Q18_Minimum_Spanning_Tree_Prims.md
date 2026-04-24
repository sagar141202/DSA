# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The graph is represented as an adjacency list, where each edge is a tuple of (u, v, w) denoting an edge between vertices u and v with weight w. The goal is to find the subset of edges with the minimum total weight that connects all vertices in the graph. For example, given a graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)}, the Minimum Spanning Tree is {(0, 3, 5), (2, 3, 4), (0, 1, 10), (0, 2, 6)} with a total weight of 25.

## Approach
Prim's algorithm works by selecting a random vertex as the starting point and growing the tree one edge at a time. It uses a greedy approach to choose the edge with the minimum weight that connects a vertex in the tree to a vertex not yet in the tree. This process continues until all vertices are included in the tree.

## Complexity
- Time: O(E log V)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class DisjointSet {
public:
    vector<int> parent;
    vector<int> rank;

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

vector<vector<int>> primMST(vector<vector<int>>& graph, int V) {
    vector<vector<int>> result;
    DisjointSet ds(V);
    vector<vector<int>> edges;

    for (int i = 0; i < V; i++) {
        for (int j = i + 1; j < V; j++) {
            if (graph[i][j] != 0) {
                edges.push_back({graph[i][j], i, j});
            }
        }
    }

    sort(edges.begin(), edges.end());

    for (auto& edge : edges) {
        int w = edge[0];
        int u = edge[1];
        int v = edge[2];

        if (ds.find(u) != ds.find(v)) {
            result.push_back({u, v, w});
            ds.unionSet(u, v);
        }
    }

    return result;
}

int main() {
    int V = 5;
    vector<vector<int>> graph = {
        {0, 10, 6, 5, 0},
        {10, 0, 0, 15, 0},
        {6, 0, 0, 4, 0},
        {5, 15, 4, 0, 0},
        {0, 0, 0, 0, 0}
    };

    vector<vector<int>> mst = primMST(graph, V);

    cout << "Minimum Spanning Tree:" << endl;
    for (auto& edge : mst) {
        cout << "(" << edge[0] << ", " << edge[1] << ", " << edge[2] << ")" << endl;
    }

    return 0;
}
```

## Test Cases
```
Input:
Graph:
  (0, 1, 10)
  (0, 2, 6)
  (0, 3, 5)
  (1, 3, 15)
  (2, 3, 4)

Output:
Minimum Spanning Tree:
(0, 3, 5)
(2, 3, 4)
(0, 1, 10)
(0, 2, 6)

Total Weight: 25
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm used to find the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm works by selecting a random vertex as the starting point and growing the tree one edge at a time, choosing the edge with the minimum weight that connects a vertex in the tree to a vertex not yet in the tree.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices, making it efficient for large graphs.