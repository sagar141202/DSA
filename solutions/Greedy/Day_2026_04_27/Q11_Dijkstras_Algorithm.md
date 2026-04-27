# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest path between nodes in a graph. It works with weighted graphs, where each edge has a weight or cost associated with it. Given a source node, the algorithm calculates the minimum distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or adjacency matrix. The algorithm assumes that all edge weights are non-negative. If the graph contains negative weight edges, a different algorithm such as Bellman-Ford should be used.

## Approach
Dijkstra's algorithm uses a greedy approach, selecting the node with the minimum distance that has not been processed yet. It maintains a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighbors.

## Complexity
- Time: O((V + E)logV)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for a graph edge
struct Edge {
    int dest;
    int weight;
};

// Define the structure for a graph node
struct Node {
    int id;
    int dist;
};

// Comparison function for the priority queue
struct compare {
    bool operator()(const Node& a, const Node& b) {
        return a.dist > b.dist;
    }
};

// Function to implement Dijkstra's algorithm
void dijkstra(vector<vector<Edge>>& graph, int source) {
    int V = graph.size();
    vector<int> dist(V, INT_MAX);
    dist[source] = 0;

    priority_queue<Node, vector<Node>, compare> pq;
    pq.push({source, 0});

    while (!pq.empty()) {
        Node curr = pq.top();
        pq.pop();

        for (const Edge& edge : graph[curr.id]) {
            int newDist = curr.dist + edge.weight;
            if (newDist < dist[edge.dest]) {
                dist[edge.dest] = newDist;
                pq.push({edge.dest, newDist});
            }
        }
    }

    // Print the shortest distances
    for (int i = 0; i < V; i++) {
        cout << "Shortest distance from " << source << " to " << i << ": " << dist[i] << endl;
    }
}

int main() {
    int V = 6;
    vector<vector<Edge>> graph(V);

    // Add edges to the graph
    graph[0].push_back({1, 4});
    graph[0].push_back({2, 2});
    graph[1].push_back({3, 5});
    graph[2].push_back({1, 1});
    graph[2].push_back({3, 8});
    graph[2].push_back({4, 10});
    graph[3].push_back({4, 2});
    graph[3].push_back({5, 6});
    graph[4].push_back({5, 3});

    int source = 0;
    dijkstra(graph, source);

    return 0;
}
```

## Test Cases
```
Input:
Graph with 6 nodes and the following edges:
0 -> 1 (weight: 4)
0 -> 2 (weight: 2)
1 -> 3 (weight: 5)
2 -> 1 (weight: 1)
2 -> 3 (weight: 8)
2 -> 4 (weight: 10)
3 -> 4 (weight: 2)
3 -> 5 (weight: 6)
4 -> 5 (weight: 3)
Source node: 0

Output:
Shortest distance from 0 to 0: 0
Shortest distance from 0 to 1: 3
Shortest distance from 0 to 2: 2
Shortest distance from 0 to 3: 8
Shortest distance from 0 to 4: 10
Shortest distance from 0 to 5: 13
```

## Key Takeaways
- Dijkstra's algorithm is a popular choice for finding the shortest path in a weighted graph with non-negative edge weights.
- The algorithm uses a greedy approach, selecting the node with the minimum distance that has not been processed yet.
- The time complexity of Dijkstra's algorithm is O((V + E)logV) using a priority queue, where V is the number of vertices and E is the number of edges.