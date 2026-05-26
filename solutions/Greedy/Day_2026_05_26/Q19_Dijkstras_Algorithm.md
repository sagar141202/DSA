# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a graph search algorithm that finds the shortest path between nodes in a graph. Given a weighted graph and a starting node (also called the source node), the algorithm finds the shortest path from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix. The algorithm assumes that the graph does not contain any negative weight edges.

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
    int dist;
};

// Compare function for the priority queue
struct compare {
    bool operator()(const Node &a, const Node &b) {
        return a.dist > b.dist;
    }
};

// Function to implement Dijkstra's algorithm
void dijkstra(vector<vector<Edge>> &graph, int source) {
    int V = graph.size();
    vector<int> dist(V, INT_MAX);
    dist[source] = 0;

    // Create a priority queue to store nodes to be processed
    priority_queue<Node, vector<Node>, compare> pq;
    pq.push({source, 0});

    while (!pq.empty()) {
        Node node = pq.top();
        pq.pop();

        // Process all neighbors of the current node
        for (Edge edge : graph[node.id]) {
            int newDist = node.dist + edge.weight;
            if (newDist < dist[edge.dest]) {
                dist[edge.dest] = newDist;
                pq.push({edge.dest, newDist});
            }
        }
    }

    // Print the shortest distances from the source node to all other nodes
    for (int i = 0; i < V; i++) {
        cout << "Shortest distance from node " << source << " to node " << i << ": " << dist[i] << endl;
    }
}

int main() {
    int V = 5;
    vector<vector<Edge>> graph(V);

    // Add edges to the graph
    graph[0].push_back({1, 4});
    graph[0].push_back({2, 1});
    graph[1].push_back({3, 1});
    graph[2].push_back({1, 2});
    graph[2].push_back({3, 5});
    graph[3].push_back({4, 3});

    int source = 0;
    dijkstra(graph, source);

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 nodes and edges: (0, 1) with weight 4, (0, 2) with weight 1, (1, 3) with weight 1, (2, 1) with weight 2, (2, 3) with weight 5, (3, 4) with weight 3
Source node: 0
Output: 
Shortest distance from node 0 to node 0: 0
Shortest distance from node 0 to node 1: 3
Shortest distance from node 0 to node 2: 1
Shortest distance from node 0 to node 3: 4
Shortest distance from node 0 to node 4: 7
```

## Key Takeaways
- Dijkstra's algorithm is a powerful tool for finding the shortest path in a weighted graph.
- The algorithm uses a greedy approach, always choosing the node with the minimum distance that has not been processed yet.
- The time complexity of Dijkstra's algorithm is O((V + E)logV) using a binary heap, making it efficient for large graphs.