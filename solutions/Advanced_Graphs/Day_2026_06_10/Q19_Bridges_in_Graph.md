# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The graph may contain self-loops and multiple edges between the same pair of nodes. The task is to identify all the bridges in the graph and return them as a list of pairs of nodes.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify bridges by keeping track of the discovery time and low value of each node. A bridge is detected when the low value of a neighboring node is greater than the discovery time of the current node.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<int>& disc, vector<int>& low, vector<vector<int>>& bridges, int& time) {
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

vector<vector<int>> findBridges(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    vector<int> disc(n, -1), low(n, -1);
    vector<vector<int>> bridges;
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (disc[i] == -1) {
            dfs(i, -1, graph, disc, low, bridges, time);
        }
    }
    return bridges;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {3, 4}};
    vector<vector<int>> bridges = findBridges(n, edges);
    for (auto& bridge : bridges) {
        cout << bridge[0] << " " << bridge[1] << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
Output: 1 3
        3 4
```

## Key Takeaways
- The algorithm uses DFS to traverse the graph and identify bridges.
- The discovery time and low value of each node are used to detect bridges.
- The time complexity of the algorithm is O(V + E), where V is the number of nodes and E is the number of edges.