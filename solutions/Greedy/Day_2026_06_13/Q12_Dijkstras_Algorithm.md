# Dijkstra's Algorithm

## Problem Statement
Given a weighted graph and a source vertex, find the shortest path between the source vertex and all other vertices in the graph. The graph is represented as an adjacency list, where each vertex is connected to its neighboring vertices with a certain weight. The goal is to find the minimum-weight path from the source vertex to all other vertices. For example, in a graph with vertices {A, B, C, D} and edges {(A, B, 1), (A, C, 4), (B, C, 2), (B, D, 5), (C, D, 1)}, the shortest path from vertex A to all other vertices is {A: 0, B: 1, C: 3, D: 4}.

## Approach
Dijkstra's algorithm uses a greedy approach to find the shortest path by maintaining a priority queue of vertices to be processed, where the priority of each vertex is its minimum distance from the source vertex. The algorithm iteratively extracts the vertex with the minimum distance from the priority queue and updates the distances of its neighboring vertices. This process continues until all vertices have been processed.

## Complexity
- Time: O((V + E)logV)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<pii> vii;
typedef vector<vii> graph;

void dijkstra(graph &g, int src) {
    int V = g.size();
    vector<int> dist(V, INT_MAX);
    dist[src] = 0;
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        for (auto &v : g[u]) {
            int vertex = v.first;
            int weight = v.second;
            if (dist[vertex] > dist[u] + weight) {
                dist[vertex] = dist[u] + weight;
                pq.push({dist[vertex], vertex});
            }
        }
    }

    cout << "Vertex \tDistance from Source" << endl;
    for (int i = 0; i < V; i++) {
        cout << i << "\t" << dist[i] << endl;
    }
}

int main() {
    int V = 5;
    graph g(V);
    g[0].push_back({1, 1});
    g[0].push_back({2, 4});
    g[1].push_back({2, 2});
    g[1].push_back({3, 5});
    g[2].push_back({3, 1});
    g[2].push_back({4, 8});
    g[3].push_back({4, 3});

    dijkstra(g, 0);

    return 0;
}
```

## Test Cases
```
Input: 
Graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1, 1), (0, 2, 4), (1, 2, 2), (1, 3, 5), (2, 3, 1), (2, 4, 8), (3, 4, 3)}
Source vertex: 0
Output: 
Vertex 	Distance from Source
0 		0
1 		1
2 		3
3 		4
4 		7
```

## Key Takeaways
- Dijkstra's algorithm is a greedy algorithm that uses a priority queue to find the shortest path from a source vertex to all other vertices in a weighted graph.
- The algorithm has a time complexity of O((V + E)logV) and a space complexity of O(V + E), where V is the number of vertices and E is the number of edges in the graph.
- Dijkstra's algorithm can be used in a variety of applications, including network routing, traffic management, and logistics.