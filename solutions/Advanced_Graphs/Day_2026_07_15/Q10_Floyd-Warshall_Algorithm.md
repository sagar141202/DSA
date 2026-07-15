# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights. Given a weighted graph G = (V, E) with n vertices, the algorithm computes the shortest path between all pairs of vertices. The graph can contain negative weight edges, but it should not contain any negative cycles. The algorithm should be able to handle graphs with n vertices and m edges, where m is the number of edges in the graph. For example, consider a graph with 4 vertices and 5 edges: (0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, 1), (3, 1, -2). The shortest path from vertex 0 to vertex 1 is 0 -> 3 -> 1 with a total weight of 8.

## Approach
The Floyd-Warshall algorithm works by considering all possible paths of length 1, 2, ..., n between all pairs of vertices. It iteratively updates the shortest path between each pair of vertices by considering all possible intermediate vertices. The algorithm uses dynamic programming to build up the solution.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to implement Floyd-Warshall algorithm
void floydWarshall(int graph[][4], int n) {
    int dist[n][n];

    // Initialize the distance matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = graph[i][j];
        }
    }

    // Implement Floyd-Warshall algorithm
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
    int graph[][4] = {{0, 5, INT_MAX, 10},
                       {INT_MAX, 0, 3, INT_MAX},
                       {INT_MAX, INT_MAX, 0, 1},
                       {INT_MAX, -2, INT_MAX, 0}};

    int n = sizeof(graph) / sizeof(graph[0]);

    floydWarshall(graph, n);

    return 0;
}
```

## Test Cases
```
Input: 
0 5 INF INF
INF 0 3 INF
INF INF 0 1
INF -2 INF 0

Output: 
0 5 8 9
4 0 3 4
6 3 0 1
2 1 -2 0
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it cannot handle negative cycles.
- The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2).
- The algorithm is useful for finding the shortest paths between all pairs of vertices in a weighted graph.