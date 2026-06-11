# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The graph is represented as an adjacency list, where each edge is a tuple of (u, v, w) representing an edge between vertices u and v with weight w. The goal is to find the subset of edges with the minimum total weight that connects all vertices in the graph. For example, consider a graph with 5 vertices and the following edges: (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9). The minimum spanning tree for this graph should have a total weight of 16.

## Approach
Prim's algorithm works by selecting a random vertex as the starting point and then iteratively adding the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST. This process continues until all vertices are included in the MST. The algorithm uses a priority queue to efficiently select the minimum-weight edge at each step.

## Complexity
- Time: O(E log V)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Graph {
public:
    int V;
    vector<vector<pair<int, int>>> adj;

    Graph(int vertices) : V(vertices), adj(vertices) {}

    void addEdge(int u, int v, int w) {
        adj[u].emplace_back(v, w);
        adj[v].emplace_back(u, w);
    }

    int primMST() {
        vector<int> key(V, INT_MAX);
        vector<int> parent(V, -1);
        vector<bool> mstSet(V, false);
        key[0] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.emplace(0, 0);

        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();

            mstSet[u] = true;

            for (const auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;

                if (!mstSet[v] && w < key[v]) {
                    key[v] = w;
                    parent[v] = u;
                    pq.emplace(w, v);
                }
            }
        }

        int weight = 0;
        for (int i = 1; i < V; ++i) {
            weight += key[i];
        }

        return weight;
    }
};

int main() {
    Graph g(5);
    g.addEdge(0, 1, 2);
    g.addEdge(0, 3, 6);
    g.addEdge(1, 2, 3);
    g.addEdge(1, 3, 8);
    g.addEdge(1, 4, 5);
    g.addEdge(2, 4, 7);
    g.addEdge(3, 4, 9);

    cout << "Minimum Spanning Tree weight: " << g.primMST() << endl;

    return 0;
}
```

## Test Cases
```
Input: 
Vertices: 5
Edges: (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)
Output: 
Minimum Spanning Tree weight: 16
```

## Key Takeaways
- Prim's algorithm is an efficient method for finding the Minimum Spanning Tree of a graph.
- The algorithm uses a priority queue to select the minimum-weight edge at each step, resulting in a time complexity of O(E log V).
- The space complexity is O(V + E), which is used to store the adjacency list representation of the graph and the MST.