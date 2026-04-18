# Articulation Points

## Problem Statement
Given an undirected graph, find all articulation points. An articulation point is a node in a graph that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list. The function should return a list of all articulation points in the graph. For example, in a graph with nodes {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (1, 3), (1, 4)}, the articulation points are {1}.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points. It keeps track of the discovery time and low value for each node. If the low value of a node is greater than or equal to its discovery time, and it is not the root node, then it is an articulation point.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<int>& visited, 
         vector<int>& disc, vector<int>& low, vector<int>& articulationPoints, int& time) {
    visited[node] = 1;
    disc[node] = low[node] = time++;
    int childCount = 0;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            childCount++;
            dfs(neighbor, node, graph, visited, disc, low, articulationPoints, time);
            low[node] = min(low[node], low[neighbor]);
            if (parent == -1 && childCount > 1) {
                articulationPoints.push_back(node);
            } else if (parent != -1 && low[neighbor] >= disc[node]) {
                articulationPoints.push_back(node);
            }
        } else if (neighbor != parent) {
            low[node] = min(low[node], disc[neighbor]);
        }
    }
}

vector<int> findArticulationPoints(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    vector<int> visited(n, 0);
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<int> articulationPoints;
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1, graph, visited, disc, low, articulationPoints, time);
        }
    }
    return articulationPoints;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {1, 4}};
    vector<int> articulationPoints = findArticulationPoints(n, edges);
    for (int point : articulationPoints) {
        cout << point << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: [1]
```

## Key Takeaways
- Articulation points are nodes that, when removed, increase the number of connected components in the graph.
- The algorithm uses DFS to traverse the graph and identify articulation points.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges.