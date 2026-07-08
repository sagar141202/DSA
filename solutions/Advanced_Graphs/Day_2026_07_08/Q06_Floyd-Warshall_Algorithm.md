# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights. Given a graph with n vertices, the algorithm computes the shortest path between all pairs of vertices. The graph can contain negative weight edges, but it should not contain any negative cycles. The algorithm takes as input a 2D matrix representing the adjacency matrix of the graph, where the value at position (i, j) represents the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the value at position (i, j) is typically set to infinity.

## Approach
The Floyd-Warshall algorithm works by iteratively improving the estimate of the shortest path between each pair of vertices. It does this by considering each vertex as an intermediate step in the path. The algorithm starts with the initial adjacency matrix and then iteratively updates the matrix to include the shortest path between each pair of vertices that passes through each vertex.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void floydWarshall(int** graph, int n) {
    // Create a copy of the input graph
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
                // Update the shortest path if a shorter path is found
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
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

    // Initialize the graph
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
- The Floyd-Warshall algorithm can handle negative weight edges, but it cannot handle negative cycles.
- The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2), making it less efficient than other algorithms like Dijkstra's or Bellman-Ford for single-source shortest paths.
- The algorithm is useful for finding the shortest paths between all pairs of vertices in a weighted graph, which can be useful in a variety of applications such as network routing or traffic optimization.