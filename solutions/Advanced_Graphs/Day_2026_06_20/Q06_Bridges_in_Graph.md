# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph. The input graph is guaranteed to be connected.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and keep track of the discovery time and low value of each node. If the low value of a node is greater than the discovery time of its parent, then the edge between them is a bridge. The DFS traversal is performed recursively, and the discovery time and low value are updated accordingly.

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<int>& disc, vector<int>& low, vector<pair<int, int>>& bridges, int& time) {
    disc[node] = low[node] = time++;
    for (int neighbor : graph[node]) {
        if (disc[neighbor] == -1) {
            dfs(neighbor, node, graph, disc, low, bridges, time);
            low[node] = min(low[node], low[neighbor]);
            if (low[neighbor] > disc[node]) {
                bridges.push_back({node, neighbor});
            }
        } else if (neighbor != parent) {
            low[node] = min(low[node], disc[neighbor]);
        }
    }
}

vector<pair<int, int>> findBridges(int numNodes, vector<vector<int>>& graph) {
    vector<int> disc(numNodes, -1);
    vector<int> low(numNodes, -1);
    vector<pair<int, int>> bridges;
    int time = 0;
    for (int i = 0; i < numNodes; i++) {
        if (disc[i] == -1) {
            dfs(i, -1, graph, disc, low, bridges, time);
        }
    }
    return bridges;
}

int main() {
    int numNodes = 5;
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}};
    vector<pair<int, int>> bridges = findBridges(numNodes, graph);
    for (auto bridge : bridges) {
        cout << "(" << bridge.first << ", " << bridge.second << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: numNodes = 5, graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}}
Output: (1, 2)
        (3, 4)
```

## Key Takeaways
- The algorithm uses DFS to traverse the graph and keep track of the discovery time and low value of each node.
- If the low value of a node is greater than the discovery time of its parent, then the edge between them is a bridge.
- The time complexity of the algorithm is O(V + E), where V is the number of nodes and E is the number of edges in the graph.