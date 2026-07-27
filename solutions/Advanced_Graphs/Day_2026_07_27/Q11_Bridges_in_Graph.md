# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph. For example, given a graph with 5 nodes and the following edges: (0, 1), (1, 2), (2, 0), (1, 3), (1, 4), the function should return [(1, 3), (1, 4)], because removing either of these edges would increase the number of connected components in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and find the bridges. It keeps track of the discovery time and low value of each node, and uses these values to determine if an edge is a bridge. If the low value of a node is greater than the discovery time of its parent, then the edge between them is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<int>& disc, vector<int>& low, vector<bool>& visited, vector<pair<int, int>>& bridges, int& time) {
    visited[node] = true;
    disc[node] = low[node] = time++;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, node, graph, disc, low, visited, bridges, time);
            low[node] = min(low[node], low[neighbor]);
            if (low[neighbor] > disc[node]) {
                bridges.push_back({node, neighbor});
            }
        } else if (neighbor != parent) {
            low[node] = min(low[node], disc[neighbor]);
        }
    }
}

vector<pair<int, int>> findBridges(int numNodes, vector<vector<int>>& edges) {
    vector<vector<int>> graph(numNodes);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    vector<int> disc(numNodes, -1), low(numNodes, -1);
    vector<bool> visited(numNodes, false);
    vector<pair<int, int>> bridges;
    int time = 0;
    for (int i = 0; i < numNodes; i++) {
        if (!visited[i]) {
            dfs(i, -1, graph, disc, low, visited, bridges, time);
        }
    }
    return bridges;
}

int main() {
    int numNodes = 5;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {1, 4}};
    vector<pair<int, int>> bridges = findBridges(numNodes, edges);
    for (auto& bridge : bridges) {
        cout << "(" << bridge.first << ", " << bridge.second << ") ";
    }
    return 0;
}
```

## Test Cases
```
Input: numNodes = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: [(1, 3), (1, 4)]
```

## Key Takeaways
- Use DFS to traverse the graph and find the bridges.
- Keep track of the discovery time and low value of each node to determine if an edge is a bridge.
- If the low value of a node is greater than the discovery time of its parent, then the edge between them is a bridge.