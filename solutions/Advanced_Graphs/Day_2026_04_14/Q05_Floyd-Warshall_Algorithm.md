# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted graph. Given a graph with n vertices and edges with weights, the algorithm should output a 2D matrix where the value at the i-th row and j-th column represents the minimum weight path from vertex i to vertex j. The graph can contain negative weight edges, but it should not contain negative weight cycles. The algorithm should be able to handle graphs with up to 100 vertices.

## Approach
The Floyd-Warshall algorithm uses dynamic programming to find the shortest path between all pairs of vertices. It works by considering each vertex as an intermediate step in the path and updating the shortest distance matrix accordingly. The algorithm iterates over all vertices and updates the shortest distance between each pair of vertices.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
                // Update the shortest distance if a shorter path is found
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    // Print the shortest distance matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << dist[i][j] << " ";
        }
        cout << endl;
    }

    // Deallocate memory
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

    // Initialize the graph with weights
    graph[0][0] = 0; graph[0][1] = 5; graph[0][2] = INT_MAX; graph[0][3] = 10;
    graph[1][0] = INT_MAX; graph[1][1] = 0; graph[1][2] = 3; graph[1][3] = INT_MAX;
    graph[2][0] = INT_MAX; graph[2][1] = INT_MAX; graph[2][2] = 0; graph[2][3] = 1;
    graph[3][0] = INT_MAX; graph[3][1] = INT_MAX; graph[3][2] = INT_MAX; graph[3][3] = 0;

    floydWarshall(graph, n);

    // Deallocate memory
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
- The Floyd-Warshall algorithm can handle graphs with negative weight edges, but it should not contain negative weight cycles.
- The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2).
- The algorithm can be used to find the shortest path between all pairs of vertices in a weighted graph.