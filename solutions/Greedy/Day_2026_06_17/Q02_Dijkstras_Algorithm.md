# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory used for finding the shortest paths between nodes in a graph. Given a weighted graph and a source node, the algorithm calculates the minimum distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix. The algorithm assumes that the graph does not contain any negative weight edges. For example, consider a graph with 5 nodes (A, B, C, D, E) and the following edges: A-B (weight 1), A-C (weight 4), B-C (weight 2), B-D (weight 5), C-D (weight 1), D-E (weight 3). If we want to find the shortest distance from node A to all other nodes, Dijkstra's algorithm can be used.

## Approach
Dijkstra's algorithm works by maintaining a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighboring nodes. This process continues until all nodes have been processed.

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
    int dist;
};

// Comparison function for the priority queue
struct compare {
    bool operator()(const Node& a, const Node& b) {
        return a.dist > b.dist;
    }
};

// Function to implement Dijkstra's algorithm
void dijkstra(vector<vector<Edge>>& graph, int source) {
    // Initialize the distance array
    vector<int> dist(graph.size(), INT_MAX);
    dist[source] = 0;

    // Create a priority queue
    priority_queue<Node, vector<Node>, compare> pq;
    pq.push({source, 0});

    while (!pq.empty()) {
        // Extract the node with the minimum priority from the queue
        Node node = pq.top();
        pq.pop();

        // Update the distances of the neighboring nodes
        for (const Edge& edge : graph[node.id]) {
            if (dist[edge.dest] > dist[node.id] + edge.weight) {
                dist[edge.dest] = dist[node.id] + edge.weight;
                pq.push({edge.dest, dist[edge.dest]});
            }
        }
    }

    // Print the shortest distances
    for (int i = 0; i < dist.size(); i++) {
        cout << "Shortest distance from source " << source << " to node " << i << ": " << dist[i] << endl;
    }
}

int main() {
    // Create a sample graph
    int numNodes = 5;
    vector<vector<Edge>> graph(numNodes);

    // Add edges to the graph
    graph[0].push_back({1, 1});
    graph[0].push_back({2, 4});
    graph[1].push_back({2, 2});
    graph[1].push_back({3, 5});
    graph[2].push_back({3, 1});
    graph[3].push_back({4, 3});

    // Run Dijkstra's algorithm
    dijkstra(graph, 0);

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 nodes (A, B, C, D, E) and the following edges: A-B (weight 1), A-C (weight 4), B-C (weight 2), B-D (weight 5), C-D (weight 1), D-E (weight 3)
Source node: A (node 0)
Output: 
Shortest distance from source 0 to node 0: 0
Shortest distance from source 0 to node 1: 1
Shortest distance from source 0 to node 2: 3
Shortest distance from source 0 to node 3: 4
Shortest distance from source 0 to node 4: 7
```

## Key Takeaways
- Dijkstra's algorithm is a popular algorithm for finding the shortest paths in a graph.
- The algorithm assumes that the graph does not contain any negative weight edges.
- The time complexity of Dijkstra's algorithm is O((V + E)logV) using a priority queue, where V is the number of vertices and E is the number of edges.