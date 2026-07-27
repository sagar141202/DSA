# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest path between nodes in a graph. Given a weighted graph and a source node, the algorithm calculates the minimum distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix. The algorithm assumes that the graph does not contain any negative weight edges. For example, consider a graph with nodes A, B, C, D, and E, where the edges have the following weights: A-B = 1, A-C = 4, B-C = 2, B-D = 5, C-D = 1, D-E = 3. If we want to find the shortest path from node A to all other nodes, Dijkstra's algorithm will return the minimum distances.

## Approach
Dijkstra's algorithm works by maintaining a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighboring nodes. This process continues until all nodes have been processed.

## Complexity
- Time: O((V + E)logV)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int id;
    int distance;
    Node(int id, int distance) : id(id), distance(distance) {}
    bool operator<(const Node& other) const {
        return distance > other.distance;
    }
};

vector<int> dijkstra(vector<vector<pair<int, int>>>& graph, int source) {
    int n = graph.size();
    vector<int> distances(n, INT_MAX);
    distances[source] = 0;
    priority_queue<Node> pq;
    pq.push(Node(source, 0));

    while (!pq.empty()) {
        Node node = pq.top();
        pq.pop();

        for (auto& neighbor : graph[node.id]) {
            int newDistance = node.distance + neighbor.second;
            if (newDistance < distances[neighbor.first]) {
                distances[neighbor.first] = newDistance;
                pq.push(Node(neighbor.first, newDistance));
            }
        }
    }

    return distances;
}

int main() {
    int n = 5;
    vector<vector<pair<int, int>>> graph(n);
    graph[0].push_back({1, 1});
    graph[0].push_back({2, 4});
    graph[1].push_back({2, 2});
    graph[1].push_back({3, 5});
    graph[2].push_back({3, 1});
    graph[3].push_back({4, 3});

    vector<int> distances = dijkstra(graph, 0);
    for (int i = 0; i < n; i++) {
        cout << "Shortest distance from node 0 to node " << i << ": " << distances[i] << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with nodes A, B, C, D, E
Edges: A-B = 1, A-C = 4, B-C = 2, B-D = 5, C-D = 1, D-E = 3
Source node: A
Output: 
Shortest distance from node A to node 0: 0
Shortest distance from node A to node 1: 1
Shortest distance from node A to node 2: 3
Shortest distance from node A to node 3: 4
Shortest distance from node A to node 4: 7
```

## Key Takeaways
- Dijkstra's algorithm is used for finding the shortest path between nodes in a weighted graph.
- The algorithm assumes that the graph does not contain any negative weight edges.
- The time complexity of Dijkstra's algorithm is O((V + E)logV), where V is the number of vertices and E is the number of edges.