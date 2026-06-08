# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest path between nodes in a graph. Given a weighted graph and a starting node (also called the source node), the algorithm calculates the shortest distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or adjacency matrix. The algorithm assumes that the graph does not contain any negative weight edges. The goal is to find the minimum distance from the source node to all other nodes and to construct the shortest path.

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

// Define the structure for a graph node
struct Node {
    int id;
    int distance;
};

// Comparison function for the priority queue
struct compare {
    bool operator()(const Node& a, const Node& b) {
        return a.distance > b.distance;
    }
};

// Function to implement Dijkstra's algorithm
void dijkstra(vector<vector<Edge>>& graph, int source) {
    int numNodes = graph.size();
    vector<int> distances(numNodes, INT_MAX);
    vector<bool> visited(numNodes, false);
    priority_queue<Node, vector<Node>, compare> pq;

    // Initialize the distance of the source node to 0
    distances[source] = 0;
    pq.push({source, 0});

    while (!pq.empty()) {
        // Extract the node with the minimum distance from the priority queue
        Node currentNode = pq.top();
        pq.pop();

        // If the node has already been visited, skip it
        if (visited[currentNode.id]) {
            continue;
        }

        // Mark the node as visited
        visited[currentNode.id] = true;

        // Update the distances of the node's neighbors
        for (const Edge& edge : graph[currentNode.id]) {
            int neighbor = edge.dest;
            int weight = edge.weight;
            int newDistance = distances[currentNode.id] + weight;

            if (newDistance < distances[neighbor]) {
                distances[neighbor] = newDistance;
                pq.push({neighbor, newDistance});
            }
        }
    }

    // Print the shortest distances from the source node to all other nodes
    for (int i = 0; i < numNodes; i++) {
        cout << "Shortest distance from source node " << source << " to node " << i << ": " << distances[i] << endl;
    }
}

int main() {
    int numNodes = 5;
    vector<vector<Edge>> graph(numNodes);

    // Add edges to the graph
    graph[0].push_back({1, 4});
    graph[0].push_back({2, 1});
    graph[1].push_back({3, 1});
    graph[2].push_back({1, 2});
    graph[2].push_back({3, 5});
    graph[3].push_back({4, 3});

    int sourceNode = 0;
    dijkstra(graph, sourceNode);

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 nodes and the following edges:
- Node 0 to node 1 with weight 4
- Node 0 to node 2 with weight 1
- Node 1 to node 3 with weight 1
- Node 2 to node 1 with weight 2
- Node 2 to node 3 with weight 5
- Node 3 to node 4 with weight 3
Source node: 0

Output: 
Shortest distance from source node 0 to node 0: 0
Shortest distance from source node 0 to node 1: 3
Shortest distance from source node 0 to node 2: 1
Shortest distance from source node 0 to node 3: 4
Shortest distance from source node 0 to node 4: 7
```

## Key Takeaways
- Dijkstra's algorithm is a greedy algorithm that works by maintaining a priority queue of nodes and repeatedly extracting the node with the minimum distance.
- The algorithm assumes that the graph does not contain any negative weight edges.
- The time complexity of Dijkstra's algorithm is O((V + E)logV) using a binary heap, where V is the number of vertices and E is the number of edges.