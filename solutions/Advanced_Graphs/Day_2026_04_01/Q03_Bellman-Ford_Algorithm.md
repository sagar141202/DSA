# Bellman-Ford Algorithm

## Problem Statement
The Bellman-Ford algorithm is used to find the shortest path from a source vertex to all other vertices in a weighted graph. It can handle negative weight edges, and can detect negative weight cycles. The algorithm takes as input a graph with V vertices and E edges, and a source vertex s. It outputs the shortest distance from s to all other vertices, or reports if a negative weight cycle is detected. For example, given a graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)}, the shortest distance from vertex 0 to all other vertices is {0, -1, 2, -2, 1}.

## Approach
The Bellman-Ford algorithm works by relaxing all edges V-1 times, where V is the number of vertices. After V-1 relaxations, the shortest distance to all vertices is calculated. Then, one more relaxation is done to check for negative weight cycles. If any distance is reduced in this last relaxation, then a negative weight cycle is detected.

## Complexity
- Time: O(VE)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Graph {
    int V;
    vector<vector<int>> graph;

public:
    Graph(int vertices) {
        V = vertices;
        graph.resize(vertices);
    }

    void addEdge(int u, int v, int w) {
        graph[u].push_back(v);
        graph[u].push_back(w);
    }

    void bellmanFord(int src) {
        vector<int> dist(V, INT_MAX);
        dist[src] = 0;

        for (int i = 0; i < V - 1; i++) {
            for (int u = 0; u < V; u++) {
                for (int j = 0; j < graph[u].size(); j += 2) {
                    int v = graph[u][j];
                    int w = graph[u][j + 1];
                    if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                    }
                }
            }
        }

        for (int u = 0; u < V; u++) {
            for (int j = 0; j < graph[u].size(); j += 2) {
                int v = graph[u][j];
                int w = graph[u][j + 1];
                if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                    cout << "Negative weight cycle detected" << endl;
                    return;
                }
            }
        }

        cout << "Vertex \tDistance from Source" << endl;
        for (int i = 0; i < V; i++) {
            cout << i << "\t" << dist[i] << endl;
        }
    }
};

int main() {
    Graph g(5);
    g.addEdge(0, 1, -1);
    g.addEdge(0, 2, 4);
    g.addEdge(1, 2, 3);
    g.addEdge(1, 3, 2);
    g.addEdge(1, 4, 2);
    g.addEdge(3, 2, 5);
    g.addEdge(3, 1, 1);
    g.addEdge(4, 3, -3);
    g.bellmanFord(0);
    return 0;
}
```

## Test Cases
```
Input: 
Graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)}
Output: 
Vertex 	Distance from Source
0 		0
1 		-1
2 		2
3 		-2
4 		1
```

## Key Takeaways
- The Bellman-Ford algorithm can handle negative weight edges and detect negative weight cycles.
- It has a time complexity of O(VE) and a space complexity of O(V).
- The algorithm can be used to find the shortest path from a source vertex to all other vertices in a weighted graph.