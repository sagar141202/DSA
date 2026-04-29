# Bridges in Graph

## Problem Statement
Given an undirected graph, find all bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of neighboring nodes. The graph can have at most 100 nodes and 1000 edges. For example, in a graph with nodes 0, 1, 2, and 3, and edges (0, 1), (1, 2), (2, 3), the edge (1, 2) is a bridge because removing it would disconnect the graph into two components.

## Approach
The approach to finding bridges in a graph involves using a depth-first search (DFS) algorithm to traverse the graph and keep track of the discovery time and low value of each node. The discovery time is the time at which the node is first visited, and the low value is the smallest discovery time that can be reached from the node. If the low value of a node is greater than the discovery time of its parent, then the edge between the node and its parent is a bridge.

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

vector<pair<int, int>> findBridges(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (vector<int>& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    
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
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {1, 4}};
    vector<pair<int, int>> bridges = findBridges(n, edges);
    for (pair<int, int>& bridge : bridges) {
        cout << "(" << bridge.first << ", " << bridge.second << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
n = 5
edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: 
(1, 3)
(1, 4)
```

## Key Takeaways
- The algorithm uses DFS to traverse the graph and keep track of the discovery time and low value of each node.
- A bridge is detected when the low value of a node is greater than the discovery time of its parent.
- The algorithm has a time complexity of O(V + E) and a space complexity of O(V), where V is the number of nodes and E is the number of edges.