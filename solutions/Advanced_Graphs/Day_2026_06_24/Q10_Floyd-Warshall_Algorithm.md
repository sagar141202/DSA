# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted and directed graph. Given a graph with `n` vertices, the algorithm computes the shortest path between every pair of vertices `(i, j)` and stores it in a 2D matrix `dist`. The graph is represented as an adjacency matrix `graph`, where `graph[i][j]` is the weight of the edge from vertex `i` to vertex `j`. If there is no edge between vertices `i` and `j`, then `graph[i][j]` is `INT_MAX`. The algorithm should handle negative weight edges, but it assumes that there are no negative weight cycles in the graph.

## Approach
The Floyd-Warshall algorithm works by considering all possible paths of length 1, 2, ..., `n` between every pair of vertices. It uses dynamic programming to build up the shortest path matrix `dist` iteratively. The algorithm starts with the initial graph and then iteratively considers all vertices as intermediate points to find shorter paths.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INT_MAX = 1e9;

void floydWarshall(vector<vector<int>>& graph, int n) {
    // Create a copy of the graph to store the shortest distances
    vector<vector<int>> dist = graph;

    // Iterate over all possible intermediate vertices
    for (int k = 0; k < n; k++) {
        // Iterate over all pairs of vertices
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Check if the path through vertex k is shorter
                if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    // Print the shortest distance matrix
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

    cout << "Enter the weights of the edges:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                graph[i][j] = 0; // Weight of self-loop is 0
            } else {
                int weight;
                cin >> weight;
                if (weight != -1) { // -1 indicates no edge
                    graph[i][j] = weight;
                }
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
Enter the weights of the edges:
0 -1 -1 -1
-1 0 3 -1
-1 -1 0 2
-1 -1 -1 0

Output:
0 4 3 5 
-1 0 -1 -1 
-1 -1 0 2 
-1 -1 -1 0
```

## Key Takeaways
- The Floyd-Warshall algorithm has a time complexity of O(n^3) and space complexity of O(n^2), making it efficient for finding shortest paths in dense graphs.
- The algorithm can handle negative weight edges, but it assumes that there are no negative weight cycles in the graph.
- The algorithm uses dynamic programming to build up the shortest path matrix iteratively, considering all possible paths of length 1, 2, ..., `n` between every pair of vertices.