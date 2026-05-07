# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest paths between nodes in a graph. Given a weighted graph and a source node, the algorithm calculates the minimum distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix. The algorithm assumes that the graph does not contain any negative weight edges. For example, in a graph with nodes A, B, C, and D, where the edges have weights as follows: A-B (1), A-C (4), B-C (2), B-D (5), C-D (1), the shortest path from A to D can be found using Dijkstra's algorithm.

## Approach
Dijkstra's algorithm works by maintaining a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighboring nodes. This process continues until all nodes have been processed. The algorithm uses a greedy approach, always choosing the node with the minimum distance that has not been processed yet.

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
    int numVertices;
    vector<vector<Edge>> adjList;
};

// Function to create a graph
Graph createGraph(int numVertices) {
    Graph graph;
    graph.numVertices = numVertices;
    graph.adjList.resize(numVertices);
    return graph;
}

// Function to add an edge to the graph
void addEdge(Graph& graph, int src, int dest, int weight) {
    Edge edge;
    edge.dest = dest;
    edge.weight = weight;
    graph.adjList[src].push_back(edge);
}

// Function to implement Dijkstra's algorithm
void dijkstra(Graph& graph, int src) {
    // Create a vector to store the minimum distances
    vector<int> dist(graph.numVertices, INT_MAX);
    dist[src] = 0;

    // Create a priority queue to store the nodes to be processed
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        int currDist = pq.top().first;
        int currNode = pq.top().second;
        pq.pop();

        // Process all neighbors of the current node
        for (const auto& edge : graph.adjList[currNode]) {
            int neighbor = edge.dest;
            int weight = edge.weight;

            // Update the distance of the neighbor if a shorter path is found
            if (dist[currNode] + weight < dist[neighbor]) {
                dist[neighbor] = dist[currNode] + weight;
                pq.push({dist[neighbor], neighbor});
            }
        }
    }

    // Print the minimum distances
    for (int i = 0; i < graph.numVertices; i++) {
        cout << "Minimum distance from node " << src << " to node " << i << ": " << dist[i] << endl;
    }
}

int main() {
    // Create a graph
    Graph graph = createGraph(5);

    // Add edges to the graph
    addEdge(graph, 0, 1, 1);
    addEdge(graph, 0, 2, 4);
    addEdge(graph, 1, 2, 2);
    addEdge(graph, 1, 3, 5);
    addEdge(graph, 2, 3, 1);

    // Run Dijkstra's algorithm
    dijkstra(graph, 0);

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 nodes and the following edges:
0-1 (1)
0-2 (4)
1-2 (2)
1-3 (5)
2-3 (1)
Source node: 0

Output: 
Minimum distance from node 0 to node 0: 0
Minimum distance from node 0 to node 1: 1
Minimum distance from node 0 to node 2: 3
Minimum distance from node 0 to node 3: 4
Minimum distance from node 0 to node 4: 2147483647
```

## Key Takeaways
- Dijkstra's algorithm is used for finding the shortest paths between nodes in a graph.
- The algorithm assumes that the graph does not contain any negative weight edges.
- The time complexity of Dijkstra's algorithm is O((V + E)logV), where V is the number of vertices and E is the number of edges in the graph.