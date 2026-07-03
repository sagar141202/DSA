# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest paths between nodes in a graph. Given a weighted graph and a source node, the algorithm calculates the minimum distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix. The algorithm assumes that the graph does not contain any negative-weight edges. The goal is to find the shortest distance from the source node to all other nodes and to construct the shortest path from the source node to each node.

## Approach
Dijkstra's algorithm works by maintaining a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm iteratively extracts the node with the minimum priority from the queue, updates the distances of its neighbors, and adds them to the queue if necessary. This process continues until the queue is empty, at which point the algorithm has calculated the shortest distances from the source node to all other nodes.

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

// Function to create a graph with V vertices
Graph createGraph(int V) {
    Graph graph;
    graph.V = V;
    graph.adj.resize(V);
    return graph;
}

// Function to add an edge to the graph
void addEdge(Graph& graph, int src, int dest, int weight) {
    Edge edge = {dest, weight};
    graph.adj[src].push_back(edge);
}

// Function to implement Dijkstra's algorithm
void dijkstra(Graph& graph, int src) {
    // Create a vector to store the shortest distances
    vector<int> dist(graph.V, INT_MAX);
    dist[src] = 0;

    // Create a priority queue to store the nodes to be processed
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});

    // Create a vector to store the previous node in the shortest path
    vector<int> prev(graph.V, -1);

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        // Iterate over all the neighbors of the current node
        for (const auto& edge : graph.adj[u]) {
            int v = edge.dest;
            int weight = edge.weight;

            // If the distance to the neighbor can be reduced, update it
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                prev[v] = u;
                pq.push({dist[v], v});
            }
        }
    }

    // Print the shortest distances and paths
    for (int i = 0; i < graph.V; i++) {
        cout << "Shortest distance from node " << src << " to node " << i << ": " << dist[i] << endl;
        cout << "Shortest path from node " << src << " to node " << i << ": ";
        vector<int> path;
        int u = i;
        while (u != -1) {
            path.push_back(u);
            u = prev[u];
        }
        reverse(path.begin(), path.end());
        for (int node : path) {
            cout << node << " ";
        }
        cout << endl;
    }
}

// Example usage
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
Source node: 0

Output:
Shortest distance from node 0 to node 0: 0
Shortest path from node 0 to node 0: 0
Shortest distance from node 0 to node 1: 3
Shortest path from node 0 to node 1: 0 2 1
Shortest distance from node 0 to node 2: 2
Shortest path from node 0 to node 2: 0 2
Shortest distance from node 0 to node 3: 8
Shortest path from node 0 to node 3: 0 2 1 3
Shortest distance from node 0 to node 4: 10
Shortest path from node 0 to node 4: 0 2 1 3 4
Shortest distance from node 0 to node 5: 13
Shortest path from node 0 to node 5: 0 2 1 3 4 5
```

## Key Takeaways
- Dijkstra's algorithm can be used to find the shortest paths between nodes in a weighted graph.
- The algorithm assumes that the graph does not contain any negative-weight edges.
- The time complexity of Dijkstra's algorithm is O((V + E)logV), where V is the number of vertices and E is the number of edges.
- The space complexity of Dijkstra's algorithm is O(V + E), where V is the number of vertices and E is the number of edges.