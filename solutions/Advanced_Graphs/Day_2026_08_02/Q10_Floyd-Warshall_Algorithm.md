# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted graph. Given a graph with n vertices, the algorithm computes the shortest path between every pair of vertices. The graph can contain negative weight edges, but it should not contain any negative cycles. The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2). For example, consider a graph with 4 vertices and the following edges: (0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, 1). The shortest path between every pair of vertices can be computed using the Floyd-Warshall algorithm.

## Approach
The Floyd-Warshall algorithm works by considering each vertex as an intermediate vertex in the shortest path between every pair of vertices. It iterates over all vertices and updates the shortest distance between every pair of vertices. The algorithm uses dynamic programming to store the shortest distances between every pair of vertices.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void floydWarshall(int graph[][3], int n) {
    // Create a 2D array to store the shortest distances between every pair of vertices
    int dist[n][n];
    
    // Initialize the dist array with the given graph
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = INT_MAX;
        }
    }
    
    // Initialize the dist array with the given graph
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                dist[i][j] = 0;
            }
        }
    }
    
    // Initialize the dist array with the given graph
    for (int i = 0; i < 3; i++) {
        dist[graph[i][0]][graph[i][1]] = graph[i][2];
        dist[graph[i][1]][graph[i][0]] = graph[i][2]; // Remove this line for directed graph
    }
    
    // Compute the shortest distances between every pair of vertices
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    
    // Print the shortest distances between every pair of vertices
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (dist[i][j] == INT_MAX) {
                cout << "INF ";
            } else {
                cout << dist[i][j] << " ";
            }
        }
        cout << endl;
    }
}

int main() {
    int graph[][3] = {{0, 1, 5}, {0, 3, 10}, {1, 2, 3}, {2, 3, 1}};
    int n = 4;
    floydWarshall(graph, n);
    return 0;
}
```

## Test Cases
```
Input: 
Graph with edges: (0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, 1)
Output: 
0 5 8 6 
INF 0 3 4 
INF INF 0 1 
INF INF INF 0 
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it cannot handle negative cycles.
- The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2).
- The algorithm uses dynamic programming to store the shortest distances between every pair of vertices.