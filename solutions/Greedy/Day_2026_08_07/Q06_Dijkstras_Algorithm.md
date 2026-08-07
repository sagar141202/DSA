# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest path between nodes in a graph. Given a weighted graph and a starting node (also called the source node), the algorithm finds the shortest path from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix. The algorithm assumes that the graph does not contain any negative weight edges.

## Approach
Dijkstra's algorithm works by maintaining a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighboring nodes. This process continues until the queue is empty, at which point the algorithm has found the shortest path from the source node to all other nodes in the graph. The algorithm uses a greedy approach, always choosing the node with the minimum distance.

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
    distances[source] = 0;

    // Create a priority queue to store nodes to be processed
    priority_queue<Node, vector<Node>, compare> queue;
    queue.push({source, 0});

    while (!queue.empty()) {
        // Extract the node with the minimum distance from the queue
        Node currentNode = queue.top();
        queue.pop();

        // Iterate over the neighbors of the current node
        for (const Edge& edge : graph[currentNode.id]) {
            int newDistance = currentNode.distance + edge.weight;

            // If a shorter path to the neighbor is found, update its distance
            if (newDistance < distances[edge.dest]) {
                distances[edge.dest] = newDistance;
                queue.push({edge.dest, newDistance});
            }
        }
    }

    // Print the shortest distances from the source node to all other nodes
    for (int i = 0; i < numNodes; i++) {
        cout << "Shortest distance from node " << source << " to node " << i << ": " << distances[i] << endl;
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
Shortest distance from node 0 to node 0: 0
Shortest distance from node 0 to node 1: 3
Shortest distance from node 0 to node 2: 1
Shortest distance from node 0 to node 3: 4
Shortest distance from node 0 to node 4: 7
```

## Key Takeaways
- Dijkstra's algorithm is used for finding the shortest path between nodes in a weighted graph.
- The algorithm assumes that the graph does not contain any negative weight edges.
- The algorithm uses a greedy approach, always choosing the node with the minimum distance.