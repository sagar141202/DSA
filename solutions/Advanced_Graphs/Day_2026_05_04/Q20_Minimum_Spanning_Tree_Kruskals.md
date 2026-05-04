# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) of the graph using Kruskal's algorithm. The MST is a subgraph that connects all the vertices together while minimizing the total edge weight. The graph is represented as a list of edges, where each edge is a tuple of (u, v, w) representing an edge between vertices u and v with weight w.

## Approach
Kruskal's algorithm works by sorting all the edges in non-decreasing order of their weights and then selecting the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

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

    int find(int node) {
        if (node == parent[node]) {
            return node;
        }
        return parent[node] = find(parent[node]);
    }

    void unionByRank(int u, int v) {
        int op1, op2;
        op1 = find(u);
        op2 = find(v);
        if (op1 == op2) {
            return;
        }
        if (rank[op1] < rank[op2]) {
            parent[op1] = op2;
        } else if (rank[op2] < rank[op1]) {
            parent[op2] = op1;
        } else {
            parent[op1] = op2;
            rank[op2]++;
        }
    }
};

int spanningTree(int V, vector<vector<int>>& edges) {
    sort(edges.begin(), edges.end(), [](vector<int>& a, vector<int>& b) {
        return a[2] < b[2];
    });
    DisjointSet ds(V);
    int cost = 0;
    for (auto& edge : edges) {
        int u = edge[0], v = edge[1], weight = edge[2];
        if (ds.find(u) != ds.find(v)) {
            ds.unionByRank(u, v);
            cost += weight;
        }
    }
    return cost;
}

int main() {
    int V = 4;
    vector<vector<int>> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    cout << "Minimum Spanning Tree cost: " << spanningTree(V, edges);
    return 0;
}
```

## Test Cases
```
Input: V = 4, edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
Output: Minimum Spanning Tree cost: 19
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.