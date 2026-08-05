# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights. Given a graph with n vertices, the algorithm computes the shortest path between all pairs of vertices. The graph can be represented as an adjacency matrix, where the entry at row i and column j represents the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the entry is typically set to infinity. The algorithm can handle negative weight edges, but it assumes that there are no negative cycles in the graph. A negative cycle is a cycle whose total weight is negative.

## Approach
The Floyd-Warshall algorithm works by considering all possible paths between each pair of vertices. It starts by initializing the shortest distance between each pair of vertices as the direct edge weight between them. Then, it iteratively considers each vertex as an intermediate step in the path, updating the shortest distance between each pair of vertices if a shorter path is found. The algorithm has a dynamic programming approach, building the solution from smaller sub-problems.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
                // Update the shortest distance if a shorter path is found
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    // Print the shortest distances between all pairs of vertices
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
    int graph[][3] = {{0, 5, INT_MAX}, {50, 0, 15}, {30, INT_MAX, 0}};
    int n = sizeof(graph) / sizeof(graph[0]);
    floydWarshall(graph, n);
    return 0;
}
```

## Test Cases
```
Input: 
0 5 INF
50 0 15
30 INF 0
Output: 
0 5 20
30 35 0
20 25 15
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it assumes that there are no negative cycles in the graph.
- The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2), making it efficient for small to medium-sized graphs.
- The algorithm can be used to find the shortest path between all pairs of vertices in a weighted graph.