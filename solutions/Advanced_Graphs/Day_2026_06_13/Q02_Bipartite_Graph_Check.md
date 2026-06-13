# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is a bipartite graph. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. The graph is represented as an adjacency list. The function should return true if the graph is bipartite and false otherwise. The graph can have up to 100 nodes and 1000 edges. The nodes are numbered from 1 to n.

## Approach
We can use a graph traversal algorithm such as BFS or DFS to assign each node a color (0 or 1) and check if any adjacent nodes have the same color. If we find any adjacent nodes with the same color, we return false. Otherwise, we return true. The algorithm will iterate over all nodes in the graph.

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

bool dfs(vector<vector<int>>& graph, vector<int>& color, int node, int currColor) {
    if (color[node] != -1) {
        return color[node] == currColor;
    }

    color[node] = currColor;

    for (int neighbor : graph[node]) {
        if (!dfs(graph, color, neighbor, !currColor)) {
            return false;
        }
    }

    return true;
}
```

## Test Cases
```
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
```

## Key Takeaways
- Use DFS or BFS to traverse the graph and assign colors to each node.
- If any adjacent nodes have the same color, the graph is not bipartite.
- The time complexity is O(V + E) and the space complexity is O(V) due to the recursive call stack and the color array.