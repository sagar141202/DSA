# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subset of the edges in the graph that connects all the vertices together while minimizing the total edge cost. The graph is represented as an adjacency list or adjacency matrix, and the goal is to find the minimum-weight subgraph that spans all the vertices. For example, consider a graph with 5 vertices and the following edges: (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9). The minimum spanning tree for this graph would be the subset of edges with the minimum total weight that connects all 5 vertices.

## Approach
Prim's algorithm works by starting at an arbitrary vertex and growing the tree one edge at a time. It selects the minimum-weight edge that connects a vertex in the tree to a vertex not yet in the tree. This process is repeated until all vertices are included in the tree. The algorithm uses a priority queue to efficiently select the minimum-weight edge.

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
    if (parent[vertex] == vertex)
        return vertex;
    return parent[vertex] = findParent(parent, parent[vertex]);
}

// Function to union two vertices in the disjoint set
void unionVertices(vector<int>& parent, vector<int>& rank, int vertex1, int vertex2) {
    int root1 = findParent(parent, vertex1);
    int root2 = findParent(parent, vertex2);

    if (rank[root1] < rank[root2])
        parent[root1] = root2;
    else if (rank[root1] > rank[root2])
        parent[root2] = root1;
    else {
        parent[root2] = root1;
        rank[root1]++;
    }
}

// Function to implement Prim's algorithm
vector<Edge> primMST(Graph& graph) {
    vector<Edge> mst;
    vector<int> parent(graph.V);
    vector<int> rank(graph.V, 0);
    vector<bool> visited(graph.V, false);

    // Create a priority queue to store edges
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;

    // Initialize the disjoint set and add the first vertex to the priority queue
    for (int i = 0; i < graph.V; i++) {
        parent[i] = i;
    }
    for (Edge& edge : graph.edges) {
        pq.push({edge.weight, {edge.src, edge.dest}});
    }

    // Run Prim's algorithm
    while (!pq.empty() && mst.size() < graph.V - 1) {
        int weight = pq.top().first;
        int src = pq.top().second.first;
        int dest = pq.top().second.second;
        pq.pop();

        if (findParent(parent, src) != findParent(parent, dest)) {
            mst.push_back({src, dest, weight});
            unionVertices(parent, rank, src, dest);
        }
    }

    return mst;
}

int main() {
    // Example usage
    Graph graph;
    graph.V = 5;
    graph.E = 7;
    graph.edges = {{0, 1, 2}, {0, 3, 6}, {1, 2, 3}, {1, 3, 8}, {1, 4, 5}, {2, 4, 7}, {3, 4, 9}};

    vector<Edge> mst = primMST(graph);

    cout << "Minimum Spanning Tree Edges:\n";
    for (Edge& edge : mst) {
        cout << "Edge: (" << edge.src << ", " << edge.dest << "), Weight: " << edge.weight << "\n";
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and the following edges: (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)
Output: 
Minimum Spanning Tree Edges:
Edge: (0, 1), Weight: 2
Edge: (1, 2), Weight: 3
Edge: (1, 4), Weight: 5
Edge: (0, 3), Weight: 6
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm used to find the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- It works by starting at an arbitrary vertex and growing the tree one edge at a time, selecting the minimum-weight edge that connects a vertex in the tree to a vertex not yet in the tree.
- The algorithm uses a priority queue to efficiently select the minimum-weight edge and a disjoint set to keep track of the connected components in the tree.