# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) of the graph using Prim's algorithm. The graph is represented as an adjacency list, where each edge is a tuple of (u, v, w) representing an edge between vertices u and v with weight w. The goal is to find the subset of edges with the minimum total weight that connects all vertices in the graph. For example, given a graph with vertices {0, 1, 2, 3} and edges {(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (2, 3, 5)}, the Minimum Spanning Tree would be {(0, 1, 2), (1, 2, 3), (2, 3, 5)}.

## Approach
Prim's algorithm is a greedy algorithm that starts with an arbitrary vertex and grows the tree by adding the minimum-weight edge that connects a vertex in the tree to a vertex not yet in the tree. The algorithm uses a priority queue to efficiently select the next edge to add to the tree. The key idea is to always choose the locally optimal edge, which leads to a globally optimal solution.

## Complexity
- Time: O(E log V)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Graph {
public:
    int V;
    vector<vector<pair<int, int>>> adj;

    Graph(int vertices) : V(vertices), adj(vertices) {}

    void addEdge(int u, int v, int w) {
        adj[u].emplace_back(v, w);
        adj[v].emplace_back(u, w); // for undirected graph
    }

    int primMST() {
        vector<int> key(V, INT_MAX);
        vector<int> parent(V, -1);
        vector<bool> mstSet(V, false);
        key[0] = 0; // start with vertex 0
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.emplace(0, 0); // (weight, vertex)

        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();
            mstSet[u] = true;

            for (const auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                if (!mstSet[v] && w < key[v]) {
                    key[v] = w;
                    parent[v] = u;
                    pq.emplace(w, v);
                }
            }
        }

        int weight = 0;
        for (int i = 1; i < V; ++i) {
            weight += key[i];
        }
        return weight;
    }
};

int main() {
    int V = 4;
    Graph graph(V);
    graph.addEdge(0, 1, 2);
    graph.addEdge(0, 3, 6);
    graph.addEdge(1, 2, 3);
    graph.addEdge(1, 3, 8);
    graph.addEdge(2, 3, 5);
    cout << "Minimum Spanning Tree weight: " << graph.primMST() << endl;
    return 0;
}
```

## Test Cases
```
Input: 
Vertices: 4
Edges: [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (2, 3, 5)]
Output: 
Minimum Spanning Tree weight: 10
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm uses a priority queue to efficiently select the next edge to add to the tree.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.