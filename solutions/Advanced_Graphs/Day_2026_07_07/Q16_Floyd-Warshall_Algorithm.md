# Floyd-Warshall Algorithm

## Problem Statement
The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights. Given a graph with `n` vertices, the algorithm computes the shortest path between all pairs of vertices. The graph is represented as an adjacency matrix `dist`, where `dist[i][j]` is the weight of the edge from vertex `i` to vertex `j`. If there is no edge between vertices `i` and `j`, then `dist[i][j]` is infinity. The algorithm can handle negative weight edges, but it assumes that there are no negative weight cycles in the graph.

## Approach
The Floyd-Warshall algorithm uses dynamic programming to find the shortest paths between all pairs of vertices. It works by considering each vertex as an intermediate step in the path. The algorithm iterates over all vertices and for each vertex, it checks if the path from vertex `i` to vertex `j` can be shortened by going through vertex `k`.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = INT_MAX;

void floydWarshall(int** dist, int n) {
    // Iterate over all vertices
    for (int k = 0; k < n; k++) {
        // Iterate over all pairs of vertices
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Check if the path from vertex i to vertex j can be shortened by going through vertex k
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
}

int main() {
    int n;
    cout << "Enter the number of vertices: ";
    cin >> n;

    int** dist = new int*[n];
    for (int i = 0; i < n; i++) {
        dist[i] = new int[n];
        for (int j = 0; j < n; j++) {
            cout << "Enter the weight of the edge from vertex " << i << " to vertex " << j << ": ";
            cin >> dist[i][j];
            if (dist[i][j] == -1) {
                dist[i][j] = INF;
            }
        }
    }

    floydWarshall(dist, n);

    cout << "Shortest distances between all pairs of vertices:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (dist[i][j] == INF) {
                cout << "-1 ";
            } else {
                cout << dist[i][j] << " ";
            }
        }
        cout << endl;
    }

    return 0;
}
```

## Test Cases
```
Input:
Enter the number of vertices: 4
Enter the weight of the edge from vertex 0 to vertex 0: 0
Enter the weight of the edge from vertex 0 to vertex 1: -1
Enter the weight of the edge from vertex 0 to vertex 2: 5
Enter the weight of the edge from vertex 0 to vertex 3: 10
Enter the weight of the edge from vertex 1 to vertex 0: 2
Enter the weight of the edge from vertex 1 to vertex 1: 0
Enter the weight of the edge from vertex 1 to vertex 2: 3
Enter the weight of the edge from vertex 1 to vertex 3: -1
Enter the weight of the edge from vertex 2 to vertex 0: -1
Enter the weight of the edge from vertex 2 to vertex 1: -1
Enter the weight of the edge from vertex 2 to vertex 2: 0
Enter the weight of the edge from vertex 2 to vertex 3: 1
Enter the weight of the edge from vertex 3 to vertex 0: -1
Enter the weight of the edge from vertex 3 to vertex 1: -1
Enter the weight of the edge from vertex 3 to vertex 2: -1
Enter the weight of the edge from vertex 3 to vertex 3: 0
Output:
Shortest distances between all pairs of vertices:
0 2 5 6 
2 0 3 4 
-1 -1 0 1 
-1 -1 -1 0 
```

## Key Takeaways
- The Floyd-Warshall algorithm can handle negative weight edges, but it assumes that there are no negative weight cycles in the graph.
- The algorithm has a time complexity of O(n^3) and a space complexity of O(n^2), where n is the number of vertices in the graph.
- The algorithm can be used to find the shortest paths between all pairs of vertices in a weighted graph.