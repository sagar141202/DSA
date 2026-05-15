# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list, where each edge is a tuple of (vertex, weight). The constraints are: 1 ≤ V ≤ 10^5, 1 ≤ E ≤ 10^5, and 1 ≤ weight ≤ 10^5. For example, given a graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)}, the MST has a total weight of 19.

## Approach
Prim's algorithm uses a greedy approach to find the MST. It starts with an arbitrary vertex and grows the tree by adding the minimum-weight edge that connects a vertex in the tree to a vertex not in the tree. This process is repeated until all vertices are included in the tree. The algorithm uses a priority queue to efficiently select the minimum-weight edge.

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

            for (auto &edge : adj[u]) {
                int v = edge.first;
                int weight = edge.second;

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
    Graph graph(5);
    graph.addEdge(0, 1, 10);
    graph.addEdge(0, 2, 6);
    graph.addEdge(0, 3, 5);
    graph.addEdge(1, 3, 15);
    graph.addEdge(2, 3, 4);

    cout << "Minimum Spanning Tree weight: " << graph.primMST() << endl;

    return 0;
}
```

## Test Cases
```
Input: 
Vertices: 5
Edges: [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
Output: 
Minimum Spanning Tree weight: 19
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm used to find the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm uses a priority queue to efficiently select the minimum-weight edge that connects a vertex in the tree to a vertex not in the tree.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.