# Bellman-Ford Algorithm

## Problem Statement
The Bellman-Ford algorithm is used to find the shortest path from a source vertex to all other vertices in a weighted graph. It can handle negative weight edges and can detect negative weight cycles. Given a graph with V vertices and E edges, and a source vertex s, the algorithm returns the shortest distance from s to all other vertices. If a negative weight cycle is detected, the algorithm returns an error message. The graph is represented as an adjacency list, where each edge is a tuple of (u, v, w), representing an edge from vertex u to vertex v with weight w.

## Approach
The Bellman-Ford algorithm works by relaxing all edges V-1 times, where V is the number of vertices. After V-1 iterations, the shortest distance from the source vertex to all other vertices is calculated. The algorithm then checks for negative weight cycles by relaxing all edges one more time. If any distance can be reduced, then a negative weight cycle is detected.

## Complexity
- Time: O(VE)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class BellmanFord {
public:
    vector<int> bellmanFord(int V, vector<vector<int>>& edges, int src) {
        // Initialize distances to all vertices as infinity
        vector<int> dist(V, INT_MAX);
        dist[src] = 0; // Distance to source vertex is 0

        // Relax all edges V-1 times
        for (int i = 0; i < V - 1; i++) {
            for (auto& edge : edges) {
                int u = edge[0];
                int v = edge[1];
                int w = edge[2];
                if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                }
            }
        }

        // Check for negative weight cycles
        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                throw runtime_error("Negative weight cycle detected");
            }
        }

        return dist;
    }
};

int main() {
    int V = 5;
    vector<vector<int>> edges = {{0, 1, -1}, {0, 2, 4}, {1, 2, 3}, {1, 3, 2}, {1, 4, 2}, {3, 2, 5}, {3, 1, 1}, {4, 3, -3}};
    int src = 0;

    BellmanFord bellmanFord;
    try {
        vector<int> dist = bellmanFord.bellmanFord(V, edges, src);
        cout << "Shortest distances from source vertex: ";
        for (int i = 0; i < V; i++) {
            cout << dist[i] << " ";
        }
        cout << endl;
    } catch (const exception& e) {
        cerr << e.what() << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
V = 5
edges = [[0, 1, -1], [0, 2, 4], [1, 2, 3], [1, 3, 2], [1, 4, 2], [3, 2, 5], [3, 1, 1], [4, 3, -3]]
src = 0
Output: 
Shortest distances from source vertex: -1 2 -2 1 0

Input: 
V = 4
edges = [[0, 1, 1], [1, 2, -1], [2, 3, 1], [3, 1, -2]]
src = 0
Output: 
Negative weight cycle detected
```

## Key Takeaways
- The Bellman-Ford algorithm can handle negative weight edges and detect negative weight cycles.
- The algorithm relaxes all edges V-1 times to calculate the shortest distance from the source vertex to all other vertices.
- If a negative weight cycle is detected, the algorithm returns an error message.