# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph, find the minimum spanning tree (MST) using Prim's algorithm. The graph is represented as an adjacency list, where each node is connected to its neighbors with a certain weight. The goal is to find the subset of edges that connect all nodes with the minimum total weight. For example, consider a graph with 4 nodes and the following edges: (0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4). The minimum spanning tree should have a total weight of 19 (edges: (0, 3, 5), (2, 3, 4), (0, 2, 6)).

## Approach
Prim's algorithm works by selecting a random node as the starting point, then iteratively adding the minimum-weight edge that connects a node in the MST to a node not yet in the MST. This process continues until all nodes are included in the MST. The algorithm uses a priority queue to efficiently select the minimum-weight edge.

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
        adj.resize(V);
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
    Graph with 4 nodes and edges: (0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)
Output: 
    Minimum Spanning Tree weight: 19
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm that finds the minimum spanning tree of a connected, undirected, and weighted graph.
- The algorithm uses a priority queue to efficiently select the minimum-weight edge that connects a node in the MST to a node not yet in the MST.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.