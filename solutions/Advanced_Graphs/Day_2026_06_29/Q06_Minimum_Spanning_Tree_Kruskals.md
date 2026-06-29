# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The graph is represented as a set of edges, where each edge is a tuple of (weight, vertex1, vertex2). The goal is to find the subset of edges that connect all vertices with the minimum total weight. The graph has 'n' vertices and 'm' edges, where 1 <= n <= 10^5 and 1 <= m <= 10^6. The weight of each edge is a positive integer.

## Approach
Kruskal's algorithm uses a greedy approach to find the MST by sorting the edges in non-decreasing order of their weights and then selecting the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

## Complexity
- Time: O(m log m)
- Space: O(n + m)

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

int kruskal(vector<vector<int>>& edges, int n) {
    sort(edges.begin(), edges.end());
    DisjointSet ds(n);
    int totalWeight = 0;
    vector<vector<int>> mst;
    for (auto& edge : edges) {
        int weight = edge[0];
        int vertex1 = edge[1];
        int vertex2 = edge[2];
        if (ds.find(vertex1) != ds.find(vertex2)) {
            ds.unionSet(vertex1, vertex2);
            totalWeight += weight;
            mst.push_back(edge);
        }
    }
    return totalWeight;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> edges(m, vector<int>(3));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }
    int totalWeight = kruskal(edges, n);
    cout << "Minimum Spanning Tree Weight: " << totalWeight << endl;
    return 0;
}
```

## Test Cases
```
Input:
4 5
1 1 2
2 2 3
3 1 3
4 3 4
5 2 4
Output:
Minimum Spanning Tree Weight: 10
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph by selecting the smallest edge that does not form a cycle.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(m log m) due to the sorting of edges, where 'm' is the number of edges in the graph.