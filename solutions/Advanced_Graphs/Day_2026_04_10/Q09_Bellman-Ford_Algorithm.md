# Bellman-Ford Algorithm

## Problem Statement
The Bellman-Ford algorithm is used to find the shortest path from a source vertex to all other vertices in a weighted graph. It can handle negative weight edges and can detect negative cycles. Given a graph with V vertices and E edges, and a source vertex s, the algorithm will output the shortest distance from s to all other vertices. If a negative cycle is detected, the algorithm will output that a negative cycle exists.

## Approach
The Bellman-Ford algorithm works by relaxing all edges V-1 times, where V is the number of vertices. After relaxing all edges V-1 times, we check for negative-weight cycles by relaxing all edges one more time. If we can still relax edges, then a negative cycle exists.

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
    Graph(int vertices) : V(vertices), adj(vertices) {}

    void addEdge(int u, int v, int w) {
        adj[u].emplace_back(v, w);
    }

    void bellmanFord(int src) {
        vector<int> dist(V, INT_MAX);
        dist[src] = 0;

        for (int i = 0; i < V - 1; i++) {
            for (int u = 0; u < V; u++) {
                for (const auto& edge : adj[u]) {
                    int v = edge.first;
                    int w = edge.second;
                    if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                    }
                }
            }
        }

        for (int u = 0; u < V; u++) {
            for (const auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                    cout << "Negative cycle detected" << endl;
                    return;
                }
            }
        }

        cout << "Vertex \tDistance from Source" << endl;
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
0 -> 1 (weight: -1)
0 -> 2 (weight: 4)
1 -> 2 (weight: 3)
1 -> 3 (weight: 2)
1 -> 4 (weight: 2)
3 -> 2 (weight: 5)
3 -> 1 (weight: 1)
4 -> 3 (weight: -3)
Source vertex: 0

Output: 
Vertex  Distance from Source
0       0
1       -1
2       2
3       -2
4       1
```

## Key Takeaways
- The Bellman-Ford algorithm can handle negative weight edges and detect negative cycles.
- The algorithm has a time complexity of O(VE), where V is the number of vertices and E is the number of edges.
- The algorithm has a space complexity of O(V), where V is the number of vertices.