# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory for finding the shortest paths between nodes in a graph. Given a graph with non-negative edge weights and a source vertex, the goal is to find the shortest distance from the source vertex to all other vertices in the graph. The graph can be represented as an adjacency list or adjacency matrix, and the algorithm should handle both cases. The algorithm should also be able to handle graphs with multiple connected components.

## Approach
The algorithm works by maintaining a priority queue of vertices, where the priority of each vertex is its current shortest distance from the source vertex. The algorithm iteratively extracts the vertex with the minimum priority from the queue, updates the distances of its neighbors, and inserts them back into the queue if necessary. This process continues until the queue is empty, at which point the shortest distances from the source vertex to all other vertices have been computed.

## Complexity
- Time: O((V + E)logV)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent a graph edge
struct Edge {
    int vertex;
    int weight;
};

// Define a comparison function for the priority queue
struct compare {
    bool operator()(const pair<int, int>& a, const pair<int, int>& b) {
        return a.second > b.second;
    }
};

// Function to implement Dijkstra's algorithm
void dijkstra(vector<vector<Edge>>& graph, int source, vector<int>& distances) {
    int V = graph.size();
    distances.assign(V, INT_MAX);
    distances[source] = 0;

    // Create a priority queue to store vertices to be processed
    priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;
    pq.push({source, 0});

    while (!pq.empty()) {
        int vertex = pq.top().first;
        int dist = pq.top().second;
        pq.pop();

        // Process all neighbors of the current vertex
        for (const auto& edge : graph[vertex]) {
            int neighbor = edge.vertex;
            int weight = edge.weight;

            // Update the distance to the neighbor if a shorter path is found
            if (dist + weight < distances[neighbor]) {
                distances[neighbor] = dist + weight;
                pq.push({neighbor, distances[neighbor]});
            }
        }
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

    // Run Dijkstra's algorithm
    vector<int> distances(V);
    dijkstra(graph, 0, distances);

    // Print the shortest distances
    for (int i = 0; i < V; i++) {
        cout << "Shortest distance from vertex 0 to vertex " << i << ": " << distances[i] << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with vertices 0-5 and the following edges:
(0, 1) with weight 4
(0, 2) with weight 2
(1, 3) with weight 5
(2, 1) with weight 1
(2, 3) with weight 8
(2, 4) with weight 10
(3, 4) with weight 2
(3, 5) with weight 6
(4, 5) with weight 3

Output: 
Shortest distance from vertex 0 to vertex 0: 0
Shortest distance from vertex 0 to vertex 1: 3
Shortest distance from vertex 0 to vertex 2: 2
Shortest distance from vertex 0 to vertex 3: 8
Shortest distance from vertex 0 to vertex 4: 10
Shortest distance from vertex 0 to vertex 5: 13
```

## Key Takeaways
- Dijkstra's algorithm is a powerful tool for finding the shortest paths in a graph.
- The algorithm works by maintaining a priority queue of vertices, where the priority of each vertex is its current shortest distance from the source vertex.
- The algorithm has a time complexity of O((V + E)logV) and a space complexity of O(V + E), making it efficient for large graphs.