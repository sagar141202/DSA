# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a graph search algorithm that finds the shortest paths between nodes in a graph. Given a weighted graph and a starting node, the algorithm calculates the minimum distance from the starting node to all other nodes in the graph. The graph can be represented as an adjacency list or adjacency matrix, and the algorithm assumes that all edge weights are non-negative. For example, consider a graph with nodes A, B, C, and D, and edges with weights as follows: A-B (2), A-C (4), B-C (1), B-D (5), C-D (3). If we start at node A, Dijkstra's algorithm will find the shortest path from A to all other nodes.

## Approach
Dijkstra's algorithm uses a greedy approach to find the shortest path by always choosing the node with the minimum distance that has not been visited yet. It maintains a priority queue of nodes to visit, where the priority is the current shortest distance from the starting node to each node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances to its neighbors.

## Complexity
- Time: O((V + E)logV)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for a graph edge
struct Edge {
    int destination;
    int weight;
};

// Define the structure for a graph
struct Graph {
    int numVertices;
    vector<vector<Edge>> adjacencyList;
};

// Function to create a graph
Graph createGraph(int numVertices) {
    Graph graph;
    graph.numVertices = numVertices;
    graph.adjacencyList.resize(numVertices);
    return graph;
}

// Function to add an edge to the graph
void addEdge(Graph& graph, int source, int destination, int weight) {
    Edge edge;
    edge.destination = destination;
    edge.weight = weight;
    graph.adjacencyList[source].push_back(edge);
}

// Function to implement Dijkstra's algorithm
vector<int> dijkstra(Graph& graph, int startNode) {
    // Initialize the distance array with infinity for all nodes
    vector<int> distances(graph.numVertices, INT_MAX);
    distances[startNode] = 0;

    // Create a priority queue to store nodes to visit
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> queue;
    queue.push({0, startNode});

    while (!queue.empty()) {
        int currentNode = queue.top().second;
        int currentDistance = queue.top().first;
        queue.pop();

        // Visit all neighbors of the current node
        for (const auto& edge : graph.adjacencyList[currentNode]) {
            int neighbor = edge.destination;
            int weight = edge.weight;

            // Update the distance to the neighbor if a shorter path is found
            if (currentDistance + weight < distances[neighbor]) {
                distances[neighbor] = currentDistance + weight;
                queue.push({distances[neighbor], neighbor});
            }
        }
    }

    return distances;
}

int main() {
    // Create a sample graph
    Graph graph = createGraph(5);
    addEdge(graph, 0, 1, 2);
    addEdge(graph, 0, 2, 4);
    addEdge(graph, 1, 2, 1);
    addEdge(graph, 1, 3, 5);
    addEdge(graph, 2, 3, 3);

    // Run Dijkstra's algorithm
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
Graph with nodes A, B, C, and D, and edges with weights as follows: A-B (2), A-C (4), B-C (1), B-D (5), C-D (3).
Start node: A

Output: 
Shortest distance from node A to node A: 0
Shortest distance from node A to node B: 2
Shortest distance from node A to node C: 3
Shortest distance from node A to node D: 6
```

## Key Takeaways
- Dijkstra's algorithm is a graph search algorithm that finds the shortest paths between nodes in a graph.
- The algorithm uses a greedy approach to find the shortest path by always choosing the node with the minimum distance that has not been visited yet.
- The time complexity of Dijkstra's algorithm is O((V + E)logV), where V is the number of vertices and E is the number of edges in the graph.