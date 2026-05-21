# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph, find the Minimum Spanning Tree (MST) using Prim's algorithm. The graph is represented as an adjacency list where each node is connected to its neighboring nodes with their respective edge weights. The goal is to find a subset of edges that connect all nodes in the graph with the minimum total edge weight. The graph has 'n' nodes and 'm' edges, and the edge weights are non-negative.

## Approach
Prim's algorithm uses a greedy approach to find the MST by selecting the minimum-weight edge that connects a visited node to an unvisited node at each step. This process continues until all nodes are visited. The algorithm starts with an arbitrary node and grows the tree by adding the minimum-weight edge that connects a node in the tree to a node not yet in the tree.

## Complexity
- Time: O((V + E) log V) for binary heap implementation or O(E + V log V) for priority queue implementation
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

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.push({0, 0});

        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();

            mstSet[u] = true;

            for (const auto& edge : adj[u]) {
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
    int n, m;
    cin >> n >> m;

    Graph graph(n);

    for (int i = 0; i < m; i++) {
        int u, v, weight;
        cin >> u >> v >> weight;

        graph.addEdge(u - 1, v - 1, weight);
    }

    int totalWeight = graph.primMST();
    cout << "Minimum Spanning Tree Weight: " << totalWeight << endl;

    return 0;
}
```

## Test Cases
```
Input: 
5 7
1 2 2
1 3 3
2 3 1
2 4 1
2 5 4
3 4 5
4 5 1
Output: 
Minimum Spanning Tree Weight: 8
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm used to find the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm starts with an arbitrary node and grows the tree by adding the minimum-weight edge that connects a node in the tree to a node not yet in the tree.
- The time complexity of Prim's algorithm is O((V + E) log V) for binary heap implementation or O(E + V log V) for priority queue implementation, where 'V' is the number of vertices and 'E' is the number of edges.