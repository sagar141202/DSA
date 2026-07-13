# Bellman-Ford Algorithm

## Problem Statement
The Bellman-Ford algorithm is used to find the shortest path from a source vertex to all other vertices in a weighted graph. It can handle negative weight edges and can detect negative weight cycles. The algorithm takes as input a graph represented as an adjacency list and a source vertex, and outputs the shortest distance from the source vertex to all other vertices. If a negative weight cycle is detected, the algorithm reports that no shortest path exists.

## Approach
The Bellman-Ford algorithm works by relaxing all edges in the graph V-1 times, where V is the number of vertices. After that, it checks for negative weight cycles by trying to relax all edges one more time. If any edge can be relaxed, then a negative weight cycle exists.

## Complexity
- Time: O(VE)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int src, dest, weight;
};

void bellmanFord(vector<Edge> edges, int V, int src) {
    // Initialize distances to all vertices as infinity
    vector<int> dist(V, INT_MAX);
    dist[src] = 0; // Distance to source is 0

    // Relax all edges V-1 times
    for (int i = 0; i < V - 1; i++) {
        for (Edge edge : edges) {
            if (dist[edge.src] != INT_MAX && dist[edge.src] + edge.weight < dist[edge.dest]) {
                dist[edge.dest] = dist[edge.src] + edge.weight;
            }
        }
    }

    // Check for negative weight cycles
    for (Edge edge : edges) {
        if (dist[edge.src] != INT_MAX && dist[edge.src] + edge.weight < dist[edge.dest]) {
            cout << "Negative weight cycle detected" << endl;
            return;
        }
    }

    // Print shortest distances
    cout << "Vertex" << "\t" << "Distance from source" << endl;
    for (int i = 0; i < V; i++) {
        cout << i << "\t" << dist[i] << endl;
    }
}

int main() {
    int V = 5;
    vector<Edge> edges = {{0, 1, -1}, {0, 2, 4}, {1, 2, 3}, {1, 3, 2}, {1, 4, 2}, {3, 2, 5}, {3, 1, 1}, {4, 3, -3}};

    bellmanFord(edges, V, 0);

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and edges: (0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)
Source vertex: 0
Output: 
Vertex  Distance from source
0       0
1       -1
2       2
3       -2
4       1
```

## Key Takeaways
- The Bellman-Ford algorithm can handle negative weight edges and detect negative weight cycles.
- It works by relaxing all edges V-1 times, where V is the number of vertices, and then checking for negative weight cycles.
- The algorithm has a time complexity of O(VE), where E is the number of edges, and a space complexity of O(V).