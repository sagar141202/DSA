# Minimum Spanning Tree (Prim's)

## Problem Statement
Given an undirected and connected graph with non-negative edge weights, find the Minimum Spanning Tree (MST) of the graph using Prim's algorithm. The graph is represented as an adjacency list, where each node is connected to its neighboring nodes with their respective edge weights. The goal is to find the subset of edges that connect all nodes in the graph with the minimum total edge weight. For example, given a graph with nodes A, B, C, and D, and edges (A, B, 1), (A, C, 4), (B, C, 2), (B, D, 5), (C, D, 3), the MST would be (A, B, 1), (B, C, 2), (C, D, 3) with a total edge weight of 6.

## Approach
Prim's algorithm uses a greedy approach to find the MST by selecting the minimum-weight edge that connects a node in the MST to a node not yet in the MST. This process is repeated until all nodes are included in the MST. The algorithm starts with an arbitrary node and grows the tree by adding the minimum-weight edge at each step.

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
void primMST(Graph& graph) {
    vector<bool> visited(graph.V, false);
    vector<int> parent(graph.V, -1);
    vector<int> key(graph.V, INT_MAX);
    key[0] = 0; // Start with node 0
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, 0}); // (weight, node)

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

    // Print the MST edges
    int totalWeight = 0;
    for (int i = 1; i < graph.V; i++) {
        cout << "Edge: (" << parent[i] << ", " << i << "), Weight: " << key[i] << endl;
        totalWeight += key[i];
    }
    cout << "Total Weight: " << totalWeight << endl;
}

int main() {
    int V = 4;
    Graph graph = createGraph(V);
    addEdge(graph, 0, 1, 1);
    addEdge(graph, 0, 2, 4);
    addEdge(graph, 1, 2, 2);
    addEdge(graph, 1, 3, 5);
    addEdge(graph, 2, 3, 3);

    primMST(graph);
    return 0;
}
```

## Test Cases
```
Input:
Nodes: A, B, C, D
Edges: (A, B, 1), (A, C, 4), (B, C, 2), (B, D, 5), (C, D, 3)

Output:
Edge: (0, 1), Weight: 1
Edge: (1, 2), Weight: 2
Edge: (2, 3), Weight: 3
Total Weight: 6
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph by selecting the minimum-weight edge at each step.
- The algorithm starts with an arbitrary node and grows the tree by adding the minimum-weight edge that connects a node in the tree to a node not yet in the tree.
- The time complexity of Prim's algorithm is O(E log V) using a priority queue, where E is the number of edges and V is the number of vertices.