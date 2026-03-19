# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) of the graph using Kruskal's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as a list of edges, where each edge is a tuple of (vertex1, vertex2, weight). The algorithm should return the total weight of the MST.

## Approach
Kruskal's algorithm works by sorting the edges in non-decreasing order of their weights, then iteratively adding the smallest edge to the MST if it does not form a cycle. This process continues until all vertices are connected.

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

int kruskal(vector<vector<int>>& edges, int V) {
    sort(edges.begin(), edges.end(), [](vector<int>& a, vector<int>& b) {
        return a[2] < b[2];
    });

    DisjointSet ds(V);
    int totalWeight = 0;

    for (auto& edge : edges) {
        int vertex1 = edge[0];
        int vertex2 = edge[1];
        int weight = edge[2];

        if (ds.find(vertex1) != ds.find(vertex2)) {
            ds.unionSet(vertex1, vertex2);
            totalWeight += weight;
        }
    }

    return totalWeight;
}

int main() {
    int V = 4;
    vector<vector<int>> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};

    int totalWeight = kruskal(edges, V);
    cout << "Total weight of MST: " << totalWeight << endl;

    return 0;
}
```

## Test Cases
```
Input: V = 4, edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
Output: Total weight of MST: 19
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph.
- The algorithm sorts the edges in non-decreasing order of their weights and then iteratively adds the smallest edge to the MST if it does not form a cycle.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.