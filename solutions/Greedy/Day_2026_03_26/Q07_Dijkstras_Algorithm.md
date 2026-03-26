# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest paths between nodes in a graph. Given a weighted graph and a starting node (also called the source node), the algorithm finds the shortest path from the source node to all other nodes in the graph. The graph can be directed or undirected, and the weights can be positive or negative. However, if the graph contains negative weight edges, Dijkstra's algorithm may not work correctly. The goal is to find the minimum distance from the source node to all other nodes in the graph.

## Approach
Dijkstra's algorithm uses a greedy approach to find the shortest path. It starts at the source node and iteratively selects the node with the minimum distance that has not been visited yet. The algorithm then updates the distances of the neighboring nodes and repeats the process until all nodes have been visited.

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

    // Create a priority queue to hold nodes to be processed
    priority_queue<Node, vector<Node>, compare> pq;
    pq.push({source, 0});

    while (!pq.empty()) {
        Node currentNode = pq.top();
        pq.pop();

        // If the current distance is greater than the known distance, skip this node
        if (currentNode.distance > distances[currentNode.id]) {
            continue;
        }

        // Iterate over all neighbors of the current node
        for (const Edge& edge : graph[currentNode.id]) {
            int newDistance = currentNode.distance + edge.weight;

            // If a shorter path to the neighbor is found, update the distance and add to the priority queue
            if (newDistance < distances[edge.dest]) {
                distances[edge.dest] = newDistance;
                pq.push({edge.dest, newDistance});
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
- Node 0 to Node 1 with weight 4
- Node 0 to Node 2 with weight 1
- Node 1 to Node 3 with weight 1
- Node 2 to Node 1 with weight 2
- Node 2 to Node 3 with weight 5
- Node 3 to Node 4 with weight 3
Source node: 0

Output: 
Shortest distance from node 0 to node 0: 0
Shortest distance from node 0 to node 1: 3
Shortest distance from node 0 to node 2: 1
Shortest distance from node 0 to node 3: 4
Shortest distance from node 0 to node 4: 7
```

## Key Takeaways
- Dijkstra's algorithm is a popular algorithm for finding the shortest paths in a graph.
- The algorithm uses a greedy approach to select the node with the minimum distance that has not been visited yet.
- The time complexity of Dijkstra's algorithm is O((V + E)logV) using a binary heap, where V is the number of vertices and E is the number of edges.