# Bipartite Graph Check

## Problem Statement
Given an undirected graph with n vertices and m edges, determine if the graph is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that every edge connects two vertices from different sets. The graph is represented as an adjacency list where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The function should return true if the graph is bipartite and false otherwise.

## Approach
We can use a graph traversal algorithm such as Breadth-First Search (BFS) or Depth-First Search (DFS) to assign each vertex a color (0 or 1) and check if any edge connects two vertices with the same color. If we find such an edge, the graph is not bipartite. We will use DFS for this solution.

## Complexity
- Time: O(n + m)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isBipartite(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> color(n, -1); // -1: not colored, 0: color 1, 1: color 2

    for (int i = 0; i < n; i++) {
        if (color[i] == -1) {
            if (!dfs(graph, color, i, 0)) {
                return false;
            }
        }
    }

    return true;
}

bool dfs(vector<vector<int>>& graph, vector<int>& color, int node, int currColor) {
    color[node] = currColor;

    for (int neighbor : graph[node]) {
        if (color[neighbor] == -1) {
            if (!dfs(graph, color, neighbor, 1 - currColor)) {
                return false;
            }
        } else if (color[neighbor] == currColor) {
            return false; // same color, not bipartite
        }
    }

    return true;
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

    if (isBipartite(graph)) {
        cout << "The graph is bipartite." << endl;
    } else {
        cout << "The graph is not bipartite." << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
5 6
0 1
0 2
1 3
1 4
2 3
2 4
Output: The graph is bipartite.

Input: 
4 4
0 1
0 2
1 2
1 3
Output: The graph is not bipartite.
```

## Key Takeaways
- Use DFS or BFS to traverse the graph and assign colors to vertices.
- If an edge connects two vertices with the same color, the graph is not bipartite.
- The time complexity of the solution is O(n + m), where n is the number of vertices and m is the number of edges.