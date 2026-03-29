# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, the goal is to find the Minimum Spanning Tree (MST) of the graph. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list, where each vertex is associated with a list of its neighboring vertices and the corresponding edge weights. The constraints are: 1 ≤ V ≤ 10^5, 1 ≤ E ≤ 10^5, and 1 ≤ edge weight ≤ 10^5. For example, given a graph with 5 vertices and 7 edges, the MST should have the minimum total edge weight.

## Approach
The algorithm used is Prim's algorithm, a greedy approach that starts with an arbitrary vertex and grows the MST by adding the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST. This process continues until all vertices are included in the MST. The key intuition is to always choose the locally optimal solution, which leads to a globally optimal solution.

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

    int find(int node) {
        if (node == parent[node]) {
            return node;
        }
        return parent[node] = find(parent[node]);
    }

    void unionByRank(int u, int v) {
        int op1 = find(u);
        int op2 = find(v);
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

int primMST(int n, vector<vector<int>>& graph) {
    vector<vector<int>> edges;
    for (int i = 0; i < graph.size(); i++) {
        for (int j = i + 1; j < graph[i].size(); j++) {
            if (graph[i][j] != 0) {
                edges.push_back({graph[i][j], i, j});
            }
        }
    }
    sort(edges.begin(), edges.end());
    DisjointSet ds(n);
    int cost = 0;
    for (auto& edge : edges) {
        int weight = edge[0];
        int u = edge[1];
        int v = edge[2];
        if (ds.find(u) != ds.find(v)) {
            ds.unionByRank(u, v);
            cost += weight;
        }
    }
    return cost;
}

int main() {
    int n = 5;
    vector<vector<int>> graph = {{0, 2, 0, 6, 0},
                                  {2, 0, 3, 8, 5},
                                  {0, 3, 0, 0, 7},
                                  {6, 8, 0, 0, 9},
                                  {0, 5, 7, 9, 0}};
    cout << "Minimum Spanning Tree cost: " << primMST(n, graph) << endl;
    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and 7 edges:
0 --2-- 1
|    / |
|   /  |
4 --5-- 1
|    / |
|   /  |
3 --7-- 4
|    / |
|   /  |
3 --8-- 1
|    / |
|   /  |
2 --3-- 2
|    / |
|   /  |
1 --9-- 3
Output: 
Minimum Spanning Tree cost: 16
```

## Key Takeaways
- Prim's algorithm is a greedy approach that always chooses the locally optimal solution, which leads to a globally optimal solution.
- The time complexity of Prim's algorithm is O(E log V) using a binary heap or priority queue to store the edges.
- The space complexity is O(V + E) for storing the graph and the disjoint set data structure.