# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge in a graph is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify bridges. It keeps track of the discovery time and low value for each node, and checks if the low value of a neighboring node is greater than the discovery time of the current node.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<int>& disc, vector<int>& low, vector<bool>& visited, vector<pair<int, int>>& bridges, int& time) {
    disc[node] = low[node] = time++;
    visited[node] = true;

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

vector<pair<int, int>> findBridges(int n, vector<vector<int>>& graph) {
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> visited(n, false);
    vector<pair<int, int>> bridges;
    int time = 0;

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1, graph, disc, low, visited, bridges, time);
        }
    }

    return bridges;
}

int main() {
    int n = 5;
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}};

    vector<pair<int, int>> bridges = findBridges(n, graph);

    for (auto& bridge : bridges) {
        cout << "(" << bridge.first << ", " << bridge.second << ")" << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
n = 5
graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}}
Output: 
(1, 2)
(3, 4)
```

## Key Takeaways
- Use DFS to traverse the graph and identify bridges.
- Keep track of the discovery time and low value for each node to determine if an edge is a bridge.
- A bridge is an edge that, when removed, increases the number of connected components in the graph.