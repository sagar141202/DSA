# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is a bipartite graph. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. The graph is represented as an adjacency list. The function should return true if the graph is bipartite and false otherwise. The graph can have up to 100 nodes and 1000 edges. For example, a graph with edges (1,2), (1,3), (2,4), (3,4) is bipartite, but a graph with edges (1,2), (2,3), (3,1) is not.

## Approach
We will use a graph traversal algorithm, specifically breadth-first search (BFS), to assign each node a color (0 or 1) and check if any edge connects two nodes of the same color. If we find such an edge, the graph is not bipartite.

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
                int node = q.front();
                q.pop();
                
                for (int neighbor : graph[node]) {
                    if (color[neighbor] == -1) {
                        color[neighbor] = 1 - color[node];
                        q.push(neighbor);
                    } else if (color[neighbor] == color[node]) {
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
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
```

## Key Takeaways
- A bipartite graph can be checked using BFS and coloring the nodes.
- If an edge connects two nodes of the same color, the graph is not bipartite.
- This algorithm has a time complexity of O(V + E) and a space complexity of O(V).