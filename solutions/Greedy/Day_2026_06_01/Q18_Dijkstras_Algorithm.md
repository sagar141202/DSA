# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory for finding the shortest paths between nodes in a graph. It works with weighted graphs, where each edge has a weight or cost associated with it. The goal is to find the minimum-weight path from a single source node to all other nodes in the graph. The algorithm assumes that the graph does not contain any negative-weight edges.

## Approach
Dijkstra's algorithm uses a greedy approach, where it always chooses the next node with the shortest distance from the source node that has not been visited yet. The algorithm maintains a priority queue of nodes, where the priority of each node is its current shortest distance from the source node.

## Complexity
- Time: O((V + E)logV)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for a graph edge
struct Edge {
    int dest, weight;
};

// Define the structure for a graph
struct Graph {
    int V;
    vector<vector<Edge>> adj;
};

// Function to create a graph
Graph createGraph(int V) {
    Graph graph;
    graph.V = V;
    graph.adj.resize(V);
    return graph;
}

// Function to add an edge to the graph
void addEdge(Graph &graph, int src, int dest, int weight) {
    Edge edge = {dest, weight};
    graph.adj[src].push_back(edge);
}

// Function to implement Dijkstra's algorithm
void dijkstra(Graph &graph, int src) {
    // Create a vector to store the shortest distances
    vector<int> dist(graph.V, INT_MAX);
    dist[src] = 0;

    // Create a priority queue to store the nodes to be processed
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        // Process all the adjacent vertices of u
        for (Edge edge : graph.adj[u]) {
            int v = edge.dest;
            int weight = edge.weight;

            // If a shorter path is found, update the distance and push it to the priority queue
            if (dist[v] > dist[u] + weight) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    // Print the shortest distances
    cout << "Vertex \tDistance from Source" << endl;
    for (int i = 0; i < graph.V; i++) {
        cout << i << "\t" << dist[i] << endl;
    }
}

int main() {
    int V = 6;
    Graph graph = createGraph(V);

    addEdge(graph, 0, 1, 4);
    addEdge(graph, 0, 2, 2);
    addEdge(graph, 1, 3, 5);
    addEdge(graph, 2, 1, 1);
    addEdge(graph, 2, 3, 8);
    addEdge(graph, 2, 4, 10);
    addEdge(graph, 3, 4, 2);
    addEdge(graph, 3, 5, 6);
    addEdge(graph, 4, 5, 3);

    dijkstra(graph, 0);

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 6 vertices and the following edges:
(0, 1) with weight 4
(0, 2) with weight 2
(1, 3) with weight 5
(2, 1) with weight 1
(2, 3) with weight 8
(2, 4) with weight 10
(3, 4) with weight 2
(3, 5) with weight 6
(4, 5) with weight 3
Source vertex: 0

Output: 
Vertex  Distance from Source
0       0
1       3
2       2
3       8
4       10
5       13
```

## Key Takeaways
- Dijkstra's algorithm is used to find the shortest paths from a single source node to all other nodes in a weighted graph.
- The algorithm uses a greedy approach, where it always chooses the next node with the shortest distance from the source node that has not been visited yet.
- The algorithm has a time complexity of O((V + E)logV) and a space complexity of O(V + E), where V is the number of vertices and E is the number of edges in the graph.