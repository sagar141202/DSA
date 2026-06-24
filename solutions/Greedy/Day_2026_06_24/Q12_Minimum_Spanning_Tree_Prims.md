# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list, where each vertex is associated with a list of its neighboring vertices and their corresponding edge weights. The algorithm should start from an arbitrary vertex and find the MST.

## Approach
Prim's algorithm uses a greedy approach to find the MST. It starts with an empty MST and iteratively adds the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST. This process continues until all vertices are included in the MST. The algorithm uses a priority queue to efficiently select the minimum-weight edge.

## Complexity
- Time: O(E log V)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for an edge
struct Edge {
    int u, v, weight;
};

// Define the structure for a graph
struct Graph {
    int V;
    vector<vector<Edge>> adj;
};

// Function to create a graph
Graph createGraph(int V) {
    Graph graph;
    graph.V = V;
    graph.adj.resize(V);
    return graph;
}

// Function to add an edge to the graph
void addEdge(Graph& graph, int u, int v, int weight) {
    Edge edge = {u, v, weight};
    graph.adj[u].push_back(edge);
    edge = {v, u, weight};
    graph.adj[v].push_back(edge);
}

// Function to find the Minimum Spanning Tree using Prim's algorithm
void primMST(Graph& graph) {
    // Initialize the MST and the visited set
    vector<Edge> mst;
    set<int> visited;

    // Start from an arbitrary vertex (0)
    visited.insert(0);

    // Create a priority queue to store the edges
    priority_queue<Edge, vector<Edge>, function<bool(const Edge&, const Edge&)>> pq(
        [](const Edge& a, const Edge& b) { return a.weight > b.weight; });

    // Add all edges from the starting vertex to the priority queue
    for (const auto& edge : graph.adj[0]) {
        pq.push(edge);
    }

    // Iterate until all vertices are included in the MST
    while (visited.size() < graph.V) {
        // Extract the minimum-weight edge from the priority queue
        Edge edge = pq.top();
        pq.pop();

        // If the edge connects a vertex in the MST to a vertex not yet in the MST, add it to the MST
        if (visited.find(edge.v) == visited.end()) {
            mst.push_back(edge);
            visited.insert(edge.v);

            // Add all edges from the newly added vertex to the priority queue
            for (const auto& newEdge : graph.adj[edge.v]) {
                if (visited.find(newEdge.v) == visited.end()) {
                    pq.push(newEdge);
                }
            }
        }
    }

    // Print the edges in the Minimum Spanning Tree
    cout << "Minimum Spanning Tree:" << endl;
    for (const auto& edge : mst) {
        cout << "Edge: " << edge.u << " - " << edge.v << ", Weight: " << edge.weight << endl;
    }
}

int main() {
    // Create a sample graph
    Graph graph = createGraph(5);
    addEdge(graph, 0, 1, 2);
    addEdge(graph, 0, 3, 6);
    addEdge(graph, 1, 2, 3);
    addEdge(graph, 1, 3, 8);
    addEdge(graph, 1, 4, 5);
    addEdge(graph, 2, 4, 7);
    addEdge(graph, 3, 4, 9);

    // Find the Minimum Spanning Tree using Prim's algorithm
    primMST(graph);

    return 0;
}
```

## Test Cases
```
Input:
Graph with 5 vertices and 7 edges:
Edge: 0 - 1, Weight: 2
Edge: 0 - 3, Weight: 6
Edge: 1 - 2, Weight: 3
Edge: 1 - 3, Weight: 8
Edge: 1 - 4, Weight: 5
Edge: 2 - 4, Weight: 7
Edge: 3 - 4, Weight: 9

Output:
Minimum Spanning Tree:
Edge: 0 - 1, Weight: 2
Edge: 1 - 2, Weight: 3
Edge: 1 - 4, Weight: 5
Edge: 0 - 3, Weight: 6
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm starts from an arbitrary vertex and iteratively adds the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST.
- The algorithm uses a priority queue to efficiently select the minimum-weight edge.