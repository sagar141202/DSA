# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list, where each vertex is associated with a list of its neighboring vertices and the corresponding edge weights. The goal is to find the MST with the minimum total edge weight.

## Approach
Prim's algorithm uses a greedy approach to find the MST by selecting the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST. This process is repeated until all vertices are included in the MST. The algorithm maintains a priority queue of vertices to be processed, where the priority of each vertex is the minimum edge weight connecting it to the MST.

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
        vector<bool> mstSet(V, false);
        key[0] = 0;
        int totalWeight = 0;

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, 0});

        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();

            if (mstSet[u]) continue;

            mstSet[u] = true;
            totalWeight += key[u];

            for (auto neighbor : adj[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;

                if (!mstSet[v] && weight < key[v]) {
                    key[v] = weight;
                    pq.push({weight, v});
                }
            }
        }

        return totalWeight;
    }
};

int main() {
    int V = 5;
    Graph graph(V);

    graph.addEdge(0, 1, 2);
    graph.addEdge(0, 3, 6);
    graph.addEdge(1, 2, 3);
    graph.addEdge(1, 3, 8);
    graph.addEdge(1, 4, 5);
    graph.addEdge(2, 4, 7);
    graph.addEdge(3, 4, 9);

    cout << "Minimum Spanning Tree weight: " << graph.primMST() << endl;

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

Output: 
Minimum Spanning Tree weight: 16
```

## Key Takeaways
- Prim's algorithm is an efficient method for finding the Minimum Spanning Tree of a connected, undirected graph.
- The algorithm uses a greedy approach to select the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST.
- The time complexity of Prim's algorithm is O(E log V) using a binary heap priority queue, where E is the number of edges and V is the number of vertices.