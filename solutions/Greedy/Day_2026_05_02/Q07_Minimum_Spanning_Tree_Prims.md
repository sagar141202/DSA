# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list, where each edge is a tuple of (u, v, w) representing an edge between vertices u and v with weight w. The goal is to find the MST with the minimum total weight.

## Approach
Prim's algorithm starts with an arbitrary vertex and grows the MST by adding the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST. This process is repeated until all vertices are included in the MST. The algorithm uses a priority queue to efficiently select the minimum-weight edge.

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

    Graph(int vertices) {
        V = vertices;
        adj.resize(vertices);
    }

    void addEdge(int u, int v, int w) {
        adj[u].emplace_back(v, w);
        adj[v].emplace_back(u, w);
    }

    int primMST() {
        vector<int> key(V, INT_MAX);
        vector<int> parent(V, -1);
        vector<bool> mstSet(V, false);

        key[0] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, 0});

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
                    pq.push({w, v});
                }
            }
        }

        int weight = 0;
        for (int i = 1; i < V; i++) {
            weight += key[i];
        }

        return weight;
    }
};

int main() {
    int V = 5;
    Graph graph(V);

    graph.addEdge(0, 1, 2);
    graph.addEdge(0, 3, 6);
    graph.addEdge(1, 2, 3);
    graph.addEdge(1, 3, 8);
    graph.addEdge(1, 4, 5);
    graph.addEdge(2, 4, 7);
    graph.addEdge(3, 4, 9);

    int mstWeight = graph.primMST();
    cout << "Minimum Spanning Tree Weight: " << mstWeight << endl;

    return 0;
}
```

## Test Cases
```
Input: 
Vertices: 5
Edges: [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
Output: 
Minimum Spanning Tree Weight: 16
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm uses a priority queue to efficiently select the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.