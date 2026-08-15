# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted and directed graph. Given a graph with n vertices, the algorithm computes the shortest path between every pair of vertices. The graph can contain negative weight edges, but it should not contain any negative cycles. The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2). For example, consider a graph with 4 vertices and the following edges: (0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, 1). The Floyd-Warshall algorithm will compute the shortest path between every pair of vertices.

## Approach
The Floyd-Warshall algorithm works by considering each vertex as an intermediate vertex in the shortest path between every pair of vertices. The algorithm iterates over all vertices and for each vertex, it checks if the path through the current vertex is shorter than the previously known shortest path. The algorithm uses dynamic programming to store the shortest distances between every pair of vertices.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to implement Floyd-Warshall algorithm
void floydWarshall(int graph[][4], int n) {
    // Create a 2D array to store the shortest distances
    int dist[n][n];

    // Initialize the dist array with the input graph
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = graph[i][j];
        }
    }

    // Implement the Floyd-Warshall algorithm
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Check if the path through the current vertex is shorter
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    // Print the shortest distances
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << dist[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    int graph[][4] = {{0, 5, INT_MAX, 10},
                      {INT_MAX, 0, 3, INT_MAX},
                      {INT_MAX, INT_MAX, 0, 1},
                      {INT_MAX, INT_MAX, INT_MAX, 0}};

    int n = sizeof(graph) / sizeof(graph[0]);

    floydWarshall(graph, n);

    return 0;
}
```

## Test Cases
```
Input: 
0 5 INF 10
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
- The Floyd-Warshall algorithm can handle negative weight edges, but it cannot handle negative cycles.
- The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2), making it less efficient than other algorithms like Dijkstra's or Bellman-Ford for single-source shortest path problems.
- The algorithm is useful for finding the shortest path between all pairs of vertices in a weighted and directed graph.