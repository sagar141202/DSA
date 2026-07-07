# Bellman-Ford Algorithm

## Problem Statement
The Bellman-Ford algorithm is used to find the shortest path from a source vertex to all other vertices in a weighted graph. It can handle negative weight edges and can detect negative weight cycles. The algorithm takes as input a graph represented as an adjacency list, a source vertex, and the number of vertices. The graph can contain negative weight edges, but if a negative weight cycle is detected, the algorithm reports that no shortest path exists.

## Approach
The Bellman-Ford algorithm works by iteratively relaxing all edges in the graph, repeating this process V-1 times where V is the number of vertices. After that, it checks for negative weight cycles by trying to relax all edges one more time.

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
                for (auto edge : adj[u]) {
                    int v = edge.first;
                    int weight = edge.second;
                    if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
                        dist[v] = dist[u] + weight;
                    }
                }
            }
        }

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

        cout << "Vertex Distance from Source" << endl;
        for (int i = 0; i < V; i++) {
            cout << i << "\t\t" << dist[i] << endl;
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
Graph with 5 vertices and the following edges:
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
Vertex Distance from Source
0       0
1       -1
2       2
3       -2
4       1
```

## Key Takeaways
- The Bellman-Ford algorithm can handle negative weight edges and can detect negative weight cycles.
- It works by iteratively relaxing all edges in the graph, repeating this process V-1 times where V is the number of vertices.
- If a negative weight cycle is detected, the algorithm reports that no shortest path exists.