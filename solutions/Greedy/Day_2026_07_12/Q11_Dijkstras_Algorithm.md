# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest paths between nodes in a graph. The problem statement is as follows: Given a weighted graph with non-negative edge weights and a source node, find the shortest distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix. The algorithm should be able to handle graphs with multiple connected components.

## Approach
Dijkstra's algorithm uses a greedy approach to find the shortest distance from the source node to all other nodes. It works by maintaining a priority queue of nodes, where the priority of each node is its current shortest distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighbors.

## Complexity
- Time: O((V + E)logV)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpi;

class Graph {
public:
    int V;
    vvi adj;

    Graph(int vertices) {
        V = vertices;
        adj.resize(V);
    }

    void addEdge(int u, int v, int w) {
        adj[u].push_back(v);
        adj[u].push_back(w);
    }

    void dijkstra(int src) {
        vector<int> dist(V, INT_MAX);
        dist[src] = 0;

        priority_queue<pii, vector<pii>, greater<pii>> pq;
        pq.push({0, src});

        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();

            for (int i = 0; i < adj[u].size(); i += 2) {
                int v = adj[u][i];
                int w = adj[u][i + 1];

                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.push({dist[v], v});
                }
            }
        }

        for (int i = 0; i < V; i++) {
            cout << "Shortest distance from " << src << " to " << i << " is " << dist[i] << endl;
        }
    }
};

int main() {
    Graph g(5);
    g.addEdge(0, 1, 4);
    g.addEdge(0, 2, 1);
    g.addEdge(1, 3, 1);
    g.addEdge(2, 1, 2);
    g.addEdge(2, 3, 5);
    g.addEdge(3, 4, 3);

    g.dijkstra(0);

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and the following edges:
(0, 1) with weight 4
(0, 2) with weight 1
(1, 3) with weight 1
(2, 1) with weight 2
(2, 3) with weight 5
(3, 4) with weight 3

Output: 
Shortest distance from 0 to 0 is 0
Shortest distance from 0 to 1 is 3
Shortest distance from 0 to 2 is 1
Shortest distance from 0 to 3 is 4
Shortest distance from 0 to 4 is 7
```

## Key Takeaways
- Dijkstra's algorithm is used for finding the shortest paths between nodes in a graph with non-negative edge weights.
- The algorithm uses a greedy approach by maintaining a priority queue of nodes and repeatedly extracting the node with the minimum priority.
- The time complexity of Dijkstra's algorithm is O((V + E)logV), where V is the number of vertices and E is the number of edges in the graph.