# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights. Given a graph with n vertices, the algorithm will find the shortest path between all pairs of vertices. The graph can be represented as an adjacency matrix, where the value at row i and column j represents the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the value is typically represented as infinity. The algorithm should handle negative weight cycles, where the shortest path from a vertex to itself is negative.

## Approach
The Floyd-Warshall algorithm works by considering all possible paths of length 1, 2, ..., n between all pairs of vertices. It uses dynamic programming to build up a solution by iterating over all vertices and updating the shortest path between each pair of vertices. The algorithm can detect negative weight cycles by checking if the shortest path from a vertex to itself is negative.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = INT_MAX;

void floydWarshall(int **graph, int n) {
    // Create a copy of the graph to store the shortest paths
    int **dist = new int*[n];
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
                // Update the shortest path between vertices i and j
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    // Print the shortest paths
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

    // Check for negative weight cycles
    for (int i = 0; i < n; i++) {
        if (dist[i][i] < 0) {
            cout << "Negative weight cycle detected" << endl;
        }
    }

    // Free memory
    for (int i = 0; i < n; i++) {
        delete[] dist[i];
    }
    delete[] dist;
}

int main() {
    int n = 4;
    int **graph = new int*[n];
    for (int i = 0; i < n; i++) {
        graph[i] = new int[n];
    }

    // Initialize the graph
    graph[0][0] = 0; graph[0][1] = 5; graph[0][2] = INF; graph[0][3] = 10;
    graph[1][0] = INF; graph[1][1] = 0; graph[1][2] = 3; graph[1][3] = INF;
    graph[2][0] = INF; graph[2][1] = INF; graph[2][2] = 0; graph[2][3] = 1;
    graph[3][0] = INF; graph[3][1] = INF; graph[3][2] = INF; graph[3][3] = 0;

    floydWarshall(graph, n);

    // Free memory
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
Graph with 4 vertices:
0  5  INF 10
INF 0  3  INF
INF INF 0  1
INF INF INF 0

Output:
0  5  8  9
INF 0  3  4
INF INF 0  1
INF INF INF 0
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges and detect negative weight cycles.
- The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2), making it suitable for small to medium-sized graphs.
- The algorithm can be used to find the shortest paths between all pairs of vertices in a weighted graph.