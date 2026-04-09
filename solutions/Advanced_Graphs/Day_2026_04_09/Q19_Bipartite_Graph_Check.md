# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. The graph is represented as an adjacency list. The function should return true if the graph is bipartite and false otherwise. The graph may contain self-loops and multiple edges between the same pair of vertices.

## Approach
The approach is to use a graph traversal algorithm (DFS or BFS) and assign each vertex a color (0 or 1) as we traverse the graph. If we encounter a vertex that has already been assigned a color and the color is different from the expected color, we return false. The algorithm will return true if we can assign colors to all vertices without encountering any conflicts.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isBipartite(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> color(n, -1);

    for (int i = 0; i < n; i++) {
        if (color[i] == -1) {
            if (!dfs(graph, color, i, 0)) {
                return false;
            }
        }
    }

    return true;
}

bool dfs(vector<vector<int>>& graph, vector<int>& color, int node, int expectedColor) {
    if (color[node] != -1) {
        return color[node] == expectedColor;
    }

    color[node] = expectedColor;
    for (int neighbor : graph[node]) {
        if (!dfs(graph, color, neighbor, 1 - expectedColor)) {
            return false;
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

    cout << boolalpha << isBipartite(graph) << endl;
    return 0;
}
```

## Test Cases
```
Input: 
4 4
0 1
1 2
2 3
3 0
Output: false

Input: 
4 4
0 1
1 2
2 3
3 0
Output: false

Input: 
5 6
0 1
0 2
1 3
1 4
2 3
3 4
Output: true
```

## Key Takeaways
- A bipartite graph can be checked using a graph traversal algorithm (DFS or BFS) and assigning colors to each vertex.
- If a vertex is already assigned a color and the color is different from the expected color, the graph is not bipartite.
- The time complexity is O(V + E) and the space complexity is O(V), where V is the number of vertices and E is the number of edges.