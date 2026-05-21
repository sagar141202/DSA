# Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) of the graph using Kruskal's algorithm. The MST is a subgraph that connects all vertices together with the minimum total edge weight. The graph is represented as a list of edges, where each edge is a tuple of (weight, vertex1, vertex2). The goal is to find the MST and calculate its total weight.

## Approach
Kruskal's algorithm works by sorting all edges in non-decreasing order of their weights and then selecting the smallest edge that does not form a cycle. This process is repeated until all vertices are connected. The algorithm uses a disjoint-set data structure to efficiently check for cycles.

## Complexity
- Time: O(E log E) or O(E log V) due to sorting the edges
- Space: O(V + E) for storing the graph and the disjoint-set data structure

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for an edge
struct Edge {
    int weight, vertex1, vertex2;
};

// Define a comparison function for sorting edges
bool compareEdges(const Edge& a, const Edge& b) {
    return a.weight < b.weight;
}

// Define the structure for a disjoint-set
struct DisjointSet {
    vector<int> parent, rank;
    
    // Initialize the disjoint-set
    DisjointSet(int V) {
        parent.resize(V + 1);
        rank.resize(V + 1, 0);
        for (int i = 1; i <= V; i++) {
            parent[i] = i;
        }
    }
    
    // Find the root of a vertex
    int find(int vertex) {
        if (parent[vertex] != vertex) {
            parent[vertex] = find(parent[vertex]);
        }
        return parent[vertex];
    }
    
    // Union two vertices
    void unionVertices(int vertex1, int vertex2) {
        int root1 = find(vertex1);
        int root2 = find(vertex2);
        
        if (root1 != root2) {
            if (rank[root1] < rank[root2]) {
                parent[root1] = root2;
            } else if (rank[root1] > rank[root2]) {
                parent[root2] = root1;
            } else {
                parent[root2] = root1;
                rank[root1]++;
            }
        }
    }
};

// Kruskal's algorithm to find the MST
int kruskal(vector<Edge>& edges, int V) {
    sort(edges.begin(), edges.end(), compareEdges);
    DisjointSet ds(V);
    int totalWeight = 0;
    int edgeCount = 0;
    
    for (const Edge& edge : edges) {
        if (ds.find(edge.vertex1) != ds.find(edge.vertex2)) {
            ds.unionVertices(edge.vertex1, edge.vertex2);
            totalWeight += edge.weight;
            edgeCount++;
        }
        
        if (edgeCount == V - 1) {
            break;
        }
    }
    
    return totalWeight;
}

int main() {
    int V, E;
    cin >> V >> E;
    
    vector<Edge> edges(E);
    for (int i = 0; i < E; i++) {
        cin >> edges[i].weight >> edges[i].vertex1 >> edges[i].vertex2;
    }
    
    int totalWeight = kruskal(edges, V);
    cout << "Total weight of MST: " << totalWeight << endl;
    
    return 0;
}
```

## Test Cases
```
Input:
4 5
1 1 2
2 2 3
3 1 3
4 3 4
5 2 4
Output:
Total weight of MST: 6
```

## Key Takeaways
- Kruskal's algorithm is a greedy algorithm that finds the MST of a graph by selecting the smallest edge that does not form a cycle.
- The algorithm uses a disjoint-set data structure to efficiently check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V) due to sorting the edges.