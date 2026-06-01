# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. The MST is a subset of the edges in the graph that connects all the vertices together while minimizing the total edge cost. The graph is represented as an adjacency list or edge list, where each edge is a tuple of (u, v, weight) representing an edge between vertices u and v with a weight. The goal is to find the MST with the minimum total weight.

## Approach
Kruskal's algorithm uses a greedy approach to find the MST by selecting the smallest edge that does not form a cycle. It uses a disjoint set data structure to keep track of connected components. The algorithm sorts the edges by weight and iterates over them, adding each edge to the MST if it does not form a cycle.

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

vector<vector<int>> kruskal(vector<vector<int>>& edges, int V) {
    vector<vector<int>> mst;
    DisjointSet ds(V);
    sort(edges.begin(), edges.end(), [](vector<int>& a, vector<int>& b) {
        return a[2] < b[2];
    });
    for (auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        int weight = edge[2];
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
    for (auto& edge : mst) {
        cout << edge[0] << " - " << edge[1] << " : " << edge[2] << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
V = 4
Output: 
0 - 3 : 5
2 - 3 : 4
0 - 1 : 10
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph.
- It uses a disjoint set data structure to keep track of connected components.
- The algorithm has a time complexity of O(E log E) or O(E log V) and a space complexity of O(V + E).