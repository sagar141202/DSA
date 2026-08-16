# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory for finding the shortest paths between nodes in a graph. Given a weighted graph and a source node, the goal is to find the shortest path from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or adjacency matrix, and the weights can be positive or zero. The algorithm should return the shortest distance from the source node to all other nodes.

## Approach
Dijkstra's algorithm works by maintaining a priority queue of nodes to visit, where the priority is the current shortest distance from the source node to each node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances to its neighbors. The algorithm uses a greedy approach, always choosing the node with the minimum priority, which ensures that the shortest path is found.

## Complexity
- Time: O((V + E)logV)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for a graph edge
struct Edge {
    int dest;
    int weight;
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
void addEdge(Graph& graph, int src, int dest, int weight) {
    Edge edge;
    edge.dest = dest;
    edge.weight = weight;
    graph.adj[src].push_back(edge);
}

// Function to implement Dijkstra's algorithm
void dijkstra(Graph& graph, int src) {
    // Create a vector to store the shortest distances
    vector<int> dist(graph.V, INT_MAX);
    dist[src] = 0;

    // Create a priority queue to store the nodes to visit
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});

    // Loop until the priority queue is empty
    while (!pq.empty()) {
        // Extract the node with the minimum priority from the queue
        int u = pq.top().second;
        pq.pop();

        // Loop through all the neighbors of the current node
        for (const auto& edge : graph.adj[u]) {
            int v = edge.dest;
            int weight = edge.weight;

            // If the distance to the neighbor can be reduced, update the distance and push it to the queue
            if (dist[v] > dist[u] + weight) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    // Print the shortest distances
    cout << "Node\tDistance from Source" << endl;
    for (int i = 0; i < graph.V; i++) {
        cout << i << "\t" << dist[i] << endl;
    }
}

int main() {
    // Create a graph
    Graph graph = createGraph(6);

    // Add edges to the graph
    addEdge(graph, 0, 1, 4);
    addEdge(graph, 0, 2, 2);
    addEdge(graph, 1, 3, 5);
    addEdge(graph, 2, 1, 1);
    addEdge(graph, 2, 3, 8);
    addEdge(graph, 2, 4, 10);
    addEdge(graph, 3, 4, 2);
    addEdge(graph, 3, 5, 6);
    addEdge(graph, 4, 5, 3);

    // Run Dijkstra's algorithm
    dijkstra(graph, 0);

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 6 nodes and the following edges:
0 -> 1 (weight 4)
0 -> 2 (weight 2)
1 -> 3 (weight 5)
2 -> 1 (weight 1)
2 -> 3 (weight 8)
2 -> 4 (weight 10)
3 -> 4 (weight 2)
3 -> 5 (weight 6)
4 -> 5 (weight 3)
Source node: 0

Output: 
Node Distance from Source
0   0
1   3
2   2
3   8
4   10
5   13
```

## Key Takeaways
- Dijkstra's algorithm is a greedy algorithm that works by maintaining a priority queue of nodes to visit.
- The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances to its neighbors.
- The time complexity of Dijkstra's algorithm is O((V + E)logV) using a binary heap, where V is the number of vertices and E is the number of edges.