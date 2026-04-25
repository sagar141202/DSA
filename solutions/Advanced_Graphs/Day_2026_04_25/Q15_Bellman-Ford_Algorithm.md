# Bellman-Ford Algorithm

## Problem Statement
The Bellman-Ford algorithm is used to find the shortest path from a source vertex to all other vertices in a weighted graph. It can handle negative weight edges, and can detect negative weight cycles. The algorithm takes as input a graph with V vertices and E edges, and a source vertex s. The graph is represented as an adjacency list, where each edge is a tuple (u, v, w) representing an edge from vertex u to vertex v with weight w. The algorithm returns the shortest distance from the source vertex to all other vertices, or indicates if a negative weight cycle is present.

## Approach
The Bellman-Ford algorithm works by relaxing all edges V-1 times, where V is the number of vertices. This ensures that the shortest path to all vertices is found. Then, it checks for negative weight cycles by relaxing all edges one more time. If any distance can be reduced, then a negative weight cycle is present.

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
    vector<vector<int>> graph;

    Graph(int vertices) {
        V = vertices;
        graph.resize(vertices);
    }

    void addEdge(int u, int v, int w) {
        graph[u].push_back(v);
        graph[u].push_back(w);
    }

    void bellmanFord(int src) {
        vector<int> dist(V, INT_MAX);
        dist[src] = 0;

        for (int i = 0; i < V - 1; i++) {
            for (int u = 0; u < V; u++) {
                for (int j = 0; j < graph[u].size(); j += 2) {
                    int v = graph[u][j];
                    int w = graph[u][j + 1];
                    if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                    }
                }
            }
        }

        for (int u = 0; u < V; u++) {
            for (int j = 0; j < graph[u].size(); j += 2) {
                int v = graph[u][j];
                int w = graph[u][j + 1];
                if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                    cout << "Negative weight cycle detected" << endl;
                    return;
                }
            }
        }

        cout << "Vertex Distance from Source" << endl;
        for (int i = 0; i < V; i++) {
            cout << i << "\t\t" << dist[i] << endl;
        }
    }
};

int main() {
    int V = 5;
    Graph g(V);

    g.addEdge(0, 1, -1);
    g.addEdge(0, 2, 4);
    g.addEdge(1, 2, 3);
    g.addEdge(1, 3, 2);
    g.addEdge(1, 4, 2);
    g.addEdge(3, 2, 5);
    g.addEdge(3, 1, 1);
    g.addEdge(4, 3, -3);

    g.bellmanFord(0);

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
0       0
1       -1
2       2
3       -2
4       1
```

## Key Takeaways
- The Bellman-Ford algorithm can handle negative weight edges and detect negative weight cycles.
- It works by relaxing all edges V-1 times, where V is the number of vertices.
- If a negative weight cycle is detected, the algorithm indicates its presence.