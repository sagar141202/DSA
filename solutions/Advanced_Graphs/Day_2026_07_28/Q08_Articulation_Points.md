# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a vertex that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The graph has 'n' vertices and 'm' edges. The constraints are 1 ≤ n ≤ 10^5 and 1 ≤ m ≤ 10^5.

## Approach
We will use Depth-First Search (DFS) to find the articulation points. The algorithm works by maintaining a timer for the discovery time of each vertex and the low value, which is the smallest discovery time reachable from the current vertex. If the current vertex is a cut vertex (articulation point), then the low value of its child must be greater than or equal to the discovery time of the current vertex.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int vertex, int parent, vector<vector<int>>& graph, vector<bool>& visited, vector<int>& disc, vector<int>& low, vector<bool>& ap, int& time) {
    visited[vertex] = true;
    disc[vertex] = low[vertex] = time++;
    int child = 0;
    for (int neighbor : graph[vertex]) {
        if (!visited[neighbor]) {
            child++;
            dfs(neighbor, vertex, graph, visited, disc, low, ap, time);
            low[vertex] = min(low[vertex], low[neighbor]);
            if (parent == -1 && child > 1) {
                ap[vertex] = true;
            } else if (parent != -1 && low[neighbor] >= disc[vertex]) {
                ap[vertex] = true;
            }
        } else if (neighbor != parent) {
            low[vertex] = min(low[vertex], disc[neighbor]);
        }
    }
}

void findArticulationPoints(int n, vector<vector<int>>& graph) {
    vector<bool> visited(n, false);
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> ap(n, false);
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1, graph, visited, disc, low, ap, time);
        }
    }
    for (int i = 0; i < n; i++) {
        if (ap[i]) {
            cout << i << " ";
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    findArticulationPoints(n, graph);
    return 0;
}
```

## Test Cases
```
Input: 
5 5
0 1
1 2
2 0
1 3
1 4
Output: 1 
```

## Key Takeaways
- Articulation points are critical vertices in a graph that, when removed, increase the number of connected components.
- DFS is a suitable algorithm for finding articulation points due to its ability to traverse the graph and maintain discovery times and low values.
- The algorithm has a time complexity of O(n + m), making it efficient for large graphs.