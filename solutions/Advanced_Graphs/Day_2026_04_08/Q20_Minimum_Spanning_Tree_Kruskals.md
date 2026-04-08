# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, the goal is to find the Minimum Spanning Tree (MST) of the graph. The MST is a subgraph that connects all vertices together while minimizing the total edge weight. The graph is represented as an adjacency list or edge list, where each edge is associated with a weight. The problem constraints are: 1 ≤ V ≤ 10^5, 1 ≤ E ≤ 10^5, and 1 ≤ weight ≤ 10^5. For example, consider a graph with 4 vertices and 5 edges: (0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4). The MST of this graph should have a total weight of 16 (edges: (0, 3, 5), (2, 3, 4), (0, 2, 6)).

## Approach
Kruskal's algorithm uses a disjoint set data structure to keep track of connected components in the graph. It sorts the edges by weight and iterates over them, adding each edge to the MST if it connects two different components. This approach ensures the minimum total weight of the resulting tree. The algorithm runs in nearly linear time with respect to the number of edges.

## Complexity
- Time: O(E log E) or O(E log V)
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

int main() {
    int V, E;
    cin >> V >> E;
    vector<tuple<int, int, int>> edges;
    for (int i = 0; i < E; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back({w, u, v});
    }

    sort(edges.begin(), edges.end());
    DisjointSet dsu(V);
    int mstWeight = 0;
    vector<tuple<int, int, int>> mstEdges;

    for (auto& edge : edges) {
        int w, u, v;
        tie(w, u, v) = edge;
        if (dsu.find(u) != dsu.find(v)) {
            dsu.unionSet(u, v);
            mstWeight += w;
            mstEdges.push_back(edge);
        }
    }

    cout << "MST Weight: " << mstWeight << endl;
    cout << "MST Edges:" << endl;
    for (auto& edge : mstEdges) {
        int w, u, v;
        tie(w, u, v) = edge;
        cout << "(" << u << ", " << v << ", " << w << ")" << endl;
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
MST Weight: 16
MST Edges:
(0, 3, 5)
(2, 3, 4)
(0, 2, 6)
```

## Key Takeaways
- Kruskal's algorithm is suitable for finding the Minimum Spanning Tree in a connected, undirected, and weighted graph.
- The disjoint set data structure is used to efficiently manage connected components during the algorithm's execution.
- The algorithm's time complexity is nearly linear with respect to the number of edges, making it efficient for large graphs.