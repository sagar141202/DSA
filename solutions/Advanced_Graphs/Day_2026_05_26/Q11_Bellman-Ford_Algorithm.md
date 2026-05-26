# Bellman-Ford Algorithm

## Problem Statement
The Bellman-Ford algorithm is used to find the shortest path from a source vertex to all other vertices in a weighted graph. It can handle negative weight edges, and can detect negative weight cycles. Given a graph with V vertices and E edges, and a source vertex s, the algorithm will output the shortest distance from s to all other vertices. If a negative weight cycle is detected, the algorithm will output an error message. The graph is represented as an adjacency list, where each edge is a pair (u, v, w) representing an edge from vertex u to vertex v with weight w.

## Approach
The Bellman-Ford algorithm works by relaxing all edges V-1 times, where V is the number of vertices. After V-1 iterations, the shortest distance to all vertices is known. If we relax all edges one more time and the distance to any vertex can still be reduced, then there is a negative weight cycle.

## Complexity
- Time: O(VE)
- Space: O(V)

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
        adj[u].push_back({v, w});
    }

    void bellmanFord(int src) {
        vector<int> dist(V, INT_MAX);
        dist[src] = 0;

        for (int i = 0; i < V - 1; i++) {
            for (int u = 0; u < V; u++) {
                for (auto edge : adj[u]) {
                    int v = edge.first;
                    int w = edge.second;
                    if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                    }
                }
            }
        }

        for (int u = 0; u < V; u++) {
            for (auto edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                    cout << "Negative weight cycle detected" << endl;
                    return;
                }
            }
        }

        cout << "Vertex\tDistance from Source" << endl;
        for (int i = 0; i < V; i++) {
            cout << i << "\t" << dist[i] << endl;
        }
    }
};

int main() {
    int V = 5;
    Graph graph(V);
    graph.addEdge(0, 1, -1);
    graph.addEdge(0, 2, 4);
    graph.addEdge(1, 2, 3);
    graph.addEdge(1, 3, 2);
    graph.addEdge(1, 4, 2);
    graph.addEdge(3, 2, 5);
    graph.addEdge(3, 1, 1);
    graph.addEdge(4, 3, -3);

    graph.bellmanFord(0);

    return 0;
}
```

## Test Cases
```
Input:
Graph with 5 vertices and 8 edges:
(0, 1, -1)
(0, 2, 4)
(1, 2, 3)
(1, 3, 2)
(1, 4, 2)
(3, 2, 5)
(3, 1, 1)
(4, 3, -3)
Source vertex: 0

Output:
Vertex Distance from Source
0    0
1    -1
2    2
3    -2
4    1
```

## Key Takeaways
- The Bellman-Ford algorithm can handle negative weight edges and detect negative weight cycles.
- The algorithm works by relaxing all edges V-1 times, where V is the number of vertices.
- If a negative weight cycle is detected, the algorithm will output an error message.