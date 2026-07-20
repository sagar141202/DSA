# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The graph is represented as an adjacency list or matrix. The goal is to find the subset of edges with the minimum total weight that connects all vertices. For example, consider a graph with 4 vertices and 5 edges: (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (2, 3, 5). The minimum spanning tree for this graph is (0, 1, 2), (1, 2, 3), (1, 3, 8) with a total weight of 2 + 3 + 5 = 10.

## Approach
Prim's algorithm uses a greedy approach to find the MST. It starts with an arbitrary vertex, adds the minimum-weight edge connected to the visited vertices, and repeats this process until all vertices are visited. The algorithm ensures that the selected edges form a tree and have the minimum total weight.

## Complexity
- Time: O(E log V) for binary heap implementation or O(E + V log V) for Fibonacci heap implementation
- Space: O(V + E) for storing the graph and the MST

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
        vector<int> key(V, INT_MAX);
        vector<int> parent(V, -1);
        vector<bool> mstSet(V, false);
        key[0] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, 0});

        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();
            mstSet[u] = true;

            for (auto neighbor : adj[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;
                if (!mstSet[v] && weight < key[v]) {
                    key[v] = weight;
                    parent[v] = u;
                    pq.push({weight, v});
                }
            }
        }

        int totalWeight = 0;
        for (int i = 1; i < V; i++) {
            totalWeight += key[i];
        }
        return totalWeight;
    }
};

int main() {
    Graph g(4);
    g.addEdge(0, 1, 2);
    g.addEdge(0, 3, 6);
    g.addEdge(1, 2, 3);
    g.addEdge(1, 3, 8);
    g.addEdge(2, 3, 5);

    int mstWeight = g.primMST();
    cout << "Minimum Spanning Tree weight: " << mstWeight << endl;
    return 0;
}
```

## Test Cases
```
Input: 
Graph with 4 vertices and 5 edges: (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (2, 3, 5)
Output: 
Minimum Spanning Tree weight: 10
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm used to find the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm starts with an arbitrary vertex and adds the minimum-weight edge connected to the visited vertices, ensuring the selected edges form a tree with the minimum total weight.
- The time complexity of Prim's algorithm is O(E log V) for binary heap implementation or O(E + V log V) for Fibonacci heap implementation, and the space complexity is O(V + E) for storing the graph and the MST.