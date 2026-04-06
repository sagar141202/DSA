# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights. Given a graph with n vertices, the algorithm computes the shortest path between all pairs of vertices. If there is a negative weight cycle, the algorithm can detect it. The graph is represented as an adjacency matrix, where the entry at row i and column j represents the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the entry is typically set to infinity.

## Approach
The Floyd-Warshall algorithm works by considering all possible paths of length 1, 2, ..., n between all pairs of vertices. It iteratively updates the shortest distance between each pair of vertices by considering the shortest path that goes through each vertex. The algorithm uses dynamic programming to efficiently compute the shortest distances.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = INT_MAX;

void floydWarshall(int** graph, int n) {
    // Create a copy of the graph to store the shortest distances
    int** dist = new int*[n];
    for (int i = 0; i < n; i++) {
        dist[i] = new int[n];
        for (int j = 0; j < n; j++) {
            dist[i][j] = graph[i][j];
        }
    }

    // Iterate over all vertices
    for (int k = 0; k < n; k++) {
        // Iterate over all pairs of vertices
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Update the shortest distance between vertices i and j
                // by considering the path that goes through vertex k
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    // Print the shortest distances
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (dist[i][j] == INF) {
                cout << "INF ";
            } else {
                cout << dist[i][j] << " ";
            }
        }
        cout << endl;
    }

    // Free memory
    for (int i = 0; i < n; i++) {
        delete[] dist[i];
    }
    delete[] dist;
}

int main() {
    int n = 4;
    int** graph = new int*[n];
    for (int i = 0; i < n; i++) {
        graph[i] = new int[n];
    }

    // Initialize the graph
    graph[0][0] = 0; graph[0][1] = 5; graph[0][2] = INF; graph[0][3] = 10;
    graph[1][0] = INF; graph[1][1] = 0; graph[1][2] = 3; graph[1][3] = INF;
    graph[2][0] = INF; graph[2][1] = INF; graph[2][2] = 0; graph[2][3] = 1;
    graph[3][0] = INF; graph[3][1] = INF; graph[3][2] = INF; graph[3][3] = 0;

    floydWarshall(graph, n);

    // Free memory
    for (int i = 0; i < n; i++) {
        delete[] graph[i];
    }
    delete[] graph;

    return 0;
}
```

## Test Cases
```
Input:
0 5 INF INF
INF 0 3 INF
INF INF 0 1
INF INF INF 0
Output:
0 5 8 9 
INF 0 3 4 
INF INF 0 1 
INF INF INF 0
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it can also detect negative weight cycles.
- The algorithm has a time complexity of O(n^3), where n is the number of vertices in the graph.
- The algorithm uses dynamic programming to efficiently compute the shortest distances between all pairs of vertices.