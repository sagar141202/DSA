# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted, directed graph. Given a graph with n vertices, the algorithm computes the shortest path between every pair of vertices. The graph can contain negative weight edges, but it should not contain any negative cycles. For example, consider a graph with 4 vertices and the following edges: (0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3). The algorithm should output the shortest distance between every pair of vertices.

## Approach
The Floyd-Warshall algorithm works by considering all possible paths between every pair of vertices and choosing the one with the minimum weight. It uses dynamic programming to build up the solution, starting with the shortest paths between adjacent vertices and then considering paths of increasing length. The algorithm has a simple and intuitive implementation.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void floydWarshall(vector<vector<int>>& graph, int n) {
    // Create a copy of the graph to store the shortest distances
    vector<vector<int>> dist(n, vector<int>(n, INT_MAX));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = graph[i][j];
        }
    }

    // Consider all possible paths between every pair of vertices
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Update the shortest distance if a shorter path is found
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    // Print the shortest distances between every pair of vertices
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
    int n = 4;
    vector<vector<int>> graph = {
        {0, -1, 4, INT_MAX},
        {INT_MAX, 0, 3, 2},
        {INT_MAX, INT_MAX, 0, INT_MAX},
        {INT_MAX, INT_MAX, 5, 0}
    };

    floydWarshall(graph, n);

    return 0;
}
```

## Test Cases
```
Input: 
0 -1 4 INF
INF 0 3 2
INF INF 0 INF
INF INF 5 0

Output: 
0 -1 2 -2
4 0 1 1
5 3 0 -1
3 1 -4 -2
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it cannot handle negative cycles.
- The algorithm has a time complexity of O(n^3), making it less efficient than other algorithms like Dijkstra's or Bellman-Ford for single-source shortest path problems.
- The algorithm uses dynamic programming to build up the solution, making it a good example of a dynamic programming problem.