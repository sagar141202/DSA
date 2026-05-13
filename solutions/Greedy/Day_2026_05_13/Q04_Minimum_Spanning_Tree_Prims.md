# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list, where each edge is a tuple of (u, v, w) denoting an edge between vertices u and v with weight w. The goal is to find the MST with the minimum total edge weight.

## Approach
Prim's algorithm uses a greedy approach to find the MST by selecting the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST. The algorithm starts with an arbitrary vertex and iteratively adds edges to the MST until all vertices are connected.

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
    edge = {v, u, weight}; // For undirected graph
    graph.adj[v].push_back(edge);
}

// Function to find the Minimum Spanning Tree using Prim's algorithm
int primMST(Graph& graph) {
    int V = graph.V;
    vector<bool> visited(V, false);
    vector<int> parent(V, -1);
    vector<int> key(V, INT_MAX);
    key[0] = 0; // Start with vertex 0
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, 0}); // (weight, vertex)

    int mstWeight = 0;
    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();
        visited[u] = true;

        for (const auto& edge : graph.adj[u]) {
            int v = edge.v;
            int weight = edge.weight;
            if (!visited[v] && weight < key[v]) {
                key[v] = weight;
                parent[v] = u;
                pq.push({weight, v});
            }
        }
    }

    // Calculate the total weight of the MST
    for (int i = 1; i < V; i++) {
        mstWeight += key[i];
    }

    return mstWeight;
}

int main() {
    int V = 5;
    Graph graph = createGraph(V);

    addEdge(graph, 0, 1, 2);
    addEdge(graph, 0, 3, 6);
    addEdge(graph, 1, 2, 3);
    addEdge(graph, 1, 3, 8);
    addEdge(graph, 1, 4, 5);
    addEdge(graph, 2, 4, 7);
    addEdge(graph, 3, 4, 9);

    int mstWeight = primMST(graph);
    cout << "Minimum Spanning Tree Weight: " << mstWeight << endl;

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and 7 edges:
0 --2-- 1 --3-- 2
|        |        |
6        |        | 7
|        | 5      |
3 --8-- 1 --5-- 4
|              |
9              |
Output: 
Minimum Spanning Tree Weight: 16
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm starts with an arbitrary vertex and iteratively adds edges to the MST until all vertices are connected.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.