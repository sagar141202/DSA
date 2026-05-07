# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights. Given a graph with n vertices, the algorithm computes the shortest path between all pairs of vertices. The graph can contain negative weight edges, but it should not contain any negative cycles. The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2). For example, consider a graph with 4 vertices and the following edges: (0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, -15). The algorithm should output the shortest distance between all pairs of vertices.

## Approach
The Floyd-Warshall algorithm uses dynamic programming to find the shortest paths between all pairs of vertices. It works by considering each vertex as an intermediate step in the path. The algorithm iterates over all vertices and for each vertex, it checks if the path from the source to the destination through the current vertex is shorter than the previously known path.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void floydWarshall(int graph[][4], int n) {
    // Create a 2D array to store the shortest distances
    int dist[n][n];
    
    // Initialize the dist array with the input graph
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = graph[i][j];
        }
    }
    
    // Iterate over all vertices
    for (int k = 0; k < n; k++) {
        // Iterate over all source vertices
        for (int i = 0; i < n; i++) {
            // Iterate over all destination vertices
            for (int j = 0; j < n; j++) {
                // Check if the path from the source to the destination through the current vertex is shorter
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
                       {INT_MAX, INT_MAX, 0, -15},
                       {INT_MAX, INT_MAX, INT_MAX, 0}};
    floydWarshall(graph, 4);
    return 0;
}
```

## Test Cases
```
Input: 
0 5 INF 10
INF 0 3 INF
INF INF 0 -15
INF INF INF 0
Output: 
0 5 8 -5
INF 0 3 -12
INF INF 0 -15
INF INF INF 0
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it cannot handle negative cycles.
- The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2).
- The algorithm uses dynamic programming to find the shortest paths between all pairs of vertices.