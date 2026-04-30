# Bellman-Ford Algorithm

## Problem Statement
The Bellman-Ford algorithm is used to find the shortest path from a source vertex to all other vertices in a weighted graph. It can handle negative weight edges and can detect negative weight cycles. The algorithm takes as input a graph represented as an adjacency list, a source vertex, and the number of vertices in the graph. The output is the shortest distance from the source vertex to all other vertices. If a negative weight cycle is detected, the algorithm reports that the graph contains a negative weight cycle.

## Approach
The Bellman-Ford algorithm works by relaxing all edges in the graph V-1 times, where V is the number of vertices. If after V-1 iterations, we can still relax an edge, then the graph contains a negative weight cycle. The algorithm uses dynamic programming to keep track of the shortest distance from the source vertex to all other vertices.

## Complexity
- Time: O(VE)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Graph {
    int V;
    vector<vector<pair<int, int>>> adj;

public:
    Graph(int vertices) {
        V = vertices;
        adj.resize(vertices);
    }

    void addEdge(int u, int v, int weight) {
        adj[u].push_back({v, weight});
    }

    void bellmanFord(int src) {
        vector<int> dist(V, INT_MAX);
        dist[src] = 0;

        for (int i = 0; i < V - 1; i++) {
            for (int u = 0; u < V; u++) {
                for (auto& edge : adj[u]) {
                    int v = edge.first;
                    int weight = edge.second;
                    if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
                        dist[v] = dist[u] + weight;
                    }
                }
            }
        }

        for (int u = 0; u < V; u++) {
            for (auto& edge : adj[u]) {
                int v = edge.first;
                int weight = edge.second;
                if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
                    cout << "Graph contains negative weight cycle" << endl;
                    return;
                }
            }
        }

        cout << "Vertex\tDistance from source" << endl;
        for (int i = 0; i < V; i++) {
            cout << i << "\t" << dist[i] << endl;
        }
    }
};

int main() {
    Graph g(5);
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
Graph with 5 vertices and edges:
(0, 1) with weight -1
(0, 2) with weight 4
(1, 2) with weight 3
(1, 3) with weight 2
(1, 4) with weight 2
(3, 2) with weight 5
(3, 1) with weight 1
(4, 3) with weight -3
Source vertex: 0

Output: 
Vertex Distance from source
0       0
1       -1
2       2
3       -2
4       1
```

## Key Takeaways
- The Bellman-Ford algorithm can handle negative weight edges and can detect negative weight cycles.
- The algorithm has a time complexity of O(VE), where V is the number of vertices and E is the number of edges.
- The algorithm uses dynamic programming to keep track of the shortest distance from the source vertex to all other vertices.