# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, the goal is to find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list, where each edge is a tuple of (vertex1, vertex2, weight). The constraints are: 1 ≤ V ≤ 10^5, 1 ≤ E ≤ 10^5, and 1 ≤ weight ≤ 10^5. For example, consider a graph with 4 vertices and 5 edges: (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (2, 3, 5). The output should be the total weight of the MST, which is 2 + 3 + 5 = 10.

## Approach
Prim's algorithm uses a greedy approach to find the MST. It starts with an arbitrary vertex and grows the tree by adding the minimum-weight edge that connects a vertex in the tree to a vertex not yet in the tree. This process continues until all vertices are included in the tree. The algorithm uses a priority queue to efficiently select the minimum-weight edge.

## Complexity
- Time: O(E log V)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class DisjointSet {
public:
    vector<int> parent, rank;
    DisjointSet(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

class Graph {
public:
    int V;
    vector<vector<pair<int, int>>> adj;
    Graph(int vertices) {
        V = vertices;
        adj.resize(vertices);
    }
    void addEdge(int u, int v, int weight) {
        adj[u].push_back({v, weight});
        adj[v].push_back({u, weight});
    }
    int primMST() {
        vector<bool> visited(V, false);
        vector<int> key(V, INT_MAX);
        key[0] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, 0});
        int totalWeight = 0;
        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();
            visited[u] = true;
            for (auto neighbor : adj[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;
                if (!visited[v] && weight < key[v]) {
                    key[v] = weight;
                    pq.push({weight, v});
                }
            }
        }
        for (int i = 1; i < V; i++) {
            totalWeight += key[i];
        }
        return totalWeight;
    }
};

int main() {
    int V = 4;
    Graph graph(V);
    graph.addEdge(0, 1, 2);
    graph.addEdge(0, 3, 6);
    graph.addEdge(1, 2, 3);
    graph.addEdge(1, 3, 8);
    graph.addEdge(2, 3, 5);
    int totalWeight = graph.primMST();
    cout << "Total weight of MST: " << totalWeight << endl;
    return 0;
}
```

## Test Cases
```
Input: 
V = 4
Edges: (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (2, 3, 5)
Output: 
Total weight of MST: 10
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm uses a priority queue to efficiently select the minimum-weight edge that connects a vertex in the tree to a vertex not yet in the tree.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.