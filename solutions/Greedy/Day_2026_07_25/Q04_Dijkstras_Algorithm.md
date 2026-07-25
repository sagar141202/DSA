# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest paths between nodes in a graph. Given a weighted graph with non-negative edge weights and a source node, the algorithm aims to find the shortest distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or adjacency matrix. The algorithm should handle graphs with multiple nodes and edges, and it should be able to find the shortest distance to all nodes, even if there are multiple paths to a node.

## Approach
Dijkstra's algorithm uses a greedy approach, where it selects the node with the minimum distance that has not been processed yet. It maintains a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighboring nodes.

## Complexity
- Time: O((V + E)logV)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

void dijkstra(vvii &graph, int source) {
    int V = graph.size();
    vi dist(V, INT_MAX);
    dist[source] = 0;
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({0, source});

    while (!pq.empty()) {
        int d = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        for (auto &neighbor : graph[u]) {
            int v = neighbor.first;
            int weight = neighbor.second;
            if (dist[v] > dist[u] + weight) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    cout << "Vertex \tDistance from Source" << endl;
    for (int i = 0; i < V; i++) {
        cout << i << "\t" << dist[i] << endl;
    }
}

int main() {
    int V = 6;
    vvii graph(V);
    graph[0].push_back({1, 4});
    graph[0].push_back({2, 2});
    graph[1].push_back({3, 5});
    graph[2].push_back({1, 1});
    graph[2].push_back({3, 8});
    graph[2].push_back({4, 10});
    graph[3].push_back({4, 2});
    graph[3].push_back({5, 6});
    graph[4].push_back({5, 3});

    dijkstra(graph, 0);
    return 0;
}
```

## Test Cases
```
Input: 
Graph with 6 vertices and the following edges:
0 -> 1 (weight: 4)
0 -> 2 (weight: 2)
1 -> 3 (weight: 5)
2 -> 1 (weight: 1)
2 -> 3 (weight: 8)
2 -> 4 (weight: 10)
3 -> 4 (weight: 2)
3 -> 5 (weight: 6)
4 -> 5 (weight: 3)
Source vertex: 0

Output: 
Vertex  Distance from Source
0       0
1       3
2       2
3       8
4       10
5       13
```

## Key Takeaways
- Dijkstra's algorithm is a greedy algorithm that finds the shortest paths between nodes in a graph.
- The algorithm maintains a priority queue of nodes, where the priority of each node is its minimum distance from the source node.
- The time complexity of Dijkstra's algorithm is O((V + E)logV) using a binary heap, where V is the number of vertices and E is the number of edges in the graph.