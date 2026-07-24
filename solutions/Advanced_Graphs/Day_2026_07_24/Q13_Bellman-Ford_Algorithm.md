# Bellman-Ford Algorithm

## Problem Statement
The Bellman-Ford algorithm is used to find the shortest path from a source vertex to all other vertices in a weighted graph. It can handle negative weight edges and can detect negative weight cycles. The algorithm takes as input a graph represented as an adjacency list or matrix, a source vertex, and the number of vertices. The output is the shortest distance from the source vertex to all other vertices. If a negative weight cycle is detected, the algorithm reports that no shortest path exists.

## Approach
The Bellman-Ford algorithm works by relaxing all edges V-1 times, where V is the number of vertices. If an edge can still be relaxed after V-1 iterations, then a negative weight cycle exists. The algorithm uses dynamic programming to build up the shortest distances.

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

    void addEdge(int u, int v, int weight) {
        adj[u].push_back({v, weight});
    }

    void bellmanFord(int src) {
        vector<int> dist(V, INT_MAX);
        dist[src] = 0;

        for (int i = 0; i < V - 1; i++) {
            for (int u = 0; u < V; u++) {
                for (auto edge : adj[u]) {
                    int v = edge.first;
                    int weight = edge.second;
                    if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
                        dist[v] = dist[u] + weight;
                    }
                }
            }
        }

        // Check for negative weight cycles
        for (int u = 0; u < V; u++) {
            for (auto edge : adj[u]) {
                int v = edge.first;
                int weight = edge.second;
                if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
                    cout << "Negative weight cycle detected" << endl;
                    return;
                }
            }
        }

        // Print shortest distances
        for (int i = 0; i < V; i++) {
            cout << "Shortest distance from " << src << " to " << i << ": " << dist[i] << endl;
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
Graph with 5 vertices and edges:
(0, 1, -1)
(0, 2, 4)
(1, 2, 3)
(1, 3, 2)
(1, 4, 2)
(3, 2, 5)
(3, 1, 1)
(4, 3, -3)

Output: 
Shortest distance from 0 to 0: 0
Shortest distance from 0 to 1: -1
Shortest distance from 0 to 2: 2
Shortest distance from 0 to 3: -2
Shortest distance from 0 to 4: 1
```

## Key Takeaways
- The Bellman-Ford algorithm can handle negative weight edges and detect negative weight cycles.
- The algorithm has a time complexity of O(VE), where V is the number of vertices and E is the number of edges.
- The algorithm uses dynamic programming to build up the shortest distances.