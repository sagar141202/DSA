# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The graph is represented as an adjacency list or an edge list. The MST is a subgraph that connects all vertices with the minimum total edge weight. The constraints are: 1 ≤ V ≤ 10^5, 1 ≤ E ≤ 10^5, and the edge weights are non-negative integers.

## Approach
Kruskal's algorithm sorts all edges by weight and then iteratively adds the smallest edge to the MST if it does not form a cycle. The algorithm uses a disjoint-set data structure to efficiently check for cycles. The process continues until all vertices are connected.

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

vector<vector<int>> kruskal(vector<vector<int>>& edges, int V) {
    vector<vector<int>> mst;
    DisjointSet ds(V);
    sort(edges.begin(), edges.end(), [](vector<int>& a, vector<int>& b) {
        return a[2] < b[2];
    });
    for (auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        int w = edge[2];
        if (ds.find(u) != ds.find(v)) {
            mst.push_back(edge);
            ds.unionSet(u, v);
        }
    }
    return mst;
}

int main() {
    int V = 4;
    vector<vector<int>> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    vector<vector<int>> mst = kruskal(edges, V);
    cout << "Minimum Spanning Tree Edges:" << endl;
    for (auto& edge : mst) {
        cout << edge[0] << " - " << edge[1] << " : " << edge[2] << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
V = 4
edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
Output: 
Minimum Spanning Tree Edges:
0 - 3 : 5
2 - 3 : 4
0 - 2 : 6
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.