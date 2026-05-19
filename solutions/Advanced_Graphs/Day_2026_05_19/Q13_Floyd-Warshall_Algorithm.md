# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted graph. Given a graph with n vertices, the algorithm computes the shortest path from vertex i to vertex j for all pairs (i, j). The graph can contain negative weight edges, but it should not contain any negative weight cycles. The algorithm takes as input a 2D matrix representing the adjacency matrix of the graph, where the value at position (i, j) represents the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the value at position (i, j) is typically set to a large value, such as infinity. The algorithm returns a 2D matrix representing the shortest distances between all pairs of vertices.

## Approach
The Floyd-Warshall algorithm works by iteratively improving the estimate of the shortest path between each pair of vertices. It does this by considering each vertex as a potential intermediate step in the path. The algorithm uses dynamic programming to build up the solution, starting with the initial adjacency matrix and iteratively updating the shortest distances.

## Complexity
- Time: O(V^3)
- Space: O(V^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to implement the Floyd-Warshall algorithm
void floydWarshall(vector<vector<int>>& graph) {
    int V = graph.size();
    
    // Create a copy of the input graph
    vector<vector<int>> dist(V, vector<int>(V));
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            dist[i][j] = graph[i][j];
        }
    }
    
    // Iterate over all vertices as potential intermediate steps
    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                // Update the shortest distance if a shorter path is found
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    
    // Print the shortest distances
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
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
    int V = 4;
    vector<vector<int>> graph = {{0, 5, INT_MAX, 10},
                                  {INT_MAX, 0, 3, INT_MAX},
                                  {INT_MAX, INT_MAX, 0, 1},
                                  {INT_MAX, INT_MAX, INT_MAX, 0}};
    
    floydWarshall(graph);
    
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
- The Floyd-Warshall algorithm has a time complexity of O(V^3), making it less efficient than other algorithms like Dijkstra's or Bellman-Ford for finding shortest paths from a single source.
- The algorithm can handle negative weight edges, but it cannot handle negative weight cycles.
- The Floyd-Warshall algorithm returns a 2D matrix representing the shortest distances between all pairs of vertices, making it useful for applications where all-pairs shortest paths are needed.