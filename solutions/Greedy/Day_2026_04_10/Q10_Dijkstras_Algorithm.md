# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest paths between nodes in a graph. Given a weighted graph and a source node, the algorithm aims to find the shortest path from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or adjacency matrix, and the algorithm should handle both positive and negative weight edges. However, if the graph contains a negative cycle (a cycle whose total weight is negative), the algorithm may not work correctly. The goal is to implement Dijkstra's algorithm to find the shortest distances from a given source node to all other nodes in the graph.

## Approach
Dijkstra's algorithm works by maintaining a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighbors. The algorithm uses a greedy approach, always choosing the node with the minimum distance that has not been processed yet.

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

    // Create a priority queue to store nodes to be processed
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        int currNode = pq.top().second;
        int currDist = pq.top().first;
        pq.pop();

        // Process all neighbors of the current node
        for (const Edge& edge : graph.adjList[currNode]) {
            int neighbor = edge.dest;
            int weight = edge.weight;

            // Update the distance of the neighbor if a shorter path is found
            if (currDist + weight < distances[neighbor]) {
                distances[neighbor] = currDist + weight;
                pq.push({distances[neighbor], neighbor});
            }
        }
    }

    return distances;
}

int main() {
    // Create a sample graph
    Graph graph = createGraph(5);
    addEdge(graph, 0, 1, 4);
    addEdge(graph, 0, 2, 1);
    addEdge(graph, 1, 3, 1);
    addEdge(graph, 2, 1, 2);
    addEdge(graph, 2, 3, 5);
    addEdge(graph, 3, 4, 3);

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
Graph with 5 nodes and 6 edges:
0 -> 1 (weight: 4)
0 -> 2 (weight: 1)
1 -> 3 (weight: 1)
2 -> 1 (weight: 2)
2 -> 3 (weight: 5)
3 -> 4 (weight: 3)
Source node: 0

Output: 
Shortest distance from node 0 to node 0: 0
Shortest distance from node 0 to node 1: 3
Shortest distance from node 0 to node 2: 1
Shortest distance from node 0 to node 3: 4
Shortest distance from node 0 to node 4: 7
```

## Key Takeaways
- Dijkstra's algorithm uses a greedy approach to find the shortest paths from a source node to all other nodes in a graph.
- The algorithm maintains a priority queue of nodes, where the priority of each node is its minimum distance from the source node.
- The algorithm has a time complexity of O((V + E)logV) and a space complexity of O(V + E), making it efficient for large graphs.