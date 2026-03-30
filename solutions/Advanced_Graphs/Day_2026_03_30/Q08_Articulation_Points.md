# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a node that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The function should return a list of all articulation points in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points. It keeps track of the discovery time and low value of each node to determine if it's an articulation point. A node is an articulation point if it has at least two children and is the root of the DFS tree, or if it's not the root and has a child that is an articulation point.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<int> &disc, vector<int> &low, vector<bool> &ap, vector<vector<int>> &graph, int &time) {
    disc[node] = low[node] = time++;
    int child = 0;
    for (int neighbor : graph[node]) {
        if (disc[neighbor] == -1) {
            child++;
            dfs(neighbor, node, disc, low, ap, graph, time);
            low[node] = min(low[node], low[neighbor]);
            if (parent == -1 && child > 1) {
                ap[node] = true;
            }
            if (parent != -1 && low[neighbor] >= disc[node]) {
                ap[node] = true;
            }
        } else if (neighbor != parent) {
            low[node] = min(low[node], disc[neighbor]);
        }
    }
}

vector<int> findArticulationPoints(vector<vector<int>> &graph) {
    int n = graph.size();
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> ap(n, false);
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (disc[i] == -1) {
            dfs(i, -1, disc, low, ap, graph, time);
        }
    }
    vector<int> result;
    for (int i = 0; i < n; i++) {
        if (ap[i]) {
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    int n = 5;
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}};
    vector<int> result = findArticulationPoints(graph);
    for (int node : result) {
        cout << node << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: 
Graph:
0 -- 1
1 -- 0
1 -- 2
2 -- 1
2 -- 3
3 -- 2
3 -- 4
4 -- 3

Output: 
1 3
```

## Key Takeaways
- Articulation points are critical nodes in a graph that, when removed, increase the number of connected components.
- The algorithm uses DFS to identify articulation points by tracking discovery time and low values.
- A node is an articulation point if it has at least two children and is the root of the DFS tree, or if it's not the root and has a child that is an articulation point.