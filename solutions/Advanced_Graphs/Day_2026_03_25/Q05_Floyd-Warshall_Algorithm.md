# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights. Given a graph with n vertices, the algorithm computes the shortest path between all pairs of vertices. The graph can be represented as an adjacency matrix, where the entry at row i and column j represents the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the weight is considered to be infinity. The algorithm can handle negative weight edges, but it assumes that there are no negative cycles in the graph. A negative cycle is a cycle whose total weight is negative.

## Approach
The Floyd-Warshall algorithm works by iteratively improving the estimate of the shortest path between each pair of vertices. It does this by considering all possible intermediate vertices and checking if the path through the intermediate vertex is shorter than the current shortest path. The algorithm uses dynamic programming to build up a solution to the problem.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to implement the Floyd-Warshall algorithm
void floydWarshall(vector<vector<int>>& graph) {
    int n = graph.size();
    
    // Create a copy of the graph to store the shortest distances
    vector<vector<int>> dist(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = graph[i][j];
        }
    }
    
    // Iterate over all intermediate vertices
    for (int k = 0; k < n; k++) {
        // Iterate over all pairs of vertices
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Check if the path through the intermediate vertex is shorter
                if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
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
    cout << "Enter the weights of the edges:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                graph[i][j] = 0;
            } else {
                cin >> graph[i][j];
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
Enter the weights of the edges:
0 5 10 15
5 0 3 8
10 3 0 2
15 8 2 0

Output:
0 5 8 10
5 0 3 5
8 3 0 2
10 8 2 0
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it assumes that there are no negative cycles in the graph.
- The algorithm uses dynamic programming to build up a solution to the problem.
- The time complexity of the algorithm is O(n^3), where n is the number of vertices in the graph.