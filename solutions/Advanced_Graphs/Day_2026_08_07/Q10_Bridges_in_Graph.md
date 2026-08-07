# Bridges in Graph

## Problem Statement
Given an undirected graph, find all the bridges in the graph. A bridge in a graph is an edge that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of pairs, where each pair represents a bridge in the graph.

## Approach
We will use Depth-First Search (DFS) to traverse the graph and find the bridges. The algorithm will keep track of the discovery time and low value of each node to determine if an edge is a bridge. If the low value of a node is greater than the discovery time of its parent, then the edge between them is a bridge.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<int> &disc, vector<int> &low, vector<vector<int>> &graph, vector<pair<int, int>> &bridges, int &time) {
    disc[node] = low[node] = time++;
    for (int neighbor : graph[node]) {
        if (disc[neighbor] == -1) {
            dfs(neighbor, node, disc, low, graph, bridges, time);
            low[node] = min(low[node], low[neighbor]);
            if (low[neighbor] > disc[node]) {
                bridges.push_back({node, neighbor});
            }
        } else if (neighbor != parent) {
            low[node] = min(low[node], disc[neighbor]);
        }
    }
}

vector<pair<int, int>> findBridges(int n, vector<vector<int>> &graph) {
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<pair<int, int>> bridges;
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (disc[i] == -1) {
            dfs(i, -1, disc, low, graph, bridges, time);
        }
    }
    return bridges;
}

int main() {
    int n = 5;
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}};
    vector<pair<int, int>> bridges = findBridges(n, graph);
    for (pair<int, int> bridge : bridges) {
        cout << "(" << bridge.first << ", " << bridge.second << ")" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}}
Output: (1, 2)
        (3, 4)
```

## Key Takeaways
- Bridges in a graph are edges that, when removed, increase the number of connected components.
- DFS can be used to find bridges in a graph by keeping track of the discovery time and low value of each node.
- The low value of a node is the minimum discovery time of all nodes that can be reached from it.