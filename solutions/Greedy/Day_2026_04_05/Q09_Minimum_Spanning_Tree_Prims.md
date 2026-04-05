# Minimum Spanning Tree (Prim's)

## Problem Statement
Given an undirected and connected graph with non-negative edge weights, find the minimum spanning tree (MST) of the graph using Prim's algorithm. The graph is represented as an adjacency list, where each node is associated with a list of its neighboring nodes and the corresponding edge weights. The MST is a subgraph that connects all nodes in the graph with the minimum total edge weight. For example, given a graph with 5 nodes and the following edges: (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), the minimum spanning tree will have edges (0, 1, 2), (1, 2, 3), (0, 3, 6), (1, 4, 5) with a total weight of 2 + 3 + 6 + 5 = 16.

## Approach
Prim's algorithm is a greedy algorithm that starts with an arbitrary node and grows the tree by adding the minimum-weight edge that connects a node in the tree to a node not yet in the tree. The algorithm uses a priority queue to efficiently select the minimum-weight edge. The algorithm runs until all nodes are included in the tree.

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

        int weight = 0;
        for (int i = 1; i < V; i++) {
            weight += key[i];
        }

        return weight;
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

    int mstWeight = graph.primMST();
    cout << "Minimum Spanning Tree weight: " << mstWeight << endl;

    return 0;
}
```

## Test Cases
```
Input:
5
0 1 2
0 3 6
1 2 3
1 3 8
1 4 5
2 4 7

Output:
Minimum Spanning Tree weight: 16
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm used to find the minimum spanning tree of a graph.
- The algorithm uses a priority queue to efficiently select the minimum-weight edge.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.