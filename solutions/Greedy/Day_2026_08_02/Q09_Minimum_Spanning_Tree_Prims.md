# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list, where each edge is a tuple of (vertex1, vertex2, weight). The constraints are: 1 ≤ V ≤ 10^5, 1 ≤ E ≤ 10^5, and 1 ≤ weight ≤ 10^5. For example, given a graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)}, the MST should have edges {(0, 3, 5), (2, 3, 4), (0, 1, 10), (0, 2, 6)} with a total weight of 25.

## Approach
Prim's algorithm is used to find the MST by starting at an arbitrary vertex and growing the tree by adding the minimum-weight edge that connects a vertex in the tree to a vertex not yet in the tree. The algorithm uses a priority queue to efficiently select the minimum-weight edge. It works by maintaining a set of visited vertices and iteratively adding the minimum-weight edge that connects a visited vertex to an unvisited vertex.

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

struct Edge {
    int vertex1, vertex2, weight;
    Edge(int v1, int v2, int w) : vertex1(v1), vertex2(v2), weight(w) {}
    bool operator<(const Edge& other) const {
        return weight > other.weight;
    }
};

vector<Edge> primMST(vector<vector<pair<int, int>>>& graph, int V) {
    vector<Edge> mst;
    DisjointSet ds(V);
    priority_queue<Edge> pq;
    for (auto& edge : graph[0]) {
        pq.push(Edge(0, edge.first, edge.second));
    }
    while (!pq.empty() && mst.size() < V - 1) {
        Edge edge = pq.top();
        pq.pop();
        if (ds.find(edge.vertex1) != ds.find(edge.vertex2)) {
            mst.push_back(edge);
            ds.unionSets(edge.vertex1, edge.vertex2);
            for (auto& neighbor : graph[edge.vertex2]) {
                if (ds.find(neighbor.first) != ds.find(edge.vertex1)) {
                    pq.push(Edge(edge.vertex2, neighbor.first, neighbor.second));
                }
            }
        }
    }
    return mst;
}

int main() {
    int V = 5;
    vector<vector<pair<int, int>>> graph(V);
    graph[0].push_back({1, 10});
    graph[0].push_back({2, 6});
    graph[0].push_back({3, 5});
    graph[1].push_back({3, 15});
    graph[2].push_back({3, 4});
    vector<Edge> mst = primMST(graph, V);
    for (auto& edge : mst) {
        cout << "Edge: (" << edge.vertex1 << ", " << edge.vertex2 << ", " << edge.weight << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
Vertices: 5
Edges: [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
Output: 
Edge: (0, 3, 5)
Edge: (2, 3, 4)
Edge: (0, 1, 10)
Edge: (0, 2, 6)
```

## Key Takeaways
- Prim's algorithm is used to find the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm starts at an arbitrary vertex and grows the tree by adding the minimum-weight edge that connects a vertex in the tree to a vertex not yet in the tree.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.