# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest path between nodes in a graph. It works with both directed and undirected graphs, and it can handle positive edge weights. The goal is to find the shortest path from a source node to all other nodes in the graph. Given a graph with n nodes and m edges, where each edge has a non-negative weight, find the shortest distance from the source node to all other nodes.

## Approach
Dijkstra's algorithm uses a greedy approach, selecting the node with the minimum distance that has not been processed yet. It maintains a priority queue to keep track of the nodes to be processed, where the priority of each node is its current shortest distance from the source node. The algorithm repeatedly extracts the node with the minimum distance from the priority queue and updates the distances of its neighbors.

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

#define INF INT_MAX

void dijkstra(vvi &graph, int source) {
    int n = graph.size();
    vi dist(n, INF);
    dist[source] = 0;
    priority_queue<pii, vpi, greater<pii>> pq;
    pq.push({0, source});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        for (int v = 0; v < n; v++) {
            if (graph[u][v] > 0 && dist[v] > dist[u] + graph[u][v]) {
                dist[v] = dist[u] + graph[u][v];
                pq.push({dist[v], v});
            }
        }
    }

    cout << "Shortest distances from source node: ";
    for (int i = 0; i < n; i++) {
        cout << dist[i] << " ";
    }
    cout << endl;
}

int main() {
    int n, m;
    cout << "Enter the number of nodes: ";
    cin >> n;
    cout << "Enter the number of edges: ";
    cin >> m;

    vvi graph(n, vi(n, 0));

    for (int i = 0; i < m; i++) {
        int u, v, w;
        cout << "Enter the source node, destination node, and weight of edge " << i + 1 << ": ";
        cin >> u >> v >> w;
        graph[u][v] = w;
    }

    int source;
    cout << "Enter the source node: ";
    cin >> source;

    dijkstra(graph, source);

    return 0;
}
```

## Test Cases
```
Input: 
Enter the number of nodes: 5
Enter the number of edges: 6
Enter the source node, destination node, and weight of edge 1: 0 1 4
Enter the source node, destination node, and weight of edge 2: 0 2 1
Enter the source node, destination node, and weight of edge 3: 1 3 1
Enter the source node, destination node, and weight of edge 4: 2 1 2
Enter the source node, destination node, and weight of edge 5: 2 3 5
Enter the source node, destination node, and weight of edge 6: 3 4 3
Enter the source node: 0
Output: 
Shortest distances from source node: 0 3 1 4 7 
```

## Key Takeaways
- Dijkstra's algorithm is a popular algorithm for finding the shortest path in a graph.
- It uses a greedy approach and a priority queue to efficiently find the shortest distances.
- The algorithm has a time complexity of O((V + E)logV) and a space complexity of O(V + E), making it suitable for large graphs.