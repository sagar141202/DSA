# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest paths between nodes in a graph. Given a weighted graph and a starting node (also called the source node), the algorithm calculates the shortest distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix. The algorithm assumes that the graph does not contain any negative weight edges. The goal is to find the minimum distance from the source node to all other nodes.

## Approach
Dijkstra's algorithm works by maintaining a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighbors. The algorithm terminates when the queue is empty, at which point the shortest distances from the source node to all other nodes have been calculated.

## Complexity
- Time: O((V + E) log V)
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
vector<int> dijkstra(vector<vector<Edge>>& graph, int source) {
    int numNodes = graph.size();
    vector<int> distances(numNodes, INT_MAX);
    distances[source] = 0;

    // Create a priority queue to store nodes to be processed
    priority_queue<Node, vector<Node>, Compare> queue;
    queue.push({source, 0});

    while (!queue.empty()) {
        Node node = queue.top();
        queue.pop();

        // Process all neighbors of the current node
        for (const Edge& edge : graph[node.id]) {
            int newDistance = node.distance + edge.weight;
            if (newDistance < distances[edge.destination]) {
                distances[edge.destination] = newDistance;
                queue.push({edge.destination, newDistance});
            }
        }
    }

    return distances;
}

int main() {
    // Example usage:
    int numNodes = 5;
    vector<vector<Edge>> graph(numNodes);

    // Add edges to the graph
    graph[0].push_back({1, 4});
    graph[0].push_back({2, 1});
    graph[1].push_back({3, 1});
    graph[2].push_back({1, 2});
    graph[2].push_back({3, 5});
    graph[3].push_back({4, 3});

    int source = 0;
    vector<int> distances = dijkstra(graph, source);

    // Print the shortest distances
    for (int i = 0; i < numNodes; i++) {
        cout << "Shortest distance from node " << source << " to node " << i << ": " << distances[i] << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 nodes and the following edges:
0 -> 1 (weight 4)
0 -> 2 (weight 1)
1 -> 3 (weight 1)
2 -> 1 (weight 2)
2 -> 3 (weight 5)
3 -> 4 (weight 3)
Source node: 0

Output: 
Shortest distance from node 0 to node 0: 0
Shortest distance from node 0 to node 1: 3
Shortest distance from node 0 to node 2: 1
Shortest distance from node 0 to node 3: 4
Shortest distance from node 0 to node 4: 7
```

## Key Takeaways
- Dijkstra's algorithm is used for finding the shortest paths between nodes in a weighted graph.
- The algorithm assumes that the graph does not contain any negative weight edges.
- The algorithm has a time complexity of O((V + E) log V) and a space complexity of O(V + E), where V is the number of nodes and E is the number of edges.