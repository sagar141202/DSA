# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest paths between nodes in a graph. Given a weighted graph and a starting node (also called the source node), the algorithm calculates the shortest distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix, and the algorithm assumes that all edge weights are non-negative. For example, in a graph with nodes A, B, C, and D, where the edges have weights as follows: A-B (1), A-C (4), B-C (2), B-D (5), C-D (1), the shortest distance from node A to all other nodes can be calculated using Dijkstra's algorithm.

## Approach
Dijkstra's algorithm works by maintaining a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighbors. This process continues until the queue is empty, at which point the algorithm has calculated the shortest distances from the source node to all other nodes.

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
    int numNodes;
    vector<vector<Edge>> adjList;
};

// Function to create a graph
Graph createGraph(int numNodes) {
    Graph graph;
    graph.numNodes = numNodes;
    graph.adjList.resize(numNodes);
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
    vector<int> distances(graph.numNodes, INT_MAX);
    distances[src] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        int currNode = pq.top().second;
        int currDist = pq.top().first;
        pq.pop();

        for (const auto& edge : graph.adjList[currNode]) {
            int neighbor = edge.dest;
            int weight = edge.weight;

            if (currDist + weight < distances[neighbor]) {
                distances[neighbor] = currDist + weight;
                pq.push({distances[neighbor], neighbor});
            }
        }
    }

    return distances;
}

int main() {
    // Create a graph with 5 nodes
    Graph graph = createGraph(5);

    // Add edges to the graph
    addEdge(graph, 0, 1, 1);
    addEdge(graph, 0, 2, 4);
    addEdge(graph, 1, 2, 2);
    addEdge(graph, 1, 3, 5);
    addEdge(graph, 2, 3, 1);

    // Calculate the shortest distances from node 0
    vector<int> distances = dijkstra(graph, 0);

    // Print the shortest distances
    for (int i = 0; i < distances.size(); i++) {
        cout << "Shortest distance from node 0 to node " << i << ": " << distances[i] << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with nodes A, B, C, D, and edges A-B (1), A-C (4), B-C (2), B-D (5), C-D (1)
Source node: A
Output: 
Shortest distance from node A to node A: 0
Shortest distance from node A to node B: 1
Shortest distance from node A to node C: 3
Shortest distance from node A to node D: 4
```

## Key Takeaways
- Dijkstra's algorithm is used for finding the shortest paths between nodes in a weighted graph.
- The algorithm assumes that all edge weights are non-negative.
- The time complexity of Dijkstra's algorithm is O((V + E)logV), where V is the number of nodes and E is the number of edges in the graph.