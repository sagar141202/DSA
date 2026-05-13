# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a graph search algorithm that finds the shortest path between nodes in a graph. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later. The algorithm works by maintaining a list of unvisited nodes and iteratively selecting the node with the shortest distance (or minimum cost) from the source node, then updating the distances to its neighboring nodes. The process is repeated until all nodes have been visited. The algorithm assumes that the graph does not contain any negative-weight edges.

## Approach
Dijkstra's algorithm uses a greedy approach to find the shortest path. It starts at the source node, explores the nearest node, and then backtracks until it finds the shortest path. The algorithm uses a priority queue to efficiently select the node with the minimum distance.

## Complexity
- Time: O((V + E) log V)
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
    int numVertices;
    vector<vector<Edge>> adjLists;
};

// Function to create a graph with the given number of vertices
Graph createGraph(int numVertices) {
    Graph graph;
    graph.numVertices = numVertices;
    graph.adjLists.resize(numVertices);
    return graph;
}

// Function to add an edge to the graph
void addEdge(Graph& graph, int src, int dest, int weight) {
    Edge edge;
    edge.dest = dest;
    edge.weight = weight;
    graph.adjLists[src].push_back(edge);
}

// Function to implement Dijkstra's algorithm
void dijkstra(Graph& graph, int src) {
    // Create a vector to store the minimum distances
    vector<int> distances(graph.numVertices, INT_MAX);
    distances[src] = 0;

    // Create a priority queue to store the nodes to be visited
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        // Extract the node with the minimum distance from the priority queue
        int currNode = pq.top().second;
        int currDistance = pq.top().first;
        pq.pop();

        // Iterate over the adjacent nodes of the current node
        for (const Edge& edge : graph.adjLists[currNode]) {
            int adjNode = edge.dest;
            int weight = edge.weight;

            // Update the distance to the adjacent node if a shorter path is found
            if (currDistance + weight < distances[adjNode]) {
                distances[adjNode] = currDistance + weight;
                pq.push({distances[adjNode], adjNode});
            }
        }
    }

    // Print the minimum distances from the source node to all other nodes
    for (int i = 0; i < graph.numVertices; i++) {
        cout << "Shortest distance from node " << src << " to node " << i << ": " << distances[i] << endl;
    }
}

int main() {
    // Create a graph with 5 vertices
    Graph graph = createGraph(5);

    // Add edges to the graph
    addEdge(graph, 0, 1, 4);
    addEdge(graph, 0, 2, 1);
    addEdge(graph, 1, 3, 1);
    addEdge(graph, 2, 1, 2);
    addEdge(graph, 2, 3, 5);
    addEdge(graph, 3, 4, 3);

    // Run Dijkstra's algorithm from node 0
    dijkstra(graph, 0);

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and the following edges:
0 -> 1 (weight: 4)
0 -> 2 (weight: 1)
1 -> 3 (weight: 1)
2 -> 1 (weight: 2)
2 -> 3 (weight: 5)
3 -> 4 (weight: 3)

Output: 
Shortest distance from node 0 to node 0: 0
Shortest distance from node 0 to node 1: 3
Shortest distance from node 0 to node 2: 1
Shortest distance from node 0 to node 3: 4
Shortest distance from node 0 to node 4: 7
```

## Key Takeaways
- Dijkstra's algorithm is a graph search algorithm that finds the shortest path between nodes in a graph.
- The algorithm uses a greedy approach to find the shortest path by maintaining a list of unvisited nodes and iteratively selecting the node with the minimum distance.
- The algorithm has a time complexity of O((V + E) log V) and a space complexity of O(V + E), where V is the number of vertices and E is the number of edges in the graph.