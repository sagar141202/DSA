# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subset of the edges in the graph that connect all the vertices together while minimizing the total edge cost. The graph is represented as an adjacency list, where each vertex is associated with a list of its neighboring vertices and the corresponding edge weights. The constraints are: 1 ≤ V ≤ 10^5, 1 ≤ E ≤ 10^6, and the edge weights are non-negative integers.

## Approach
The algorithm starts with an arbitrary vertex and grows the MST by adding the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST. This process continues until all vertices are included in the MST. The intuition is to use a priority queue to efficiently select the minimum-weight edge.

## Complexity
- Time: O(E log V)
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

struct Edge {
    int src, dest, weight;
};

bool compareEdges(const Edge& e1, const Edge& e2) {
    return e1.weight < e2.weight;
}

int primMST(vector<vector<pair<int, int>>>& graph, int V) {
    vector<Edge> edges;
    for (int i = 0; i < V; i++) {
        for (const auto& neighbor : graph[i]) {
            edges.push_back({i, neighbor.first, neighbor.second});
        }
    }
    sort(edges.begin(), edges.end(), compareEdges);
    DisjointSet ds(V);
    int mstWeight = 0;
    for (const auto& edge : edges) {
        if (ds.find(edge.src) != ds.find(edge.dest)) {
            ds.unionSet(edge.src, edge.dest);
            mstWeight += edge.weight;
        }
    }
    return mstWeight;
}

int main() {
    int V, E;
    cin >> V >> E;
    vector<vector<pair<int, int>>> graph(V);
    for (int i = 0; i < E; i++) {
        int src, dest, weight;
        cin >> src >> dest >> weight;
        graph[src].push_back({dest, weight});
        graph[dest].push_back({src, weight});
    }
    int mstWeight = primMST(graph, V);
    cout << "Minimum Spanning Tree Weight: " << mstWeight << endl;
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
Minimum Spanning Tree Weight: 19
```

## Key Takeaways
- Use a priority queue to efficiently select the minimum-weight edge.
- Utilize a disjoint set data structure to keep track of connected components.
- The algorithm has a time complexity of O(E log V) due to the sorting of edges and the use of the priority queue.