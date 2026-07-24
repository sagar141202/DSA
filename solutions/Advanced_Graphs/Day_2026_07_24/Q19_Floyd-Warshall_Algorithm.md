# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights. Given a graph with n vertices, the algorithm computes the shortest path between all pairs of vertices. The graph is represented as an adjacency matrix, where the value at row i and column j represents the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the value is typically set to infinity. The algorithm can handle negative weight edges, but it assumes that there are no negative cycles in the graph.

## Approach
The Floyd-Warshall algorithm uses dynamic programming to find the shortest paths between all pairs of vertices. It iterates over all vertices and for each vertex, it checks if the path from the source vertex to the destination vertex can be shortened by going through the current vertex. The algorithm has a time complexity of O(n^3), where n is the number of vertices in the graph.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = INT_MAX;

void floydWarshall(int graph[][3], int n) {
    // Create a copy of the graph to store the shortest distances
    int dist[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = graph[i][j];
        }
    }

    // Iterate over all vertices
    for (int k = 0; k < n; k++) {
        // Iterate over all pairs of vertices
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Check if the path from i to j can be shortened by going through k
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
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
}

int main() {
    int graph[][3] = {{0, 5, INF}, {10, 0, 3}, {INF, INF, 0}};
    int n = sizeof(graph) / sizeof(graph[0]);
    floydWarshall(graph, n);
    return 0;
}
```

## Test Cases
```
Input:
0 5 INF
10 0 3
INF INF 0

Output:
0 5 8
10 0 3
INF INF 0
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it assumes that there are no negative cycles in the graph.
- The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2), where n is the number of vertices in the graph.
- The algorithm can be used to find the shortest paths between all pairs of vertices in a weighted graph.