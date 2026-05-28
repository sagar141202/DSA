# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subset of the graph's edges that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list, and the goal is to find the MST with the smallest total weight. For example, given a graph with vertices {0, 1, 2, 3} and edges {(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (2, 3, 5)}, the MST should have a total weight of 10 (edges {(0, 1, 2), (1, 2, 3), (2, 3, 5)}).

## Approach
Prim's algorithm works by selecting the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST. This process is repeated until all vertices are included in the MST. The algorithm uses a priority queue to efficiently select the minimum-weight edge.

## Complexity
- Time: O(E log V)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for an edge
struct Edge {
    int src, dest, weight;
};

// Define the structure for a graph
struct Graph {
    int V, E;
    vector<Edge> edges;
};

// Function to find the parent of a vertex in the disjoint set
int findParent(vector<int>& parent, int vertex) {
    if (parent[vertex] == vertex) return vertex;
    return parent[vertex] = findParent(parent, parent[vertex]);
}

// Function to union two vertices in the disjoint set
void unionVertices(vector<int>& parent, vector<int>& rank, int vertex1, int vertex2) {
    int parent1 = findParent(parent, vertex1);
    int parent2 = findParent(parent, vertex2);

    if (rank[parent1] < rank[parent2]) {
        parent[parent1] = parent2;
    } else if (rank[parent1] > rank[parent2]) {
        parent[parent2] = parent1;
    } else {
        parent[parent2] = parent1;
        rank[parent1]++;
    }
}

// Function to implement Prim's algorithm
vector<Edge> primMST(Graph& graph) {
    vector<Edge> mst;
    vector<int> parent(graph.V);
    vector<int> rank(graph.V, 0);
    vector<bool> included(graph.V, false);

    // Initialize the disjoint set
    for (int i = 0; i < graph.V; i++) {
        parent[i] = i;
    }

    // Create a priority queue to store the edges
    priority_queue<pair<int, Edge>, vector<pair<int, Edge>>, greater<pair<int, Edge>>> pq;

    // Add all edges to the priority queue
    for (const auto& edge : graph.edges) {
        pq.push({edge.weight, edge});
    }

    // Iterate through the priority queue and add edges to the MST
    while (!pq.empty() && mst.size() < graph.V - 1) {
        int weight = pq.top().first;
        Edge edge = pq.top().second;
        pq.pop();

        int vertex1 = edge.src;
        int vertex2 = edge.dest;

        // Check if including the edge forms a cycle
        if (findParent(parent, vertex1) != findParent(parent, vertex2)) {
            mst.push_back(edge);
            unionVertices(parent, rank, vertex1, vertex2);
        }
    }

    return mst;
}

int main() {
    Graph graph;
    graph.V = 4;
    graph.E = 5;
    graph.edges = {{0, 1, 2}, {0, 3, 6}, {1, 2, 3}, {1, 3, 8}, {2, 3, 5}};

    vector<Edge> mst = primMST(graph);

    // Print the edges in the MST
    for (const auto& edge : mst) {
        cout << "Edge (" << edge.src << ", " << edge.dest << ") with weight " << edge.weight << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with vertices {0, 1, 2, 3} and edges {(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (2, 3, 5)}
Output: 
Edge (0, 1) with weight 2
Edge (1, 2) with weight 3
Edge (2, 3) with weight 5
```

## Key Takeaways
- Prim's algorithm is used to find the Minimum Spanning Tree (MST) of a connected, undirected, and weighted graph.
- The algorithm works by iteratively adding the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.