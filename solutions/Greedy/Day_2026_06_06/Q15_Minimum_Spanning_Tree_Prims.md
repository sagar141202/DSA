# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The graph is represented as an adjacency list, where each edge is a tuple of (u, v, weight). The MST is a subgraph that connects all vertices with the minimum total edge weight. The constraints are: 1 ≤ V ≤ 10^5, 1 ≤ E ≤ 10^5, and 1 ≤ weight ≤ 10^5.

## Approach
Prim's algorithm is a greedy algorithm that works by selecting the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST. The algorithm starts with an arbitrary vertex and grows the MST by adding edges one by one. The key intuition is to always choose the minimum-weight edge that does not form a cycle.

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

int primMST(vector<vector<int>>& graph, int V) {
    vector<vector<int>> edges;
    for (int i = 0; i < V; i++) {
        for (int j = i + 1; j < V; j++) {
            if (graph[i][j] != 0) {
                edges.push_back({graph[i][j], i, j});
            }
        }
    }
    sort(edges.begin(), edges.end());

    DisjointSet ds(V);
    int mstWeight = 0;
    vector<vector<int>> mstEdges;

    for (auto& edge : edges) {
        int weight = edge[0];
        int u = edge[1];
        int v = edge[2];
        if (ds.find(u) != ds.find(v)) {
            mstWeight += weight;
            mstEdges.push_back({u, v, weight});
            ds.unionSet(u, v);
        }
    }

    cout << "MST Edges: " << endl;
    for (auto& edge : mstEdges) {
        cout << edge[0] << " - " << edge[1] << " : " << edge[2] << endl;
    }

    return mstWeight;
}

int main() {
    int V = 5;
    vector<vector<int>> graph = {
        {0, 2, 0, 6, 0},
        {2, 0, 3, 8, 5},
        {0, 3, 0, 0, 7},
        {6, 8, 0, 0, 9},
        {0, 5, 7, 9, 0}
    };

    int mstWeight = primMST(graph, V);
    cout << "MST Weight: " << mstWeight << endl;

    return 0;
}
```

## Test Cases
```
Input: 
Graph:
0 2 0 6 0
2 0 3 8 5
0 3 0 0 7
6 8 0 0 9
0 5 7 9 0

Output: 
MST Edges: 
0 - 1 : 2
1 - 2 : 3
1 - 4 : 5
0 - 3 : 6
MST Weight: 16
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph.
- The algorithm uses a disjoint set data structure to keep track of connected components.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.