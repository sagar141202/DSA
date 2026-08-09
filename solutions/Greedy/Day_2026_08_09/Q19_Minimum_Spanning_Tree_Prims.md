# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, the task is to find the Minimum Spanning Tree (MST) of the graph using Prim's algorithm. The MST is a subgraph that connects all the vertices together while minimizing the total edge weight. The graph is represented as an adjacency list, where each edge is a tuple of (u, v, w) representing an edge between vertices u and v with weight w. The constraints are 1 ≤ V ≤ 10^5 and 1 ≤ E ≤ 10^6.

## Approach
Prim's algorithm is a greedy algorithm that works by selecting the minimum-weight edge that connects a vertex in the MST to a vertex not yet in the MST. This process is repeated until all vertices are included in the MST. The algorithm uses a priority queue to efficiently select the minimum-weight edge.

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

    void addEdge(int u, int v, int w) {
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
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

            if (mstSet[u]) continue;

            mstSet[u] = true;

            for (auto neighbor : adj[u]) {
                int v = neighbor.first;
                int w = neighbor.second;
                if (!mstSet[v] && w < key[v]) {
                    key[v] = w;
                    parent[v] = u;
                    pq.push({w, v});
                }
            }
        }

        int weight = 0;
        for (int i = 1; i < V; i++) {
            weight += key[i];
        }

        return weight;
    }
};

int main() {
    int V = 4;
    Graph g(V);
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
Graph with 4 vertices and 5 edges:
(0, 1, 10)
(0, 2, 6)
(0, 3, 5)
(1, 3, 15)
(2, 3, 4)
Output: Minimum Spanning Tree weight: 15

Input: 
Graph with 5 vertices and 7 edges:
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
- Prim's algorithm is suitable for finding the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm uses a priority queue to efficiently select the minimum-weight edge.
- The time complexity of Prim's algorithm is O(E log V) and the space complexity is O(V + E).