# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights. Given a graph with n vertices, the algorithm finds the shortest path between all pairs of vertices. The graph can have negative weight edges, but it should not have any negative cycles. The algorithm takes as input a 2D matrix representing the adjacency matrix of the graph, where the value at index [i][j] represents the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the value is typically represented as infinity.

## Approach
The Floyd-Warshall algorithm works by considering all possible paths between each pair of vertices. It starts by assuming that the shortest path between two vertices is the direct edge between them, and then iteratively updates the shortest path by considering all possible intermediate vertices. The algorithm uses dynamic programming to efficiently compute the shortest paths.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void floydWarshall(vector<vector<int>>& graph) {
    int n = graph.size();
    // Create a copy of the input graph to store the shortest distances
    vector<vector<int>> dist(n, vector<int>(n));
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
}

int main() {
    int n;
    cout << "Enter the number of vertices: ";
    cin >> n;
    vector<vector<int>> graph(n, vector<int>(n, INT_MAX));
    cout << "Enter the adjacency matrix:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> graph[i][j];
            if (i == j) {
                graph[i][j] = 0;
            }
        }
    }
    floydWarshall(graph);
    return 0;
}
```

## Test Cases
```
Input:
Enter the number of vertices: 4
Enter the adjacency matrix:
0 5 999 10
999 0 3 999
999 999 0 1
999 999 999 0
Output:
0 5 8 9 
999 0 3 4 
999 999 0 1 
999 999 999 0 
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it cannot handle negative cycles.
- The algorithm has a time complexity of O(n^3), where n is the number of vertices in the graph.
- The algorithm uses dynamic programming to efficiently compute the shortest paths between all pairs of vertices.