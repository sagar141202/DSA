# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted graph. The graph can have positive or negative edge weights, but it should not have any negative cycles. The algorithm takes as input a graph represented as an adjacency matrix and returns the shortest distance between all pairs of vertices. For example, given a graph with vertices {0, 1, 2} and edges {(0, 1, 5), (1, 2, 3), (0, 2, 7)}, the algorithm should return the shortest distances between all pairs of vertices, which are {(0, 0, 5, 8), (0, 1, 0, 3), (0, 2, 0, 0)}.

## Approach
The Floyd-Warshall algorithm uses dynamic programming to find the shortest path between all pairs of vertices. It works by considering each vertex as an intermediate step in the path and updating the shortest distance between all pairs of vertices accordingly. The algorithm iterates over all vertices and for each vertex, it checks if the path through the current vertex is shorter than the previously known shortest path.

## Complexity
- Time: O(V^3)
- Space: O(V^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = INT_MAX;

void floydWarshall(vector<vector<int>>& graph) {
    int V = graph.size();
    // Create a copy of the graph to store the shortest distances
    vector<vector<int>> dist(V, vector<int>(V, INF));
    
    // Initialize the dist matrix with the input graph
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            dist[i][j] = graph[i][j];
        }
    }
    
    // Iterate over all vertices
    for (int k = 0; k < V; k++) {
        // Iterate over all pairs of vertices
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                // Check if the path through the current vertex is shorter
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    
    // Print the shortest distances
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
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
    int V = 3;
    vector<vector<int>> graph = {{0, 5, 7}, {INF, 0, 3}, {INF, INF, 0}};
    floydWarshall(graph);
    return 0;
}
```

## Test Cases
```
Input: 
0 5 7
INF 0 3
INF INF 0
Output: 
0 5 8 
INF 0 3 
INF INF 0
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle graphs with positive or negative edge weights.
- The algorithm assumes that the graph does not have any negative cycles.
- The time complexity of the Floyd-Warshall algorithm is O(V^3), where V is the number of vertices in the graph.