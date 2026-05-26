# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted graph. The graph can be directed or undirected and may contain negative weight edges, but it should not contain any negative cycles. The algorithm takes as input a 2D matrix representing the adjacency matrix of the graph, where the value at index [i][j] represents the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the value at index [i][j] is typically set to a large number or infinity. The algorithm returns a 2D matrix representing the shortest path between all pairs of vertices.

## Approach
The Floyd-Warshall algorithm works by considering each vertex as an intermediate step in the shortest path between all pairs of vertices. It iteratively updates the shortest path between each pair of vertices by considering all possible intermediate vertices. The algorithm uses dynamic programming to efficiently compute the shortest paths.

## Complexity
- Time: O(V^3)
- Space: O(V^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to implement Floyd-Warshall algorithm
void floydWarshall(int** graph, int V) {
    // Create a copy of the input graph
    int** dist = new int*[V];
    for (int i = 0; i < V; i++) {
        dist[i] = new int[V];
        for (int j = 0; j < V; j++) {
            dist[i][j] = graph[i][j];
        }
    }

    // Iterate over all intermediate vertices
    for (int k = 0; k < V; k++) {
        // Iterate over all pairs of vertices
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                // Update the shortest path if a shorter path is found
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    // Print the shortest path matrix
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            cout << dist[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    int V = 4;
    int** graph = new int*[V];
    for (int i = 0; i < V; i++) {
        graph[i] = new int[V];
    }

    // Initialize the graph with sample values
    graph[0][0] = 0; graph[0][1] = 5; graph[0][2] = INT_MAX; graph[0][3] = 10;
    graph[1][0] = INT_MAX; graph[1][1] = 0; graph[1][2] = 3; graph[1][3] = INT_MAX;
    graph[2][0] = INT_MAX; graph[2][1] = INT_MAX; graph[2][2] = 0; graph[2][3] = 1;
    graph[3][0] = INT_MAX; graph[3][1] = INT_MAX; graph[3][2] = INT_MAX; graph[3][3] = 0;

    floydWarshall(graph, V);

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
- The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted graph.
- The algorithm has a time complexity of O(V^3) and a space complexity of O(V^2), where V is the number of vertices in the graph.
- The algorithm can handle negative weight edges but should not contain any negative cycles.