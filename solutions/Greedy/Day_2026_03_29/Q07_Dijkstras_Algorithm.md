# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest path between nodes in a graph. Given a weighted graph and a source node, the algorithm calculates the minimum distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix, and the algorithm assumes that all edge weights are non-negative. The goal is to find the shortest path from the source node to all other nodes, and the algorithm should be able to handle graphs with multiple connected components.

## Approach
Dijkstra's algorithm works by maintaining a priority queue of nodes to visit, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue, updates the distances of its neighbors, and marks the node as visited. This process continues until all nodes have been visited.

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

    // Create a priority queue to store nodes to visit
    priority_queue<Node, vector<Node>, compare> queue;
    queue.push({source, 0});

    while (!queue.empty()) {
        Node currentNode = queue.top();
        queue.pop();

        // Visit each neighbor of the current node
        for (const Edge& edge : graph[currentNode.id]) {
            int newDistance = currentNode.distance + edge.weight;
            if (newDistance < distances[edge.dest]) {
                distances[edge.dest] = newDistance;
                queue.push({edge.dest, newDistance});
            }
        }
    }

    // Print the shortest distances from the source node
    for (int i = 0; i < numNodes; i++) {
        cout << "Shortest distance from source to node " << i << ": " << distances[i] << endl;
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

    // Run Dijkstra's algorithm
    dijkstra(graph, 0);

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
Shortest distance from source to node 0: 0
Shortest distance from source to node 1: 3
Shortest distance from source to node 2: 1
Shortest distance from source to node 3: 4
Shortest distance from source to node 4: 7
```

## Key Takeaways
- Dijkstra's algorithm is a powerful tool for finding the shortest path in a weighted graph.
- The algorithm uses a priority queue to efficiently select the next node to visit.
- The time complexity of Dijkstra's algorithm is O((V + E)logV), making it suitable for large graphs.