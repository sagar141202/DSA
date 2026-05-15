# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a graph search algorithm that finds the shortest path between nodes in a graph. It works with weighted graphs, where each edge has a weight or cost associated with it. The goal is to find the minimum-weight path from a source node to all other nodes in the graph. The algorithm assumes that the graph does not contain any negative-weight edges. For example, given a graph with nodes A, B, C, and D, and edges with weights: A-B (2), A-C (4), B-C (1), B-D (5), C-D (3), the algorithm should return the shortest path from A to all other nodes.

## Approach
Dijkstra's algorithm uses a greedy approach to find the shortest path by selecting the node with the minimum distance that has not been processed yet. It maintains a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighbors.

## Complexity
- Time: O(|E|log|V|)
- Space: O(|V| + |E|)

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
struct Compare {
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
    priority_queue<Node, vector<Node>, Compare> queue;
    queue.push({source, 0});

    while (!queue.empty()) {
        Node currentNode = queue.top();
        queue.pop();

        // Process all neighbors of the current node
        for (const Edge& edge : graph[currentNode.id]) {
            int newDistance = currentNode.distance + edge.weight;
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
    // Create a sample graph
    int numNodes = 5;
    vector<vector<Edge>> graph(numNodes);

    // Add edges to the graph
    graph[0].push_back({1, 2});
    graph[0].push_back({2, 4});
    graph[1].push_back({2, 1});
    graph[1].push_back({3, 5});
    graph[2].push_back({3, 3});

    // Run Dijkstra's algorithm
    dijkstra(graph, 0);

    return 0;
}
```

## Test Cases
```
Input:
Graph with nodes A, B, C, D, and edges:
A-B (2)
A-C (4)
B-C (1)
B-D (5)
C-D (3)

Output:
Shortest distance from node 0 to node 0: 0
Shortest distance from node 0 to node 1: 2
Shortest distance from node 0 to node 2: 3
Shortest distance from node 0 to node 3: 6
```

## Key Takeaways
- Dijkstra's algorithm is a popular algorithm for finding the shortest path in a weighted graph.
- The algorithm uses a greedy approach to select the node with the minimum distance that has not been processed yet.
- The time complexity of Dijkstra's algorithm is O(|E|log|V|) using a binary heap, where |E| is the number of edges and |V| is the number of vertices.