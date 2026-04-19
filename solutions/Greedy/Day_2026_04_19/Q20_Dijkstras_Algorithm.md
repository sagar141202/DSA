# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a graph search algorithm that finds the shortest paths between nodes in a graph. Given a weighted graph and a source node, the algorithm calculates the minimum distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix, and the algorithm assumes that all edge weights are non-negative. For example, consider a graph with nodes A, B, C, D, and E, where the edges have the following weights: A-B (1), A-C (4), B-C (2), B-D (5), C-D (1), D-E (3). If we want to find the shortest path from node A to all other nodes, Dijkstra's algorithm will return the minimum distances: A (0), B (1), C (3), D (4), E (7).

## Approach
Dijkstra's algorithm uses a greedy approach to find the shortest paths. It maintains a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighbors.

## Complexity
- Time: O((V + E)logV)
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
    }

    vector<int> dijkstra(int src) {
        vector<int> dist(V, INT_MAX);
        dist[src] = 0;

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, src});

        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();

            for (auto neighbor : adj[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;

                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    pq.push({dist[v], v});
                }
            }
        }

        return dist;
    }
};

int main() {
    Graph g(5);
    g.addEdge(0, 1, 1);
    g.addEdge(0, 2, 4);
    g.addEdge(1, 2, 2);
    g.addEdge(1, 3, 5);
    g.addEdge(2, 3, 1);
    g.addEdge(3, 4, 3);

    vector<int> dist = g.dijkstra(0);

    cout << "Shortest distances from node 0: ";
    for (int i = 0; i < 5; i++) {
        cout << dist[i] << " ";
    }
    cout << endl;

    return 0;
}
```

## Test Cases
```
Input: 
Graph with nodes A, B, C, D, E
Edges: A-B (1), A-C (4), B-C (2), B-D (5), C-D (1), D-E (3)
Source node: A

Output: 
Shortest distances from node A: 0 1 3 4 7
```

## Key Takeaways
- Dijkstra's algorithm assumes that all edge weights are non-negative.
- The algorithm uses a priority queue to efficiently select the node with the minimum distance.
- The time complexity of Dijkstra's algorithm is O((V + E)logV) using a binary heap priority queue.