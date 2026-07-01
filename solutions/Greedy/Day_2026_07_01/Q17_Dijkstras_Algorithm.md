# Dijkstra's Algorithm

## Problem Statement
Given a weighted graph with non-negative edge weights, find the shortest path from a source node to all other nodes in the graph. The graph is represented as an adjacency list, where each node is associated with a list of its neighbors and the corresponding edge weights. The source node is given, and the goal is to find the minimum distance from the source node to all other nodes.

## Approach
Dijkstra's algorithm uses a greedy approach to find the shortest path by selecting the node with the minimum distance that has not been processed yet. It maintains a priority queue of nodes, where the priority of each node is its current minimum distance from the source node.

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

// Compare function for the priority queue
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
    priority_queue<Node, vector<Node>, Compare> pq;
    pq.push({source, 0});

    while (!pq.empty()) {
        Node currentNode = pq.top();
        pq.pop();

        // Process all neighbors of the current node
        for (const Edge& edge : graph[currentNode.id]) {
            int newDistance = currentNode.distance + edge.weight;
            if (newDistance < distances[edge.dest]) {
                distances[edge.dest] = newDistance;
                pq.push({edge.dest, newDistance});
            }
        }
    }

    // Print the shortest distances from the source node to all other nodes
    for (int i = 0; i < numNodes; i++) {
        cout << "Shortest distance from source " << source << " to node " << i << ": " << distances[i] << endl;
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
0 -> 1 (weight: 4)
0 -> 2 (weight: 1)
1 -> 3 (weight: 1)
2 -> 1 (weight: 2)
2 -> 3 (weight: 5)
3 -> 4 (weight: 3)
Source node: 0

Output: 
Shortest distance from source 0 to node 0: 0
Shortest distance from source 0 to node 1: 3
Shortest distance from source 0 to node 2: 1
Shortest distance from source 0 to node 3: 4
Shortest distance from source 0 to node 4: 7
```

## Key Takeaways
- Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a source node to all other nodes in a weighted graph.
- The algorithm uses a priority queue to store nodes to be processed, where the priority of each node is its current minimum distance from the source node.
- The time complexity of Dijkstra's algorithm is O((V + E)logV), where V is the number of nodes and E is the number of edges in the graph.