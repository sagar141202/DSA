# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a graph search algorithm that finds the shortest paths between nodes in a graph. Given a weighted graph and a source node, the goal is to find the shortest distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix, and the edge weights can be positive or zero. The algorithm should return an array of distances from the source node to all other nodes, or a special value (e.g., -1) if there is no path.

## Approach
Dijkstra's algorithm uses a greedy approach to find the shortest paths by maintaining a priority queue of nodes to visit, where the priority is the current shortest distance from the source node. The algorithm repeatedly extracts the node with the minimum distance from the queue and updates the distances to its neighbors.

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

    // Create a priority queue to store nodes to visit
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        int currNode = pq.top().second;
        int currDist = pq.top().first;
        pq.pop();

        // Visit all neighbors of the current node
        for (const auto& edge : graph.adjList[currNode]) {
            int neighbor = edge.dest;
            int weight = edge.weight;

            // Update the distance to the neighbor if a shorter path is found
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

    // Print the distances
    for (int i = 0; i < distances.size(); i++) {
        cout << "Distance from node 0 to node " << i << ": " << distances[i] << endl;
    }

    return 0;
}
```

## Test Cases
```
Input:
Graph with 5 nodes and the following edges:
(0, 1) with weight 4
(0, 2) with weight 1
(1, 3) with weight 1
(2, 1) with weight 2
(2, 3) with weight 5
(3, 4) with weight 3
Source node: 0

Output:
Distance from node 0 to node 0: 0
Distance from node 0 to node 1: 3
Distance from node 0 to node 2: 1
Distance from node 0 to node 3: 4
Distance from node 0 to node 4: 7
```

## Key Takeaways
- Dijkstra's algorithm is a greedy algorithm that finds the shortest paths from a source node to all other nodes in a weighted graph.
- The algorithm uses a priority queue to efficiently select the node with the minimum distance to visit next.
- The time complexity of Dijkstra's algorithm is O((V + E)logV) using a binary heap as the priority queue, where V is the number of nodes and E is the number of edges in the graph.