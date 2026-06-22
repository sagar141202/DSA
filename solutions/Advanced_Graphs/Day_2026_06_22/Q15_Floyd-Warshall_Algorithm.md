# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted and directed graph. The graph can contain negative weight edges, but it should not have any negative cycles. The algorithm takes as input a graph represented as an adjacency matrix, where the value at index [i][j] represents the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the value at index [i][j] is typically set to infinity. The algorithm outputs a new adjacency matrix where the value at index [i][j] represents the minimum weight of the path from vertex i to vertex j.

## Approach
The Floyd-Warshall algorithm works by iteratively considering each vertex and updating the shortest path between all pairs of vertices. It uses dynamic programming to build up the solution. The algorithm starts with the initial adjacency matrix and then iterates over each vertex, updating the shortest path between all pairs of vertices that pass through the current vertex. The algorithm runs in O(V^3) time, where V is the number of vertices in the graph.

## Complexity
- Time: O(V^3)
- Space: O(V^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void floydWarshall(vector<vector<int>>& graph) {
    int V = graph.size();
    // Create a copy of the graph to store the shortest distances
    vector<vector<int>> dist(V, vector<int>(V));
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            dist[i][j] = graph[i][j];
        }
    }

    // Iterate over each vertex
    for (int k = 0; k < V; k++) {
        // Iterate over each pair of vertices
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
- The Floyd-Warshall algorithm can handle negative weight edges, but it cannot handle negative cycles.
- The algorithm has a time complexity of O(V^3) and a space complexity of O(V^2), making it suitable for large graphs.
- The algorithm can be used to find the shortest path between all pairs of vertices in a weighted and directed graph.