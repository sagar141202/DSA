# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list, where each edge is a tuple of (vertex, weight). The algorithm should return the total weight of the MST.

## Approach
Prim's algorithm works by starting with an arbitrary vertex and growing the tree by adding the minimum-weight edge that connects a vertex in the tree to a vertex not yet in the tree. This process is repeated until all vertices are included in the tree. The algorithm uses a priority queue to efficiently select the minimum-weight edge.

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

    void addEdge(int u, int v, int weight) {
        adj[u].emplace_back(v, weight);
        adj[v].emplace_back(u, weight);
    }

    int primMST() {
        vector<bool> visited(V, false);
        vector<int> key(V, INT_MAX);
        vector<int> parent(V, -1);
        key[0] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.push({0, 0});

        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();

            visited[u] = true;

            for (const auto& edge : adj[u]) {
                int v = edge.first;
                int weight = edge.second;

                if (!visited[v] && weight < key[v]) {
                    key[v] = weight;
                    parent[v] = u;
                    pq.push({weight, v});
                }
            }
        }

        int totalWeight = 0;
        for (int i = 1; i < V; ++i) {
            totalWeight += key[i];
        }

        return totalWeight;
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
    5 vertices
    edges: (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)
Output: 
    Minimum Spanning Tree weight: 16
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph.
- The algorithm uses a priority queue to efficiently select the minimum-weight edge.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.