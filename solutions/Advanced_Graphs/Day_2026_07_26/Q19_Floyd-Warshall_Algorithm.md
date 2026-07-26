# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights. Given a graph with n vertices, the algorithm computes the shortest path between all pairs of vertices. The graph can be represented as an adjacency matrix, where the value at row i and column j represents the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the value is typically set to infinity. The algorithm can handle negative weight edges, but it assumes that the graph does not contain any negative cycles.

## Approach
The Floyd-Warshall algorithm works by considering all possible paths of length 1, 2, ..., n between all pairs of vertices. It uses dynamic programming to build up a solution by iteratively improving the shortest path between each pair of vertices. The algorithm starts with the initial adjacency matrix and then iteratively updates the matrix to include shorter paths.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = INT_MAX;

void floydWarshall(int** graph, int n) {
    // Create a copy of the graph to store the shortest distances
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
                // Check if the path through vertex k is shorter
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    int newDist = dist[i][k] + dist[k][j];
                    if (newDist < dist[i][j]) {
                        dist[i][j] = newDist;
                    }
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

    // Free memory
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
- The Floyd-Warshall algorithm can handle negative weight edges, but it assumes that the graph does not contain any negative cycles.
- The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2), where n is the number of vertices in the graph.
- The algorithm is useful for finding the shortest paths between all pairs of vertices in a weighted graph.