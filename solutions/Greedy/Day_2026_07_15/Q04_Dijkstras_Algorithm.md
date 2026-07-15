# Dijkstra's Algorithm

## Problem Statement
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest path between nodes in a graph. Given a weighted graph and a source node, the algorithm calculates the minimum distance from the source node to all other nodes in the graph. The graph can be represented as an adjacency list or an adjacency matrix, and the algorithm assumes that all edge weights are non-negative. The problem statement can be formalized as follows: given a graph G = (V, E) with non-negative edge weights, and a source node s, find the shortest path from s to all other nodes in the graph.

## Approach
Dijkstra's algorithm uses a greedy approach to find the shortest path, by always choosing the node with the minimum distance that has not been visited yet. The algorithm maintains a priority queue of nodes, where the priority of each node is its minimum distance from the source node. The algorithm repeatedly extracts the node with the minimum priority from the queue and updates the distances of its neighbors.

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
};

struct compare {
    bool operator()(const Node& a, const Node& b) {
        return a.distance > b.distance;
    }
};

vector<int> dijkstra(vector<vector<pair<int, int>>>& graph, int source) {
    int n = graph.size();
    vector<int> distances(n, INT_MAX);
    distances[source] = 0;
    priority_queue<Node, vector<Node>, compare> queue;
    queue.push(Node(source, 0));

    while (!queue.empty()) {
        Node node = queue.top();
        queue.pop();
        int u = node.id;
        int distance = node.distance;

        for (auto& neighbor : graph[u]) {
            int v = neighbor.first;
            int weight = neighbor.second;
            if (distance + weight < distances[v]) {
                distances[v] = distance + weight;
                queue.push(Node(v, distances[v]));
            }
        }
    }

    return distances;
}

int main() {
    int n = 5;
    vector<vector<pair<int, int>>> graph(n);
    graph[0].push_back({1, 4});
    graph[0].push_back({2, 1});
    graph[1].push_back({3, 1});
    graph[2].push_back({1, 2});
    graph[2].push_back({3, 5});
    graph[3].push_back({4, 3});

    int source = 0;
    vector<int> distances = dijkstra(graph, source);

    for (int i = 0; i < n; i++) {
        cout << "Distance from " << source << " to " << i << ": " << distances[i] << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph:
0 --4--> 1
0 --1--> 2
1 --1--> 3
2 --2--> 1
2 --5--> 3
3 --3--> 4
Source: 0

Output: 
Distance from 0 to 0: 0
Distance from 0 to 1: 3
Distance from 0 to 2: 1
Distance from 0 to 3: 4
Distance from 0 to 4: 7
```

## Key Takeaways
- Dijkstra's algorithm assumes that all edge weights are non-negative.
- The algorithm uses a priority queue to efficiently select the node with the minimum distance.
- The time complexity of Dijkstra's algorithm is O((V + E)logV) using a binary heap priority queue.