# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the minimum spanning tree using Prim's algorithm. The minimum spanning tree is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list, where each vertex is associated with a list of its neighboring vertices and the corresponding edge weights.

## Approach
Prim's algorithm works by selecting the minimum-weight edge that connects a vertex in the minimum spanning tree to a vertex not yet in the tree. This process is repeated until all vertices are included in the tree. The algorithm uses a priority queue to efficiently select the minimum-weight edge.

## Complexity
- Time: O(E log V)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Graph {
    int V;
    vector<vector<pair<int, int>>> adj;

public:
    Graph(int vertices) : V(vertices), adj(vertices) {}

    void addEdge(int u, int v, int weight) {
        adj[u].emplace_back(v, weight);
        adj[v].emplace_back(u, weight);
    }

    int primMST() {
        vector<int> key(V, INT_MAX);
        vector<int> parent(V, -1);
        vector<bool> mstSet(V, false);
        key[0] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.emplace(0, 0);

        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();

            mstSet[u] = true;

            for (const auto& neighbor : adj[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;

                if (!mstSet[v] && weight < key[v]) {
                    key[v] = weight;
                    parent[v] = u;
                    pq.emplace(weight, v);
                }
            }
        }

        int mstWeight = 0;
        for (int i = 1; i < V; i++) {
            mstWeight += key[i];
        }

        return mstWeight;
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
Edges:
(0, 1, 2)
(0, 3, 6)
(1, 2, 3)
(1, 3, 8)
(1, 4, 5)
(2, 4, 7)
(3, 4, 9)
Output: Minimum Spanning Tree weight: 16
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm used to find the minimum spanning tree of a connected, undirected, and weighted graph.
- The algorithm works by selecting the minimum-weight edge that connects a vertex in the minimum spanning tree to a vertex not yet in the tree.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.