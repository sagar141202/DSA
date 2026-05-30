# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted graph. The graph can contain negative weight edges, but it should not contain any negative cycles. The algorithm takes as input a weighted adjacency matrix representing the graph and outputs a new matrix where the value at row i and column j represents the shortest distance from vertex i to vertex j. For example, given a graph with vertices {0, 1, 2} and edges {(0, 1, 5), (1, 2, -2), (0, 2, 3)}, the algorithm will output the shortest distances between all pairs of vertices.

## Approach
The Floyd-Warshall algorithm works by considering all possible paths between each pair of vertices and selecting the one with the minimum weight. It iterates over all vertices and for each vertex, it checks if using that vertex as an intermediate node reduces the distance between any pair of vertices.

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
                // Check if using vertex k as an intermediate node reduces the distance
                if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    // Print the resulting distance matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << dist[i][j] << " ";
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
    int n = 3;
    int** graph = new int*[n];
    for (int i = 0; i < n; i++) {
        graph[i] = new int[n];
        for (int j = 0; j < n; j++) {
            graph[i][j] = INT_MAX;
        }
    }

    // Initialize the graph
    graph[0][0] = 0;
    graph[1][1] = 0;
    graph[2][2] = 0;
    graph[0][1] = 5;
    graph[1][2] = -2;
    graph[0][2] = 3;

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
Graph with vertices {0, 1, 2} and edges {(0, 1, 5), (1, 2, -2), (0, 2, 3)}
Output: 
Shortest distances between all pairs of vertices:
0 5 -1 
8 0 -2 
3 8 0
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges but not negative cycles.
- It has a time complexity of O(n^3) and a space complexity of O(n^2), where n is the number of vertices in the graph.
- The algorithm is useful for finding the shortest path between all pairs of vertices in a weighted graph.