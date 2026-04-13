# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite, meaning it can be colored with two colors such that no two adjacent vertices have the same color. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its adjacent vertices. The function should return true if the graph is bipartite and false otherwise. For example, a graph with vertices 0, 1, 2, and 3, and edges (0, 1), (1, 2), (2, 3), and (3, 0) is not bipartite.

## Approach
The algorithm uses a breadth-first search (BFS) traversal to assign colors to each vertex. If a vertex is already colored and its color matches the expected color, the graph is not bipartite. The intuition is to alternate between two colors for each level of the BFS traversal.

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
            queue<int> q;
            q.push(i);
            color[i] = 0;
            
            while (!q.empty()) {
                int vertex = q.front();
                q.pop();
                
                for (int adjacent : graph[vertex]) {
                    if (color[adjacent] == -1) {
                        color[adjacent] = 1 - color[vertex];
                        q.push(adjacent);
                    } else if (color[adjacent] == color[vertex]) {
                        return false;
                    }
                }
            }
        }
    }
    
    return true;
}
```

## Test Cases
```
Input: graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
Output: false
Input: graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
Output: false
Input: graph = [[1], [0, 2], [1]]
Output: true
```

## Key Takeaways
- A bipartite graph can be colored with two colors such that no two adjacent vertices have the same color.
- BFS traversal is used to assign colors to each vertex.
- If a vertex is already colored and its color matches the expected color, the graph is not bipartite.