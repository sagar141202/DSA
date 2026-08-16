# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a weighted, undirected, and connected graph with V vertices and E edges, the task is to find the Minimum Spanning Tree (MST) of the graph using Kruskal's algorithm. The graph is represented as an adjacency list or an edge list. The MST is a subgraph that connects all vertices together while minimizing the total edge weight. The graph may contain multiple edges between the same pair of vertices, and the goal is to find the MST with the minimum total weight.

## Approach
Kruskal's algorithm sorts all edges in non-decreasing order of their weights and then selects the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently detect cycles.

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

vector<vector<int>> kruskal(int V, vector<vector<int>>& edges) {
    sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[2] < b[2];
    });
    DisjointSet ds(V);
    vector<vector<int>> mst;
    for (const auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        int weight = edge[2];
        if (ds.find(u) != ds.find(v)) {
            ds.unionSets(u, v);
            mst.push_back({u, v, weight});
        }
    }
    return mst;
}

int main() {
    int V = 4;
    vector<vector<int>> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    vector<vector<int>> mst = kruskal(V, edges);
    for (const auto& edge : mst) {
        cout << "Edge: " << edge[0] << " - " << edge[1] << ", Weight: " << edge[2] << endl;
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
Edge: 0 - 3, Weight: 5
Edge: 2 - 3, Weight: 4
Edge: 0 - 2, Weight: 6
```

## Key Takeaways
- Kruskal's algorithm is used to find the Minimum Spanning Tree of a weighted, undirected, and connected graph.
- The algorithm uses a disjoint-set data structure to efficiently detect cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.