# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights. Given a graph with n vertices, the algorithm computes the shortest path between all pairs of vertices. The graph can contain negative weight edges, but it should not contain any negative cycles. The algorithm takes as input a 2D matrix representing the adjacency matrix of the graph, where the value at row i and column j represents the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the value is typically represented as infinity.

## Approach
The Floyd-Warshall algorithm works by iteratively improving the estimate of the shortest path between each pair of vertices. It does this by considering all possible intermediate vertices and checking if the path through the intermediate vertex is shorter than the current shortest path. The algorithm has a dynamic programming approach, where the solution to the problem is built from the solutions of smaller sub-problems.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to implement the Floyd-Warshall algorithm
void floydWarshall(int graph[][3], int n) {
    // Create a copy of the graph to store the shortest distances
    int dist[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = graph[i][j];
        }
    }

    // Iterate over all possible intermediate vertices
    for (int k = 0; k < n; k++) {
        // Iterate over all pairs of vertices
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Check if the path through the intermediate vertex is shorter
                if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
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
    int graph[][3] = {{0, 5, INT_MAX}, {INT_MAX, 0, 3}, {INT_MAX, INT_MAX, 0}};
    int n = sizeof(graph) / sizeof(graph[0]);
    floydWarshall(graph, n);
    return 0;
}
```

## Test Cases
```
Input: 
0 5 INF
INF 0 3
INF INF 0
Output: 
0 5 8 
INF 0 3 
INF INF 0
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it cannot handle negative cycles.
- The algorithm has a time complexity of O(n^3), where n is the number of vertices in the graph.
- The algorithm can be used to find the shortest path between all pairs of vertices in a weighted graph.