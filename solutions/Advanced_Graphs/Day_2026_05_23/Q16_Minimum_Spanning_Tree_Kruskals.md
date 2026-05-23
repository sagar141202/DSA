# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given an undirected and connected graph with non-negative edge weights, find the Minimum Spanning Tree (MST) of the graph using Kruskal's algorithm. The graph has 'n' vertices and 'm' edges. Each edge is represented as a tuple of (weight, vertex1, vertex2). The goal is to find the subset of edges that connect all vertices with the minimum total weight.

## Approach
Kruskal's algorithm uses a greedy approach to find the MST by sorting all edges in increasing order of their weights and then selecting the smallest edge that does not form a cycle. This process continues until all vertices are connected. The algorithm utilizes a disjoint set data structure to efficiently check for cycles.

## Complexity
- Time: O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices
- Space: O(V + E), for storing the graph and the disjoint set data structure

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

vector<vector<int>> kruskal(int n, vector<vector<int>>& edges) {
    sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });

    DisjointSet dsu(n);
    vector<vector<int>> mst;

    for (const auto& edge : edges) {
        int weight = edge[0];
        int vertex1 = edge[1];
        int vertex2 = edge[2];

        if (dsu.find(vertex1) != dsu.find(vertex2)) {
            mst.push_back(edge);
            dsu.unionSet(vertex1, vertex2);
        }
    }

    return mst;
}

int main() {
    int n = 4;
    vector<vector<int>> edges = {{1, 0, 1}, {2, 0, 2}, {3, 1, 2}, {4, 2, 3}};

    vector<vector<int>> mst = kruskal(n, edges);

    for (const auto& edge : mst) {
        cout << "Weight: " << edge[0] << ", Vertex1: " << edge[1] << ", Vertex2: " << edge[2] << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
n = 4
edges = [[1, 0, 1], [2, 0, 2], [3, 1, 2], [4, 2, 3]]
Output: 
Weight: 1, Vertex1: 0, Vertex2: 1
Weight: 2, Vertex1: 0, Vertex2: 2
Weight: 3, Vertex1: 1, Vertex2: 2
```

## Key Takeaways
- Kruskal's algorithm is suitable for finding the MST in a graph with a large number of vertices and edges.
- The algorithm has a time complexity of O(E log E) or O(E log V), making it efficient for sparse graphs.
- The disjoint set data structure is used to efficiently check for cycles in the graph.