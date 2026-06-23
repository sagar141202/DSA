# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest path between nodes in a graph. It works with weighted graphs, where each edge has a weight or cost associated with it. The goal is to find the minimum-weight path from a source node to all other nodes in the graph. The algorithm assumes that the graph does not contain any negative-weight edges. For example, consider a graph with nodes A, B, C, and D, where the edges have the following weights: A-B (1), A-C (4), B-C (2), B-D (5), C-D (1). The shortest path from A to D would be A-B-C-D with a total weight of 4.

## Approach
Dijkstra's algorithm uses a greedy approach, where it always chooses the next node with the minimum distance that has not been processed yet. This approach ensures that the algorithm finds the shortest path to each node in the graph. The algorithm maintains a priority queue of nodes, where the priority of each node is its minimum distance from the source node.

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
    vector<int> dist(graph.numNodes, INT_MAX);
    dist[src] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        int currNode = pq.top().second;
        int currDist = pq.top().first;
        pq.pop();

        if (currDist > dist[currNode]) {
            continue;
        }

        for (const auto& edge : graph.adjList[currNode]) {
            int newDist = currDist + edge.weight;
            if (newDist < dist[edge.dest]) {
                dist[edge.dest] = newDist;
                pq.push({newDist, edge.dest});
            }
        }
    }

    return dist;
}

int main() {
    // Create a graph
    Graph graph = createGraph(5);

    // Add edges to the graph
    addEdge(graph, 0, 1, 1);
    addEdge(graph, 0, 2, 4);
    addEdge(graph, 1, 2, 2);
    addEdge(graph, 1, 3, 5);
    addEdge(graph, 2, 3, 1);

    // Run Dijkstra's algorithm
    vector<int> dist = dijkstra(graph, 0);

    // Print the shortest distances
    for (int i = 0; i < dist.size(); i++) {
        cout << "Shortest distance from node 0 to node " << i << ": " << dist[i] << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with nodes A, B, C, D
Edges:
A-B (1)
A-C (4)
B-C (2)
B-D (5)
C-D (1)
Source node: A

Output: 
Shortest distance from node A to node A: 0
Shortest distance from node A to node B: 1
Shortest distance from node A to node C: 3
Shortest distance from node A to node D: 4
```

## Key Takeaways
- Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a source node to all other nodes in a weighted graph.
- The algorithm uses a priority queue to keep track of the nodes to be processed, where the priority of each node is its minimum distance from the source node.
- The time complexity of Dijkstra's algorithm is O((V + E)logV), where V is the number of nodes and E is the number of edges in the graph.