# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted and directed graph. Given a graph with `n` vertices and `m` edges, where each edge has a weight, the goal is to find the minimum weight path between every pair of vertices. The graph can contain negative weight edges, but it should not contain any negative cycles. If a negative cycle is present, the algorithm can detect it. For example, consider a graph with 4 vertices and 5 edges: (0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, 1), (3, 1, -15). The algorithm should output the shortest distance between every pair of vertices.

## Approach
The Floyd-Warshall algorithm works by considering each vertex as an intermediate step in the shortest path between two vertices. It iterates over all vertices and updates the shortest distance between every pair of vertices. The algorithm uses dynamic programming to store the shortest distances in a 2D matrix. The time complexity of the algorithm is O(n^3), where n is the number of vertices.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void floydWarshall(int graph[][3], int n) {
    // Create a 2D matrix to store the shortest distances
    int dist[n][n];

    // Initialize the distance matrix with the input graph
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = INT_MAX;
        }
    }

    // Populate the distance matrix with the weights of the direct edges
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                dist[i][j] = 0;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            if (graph[i][j] != 0) {
                dist[i][graph[i][j]] = graph[i][j];
            }
        }
    }

    // Floyd-Warshall algorithm
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    // Print the shortest distances
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
    int graph[][3] = {{1, 2, 3}, {0, 2, 3}, {0, 1, 3}, {0, 1, 2}};
    int n = 4;
    floydWarshall(graph, n);
    return 0;
}
```

## Test Cases
```
Input: 
graph = [[0, 5, 0, 10], 
         [0, 0, 3, 0], 
         [0, 0, 0, 1], 
         [0, -15, 0, 0]]
Output: 
0 5 8 9 
-10 0 3 -4 
-10 5 0 1 
-10 -10 -5 0 
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it cannot handle negative cycles.
- The algorithm uses a 2D matrix to store the shortest distances between every pair of vertices.
- The time complexity of the algorithm is O(n^3), where n is the number of vertices.