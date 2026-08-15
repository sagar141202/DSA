# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list or matrix, where each edge is a pair of vertices with a weight. The goal is to find the subset of edges with the minimum total weight that connects all vertices.

## Approach
Prim's algorithm starts with an arbitrary vertex and grows the MST by adding the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST. This process continues until all vertices are included in the MST. The algorithm uses a priority queue to efficiently select the next edge to add.

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

            for (auto &neighbor : adj[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;

                if (!mstSet[v] && weight < key[v]) {
                    key[v] = weight;
                    parent[v] = u;
                    pq.push({key[v], v});
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
    Graph g(4);
    g.addEdge(0, 1, 10);
    g.addEdge(0, 2, 6);
    g.addEdge(0, 3, 5);
    g.addEdge(1, 3, 15);
    g.addEdge(2, 3, 4);

    cout << "Minimum Spanning Tree weight: " << g.primMST() << endl;

    return 0;
}
```

## Test Cases
```
Input: 
Vertices: 4
Edges:
(0, 1, 10)
(0, 2, 6)
(0, 3, 5)
(1, 3, 15)
(2, 3, 4)
Output: 
Minimum Spanning Tree weight: 15
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm uses a priority queue to efficiently select the next edge to add to the MST.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.