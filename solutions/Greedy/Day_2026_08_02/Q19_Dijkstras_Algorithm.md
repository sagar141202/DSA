# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest paths between nodes in a graph. The problem statement is as follows: given a weighted graph and a source node, find the shortest distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or adjacency matrix, and the weights can be positive or zero. The algorithm should be able to handle graphs with multiple connected components.

## Approach
Dijkstra's algorithm works by maintaining a priority queue of nodes to visit, where the priority is the current shortest distance from the source node to each node. The algorithm iteratively extracts the node with the minimum priority from the queue, updates the distances to its neighbors, and inserts them into the queue if necessary.

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
vector<int> dijkstra(Graph& graph, int src) {
    vector<int> dist(graph.numVertices, INT_MAX);
    dist[src] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        for (const auto& edge : graph.adjList[u]) {
            int v = edge.dest;
            int weight = edge.weight;

            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    return dist;
}

int main() {
    int numVertices = 5;
    Graph graph = createGraph(numVertices);

    addEdge(graph, 0, 1, 4);
    addEdge(graph, 0, 2, 1);
    addEdge(graph, 1, 3, 1);
    addEdge(graph, 2, 1, 2);
    addEdge(graph, 2, 3, 5);
    addEdge(graph, 3, 4, 3);

    int src = 0;
    vector<int> dist = dijkstra(graph, src);

    cout << "Shortest distances from node " << src << ": ";
    for (int i = 0; i < numVertices; i++) {
        cout << dist[i] << " ";
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and edges:
(0, 1) with weight 4
(0, 2) with weight 1
(1, 3) with weight 1
(2, 1) with weight 2
(2, 3) with weight 5
(3, 4) with weight 3
Source node: 0

Output: 
Shortest distances from node 0: 0 3 1 4 7
```

## Key Takeaways
- Dijkstra's algorithm is used for finding the shortest paths in a weighted graph.
- The algorithm uses a priority queue to keep track of the nodes to visit, where the priority is the current shortest distance from the source node.
- The time complexity of Dijkstra's algorithm is O((V + E)logV), where V is the number of vertices and E is the number of edges in the graph.