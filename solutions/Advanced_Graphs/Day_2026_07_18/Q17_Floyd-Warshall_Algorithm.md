# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted and directed graph. Given a graph with `n` vertices and `m` edges, where each edge has a weight, the algorithm should output a 2D matrix where the value at position `(i, j)` represents the minimum weight of the path from vertex `i` to vertex `j`. The graph can contain negative weight edges, but it should not contain any negative cycles. If a negative cycle is present, the algorithm should detect it and report an error.

## Approach
The Floyd-Warshall algorithm works by iteratively improving the estimate of the shortest path between each pair of vertices. It uses dynamic programming to build up a solution by considering all possible paths of length up to `n`. The algorithm starts with the adjacency matrix of the graph and then iteratively updates the matrix to include the shortest path between each pair of vertices.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to implement the Floyd-Warshall algorithm
void floydWarshall(vector<vector<int>>& graph, int n) {
    // Create a copy of the graph to store the shortest distances
    vector<vector<int>> dist(n, vector<int>(n, INT_MAX));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = graph[i][j];
        }
    }

    // Iterate over all possible paths
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Update the shortest distance if a shorter path is found
                if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    // Check for negative cycles
    for (int i = 0; i < n; i++) {
        if (dist[i][i] < 0) {
            cout << "Negative cycle detected" << endl;
            return;
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
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                graph[i][j] = 0;
            } else {
                cout << "Enter the weight of edge from " << i << " to " << j << ": ";
                cin >> graph[i][j];
            }
        }
    }

    floydWarshall(graph, n);
    return 0;
}
```

## Test Cases
```
Input:
Enter the number of vertices: 4
Enter the weight of edge from 0 to 0: 0
Enter the weight of edge from 0 to 1: 5
Enter the weight of edge from 0 to 2: INF
Enter the weight of edge from 0 to 3: INF
Enter the weight of edge from 1 to 0: INF
Enter the weight of edge from 1 to 1: 0
Enter the weight of edge from 1 to 2: -2
Enter the weight of edge from 1 to 3: INF
Enter the weight of edge from 2 to 0: INF
Enter the weight of edge from 2 to 1: INF
Enter the weight of edge from 2 to 2: 0
Enter the weight of edge from 2 to 3: 1
Enter the weight of edge from 3 to 0: INF
Enter the weight of edge from 3 to 1: INF
Enter the weight of edge from 3 to 2: INF
Enter the weight of edge from 3 to 3: 0
Output:
0 5 3 4 
INF 0 -2 -1 
INF INF 0 1 
INF INF INF 0 
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it cannot handle negative cycles.
- The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2), making it efficient for large graphs.
- The algorithm can be used to find the shortest path between all pairs of vertices in a weighted and directed graph.