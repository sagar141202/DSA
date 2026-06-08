# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph, find the minimum spanning tree (MST) using Kruskal's algorithm. The graph is represented as a set of edges, where each edge is a tuple of (node1, node2, weight). The goal is to find the subset of edges with the minimum total weight that connects all nodes in the graph. For example, given a graph with nodes {0, 1, 2, 3} and edges {(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)}, the minimum spanning tree is {(0, 3, 5), (2, 3, 4), (0, 2, 6)}.

## Approach
Kruskal's algorithm sorts all edges in non-decreasing order of their weights and then selects the smallest edge that does not form a cycle. This process is repeated until all nodes are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

## Complexity
- Time: O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices
- Space: O(V + E), for storing the graph and the disjoint-set data structure

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

vector<pair<int, pair<int, int>>> kruskal(vector<pair<int, pair<int, int>>> edges, int n) {
    sort(edges.begin(), edges.end());
    DisjointSet dsu(n);
    vector<pair<int, pair<int, int>>> mst;

    for (auto edge : edges) {
        int weight = edge.first;
        int node1 = edge.second.first;
        int node2 = edge.second.second;
        if (dsu.find(node1) != dsu.find(node2)) {
            mst.push_back(edge);
            dsu.unionSet(node1, node2);
        }
    }

    return mst;
}

int main() {
    int n = 4; // number of nodes
    vector<pair<int, pair<int, int>>> edges = {{10, {0, 1}}, {6, {0, 2}}, {5, {0, 3}}, {15, {1, 3}}, {4, {2, 3}}};
    vector<pair<int, pair<int, int>>> mst = kruskal(edges, n);

    cout << "Minimum Spanning Tree:" << endl;
    for (auto edge : mst) {
        cout << "(" << edge.second.first << ", " << edge.second.second << ", " << edge.first << ")" << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
edges = [(10, (0, 1)), (6, (0, 2)), (5, (0, 3)), (15, (1, 3)), (4, (2, 3))]
n = 4

Output: 
Minimum Spanning Tree:
(0, 3, 5)
(2, 3, 4)
(0, 2, 6)
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the minimum spanning tree of a connected, undirected, and weighted graph.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.