# Bipartite Graph Check

## Problem Statement
Given an undirected graph, check if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. The graph is represented as an adjacency list. The function should return true if the graph is bipartite, false otherwise. The graph has n vertices and m edges. 1 ≤ n ≤ 10^5, 1 ≤ m ≤ 10^5.

## Approach
We will use a breadth-first search (BFS) traversal to assign colors to each vertex. If we encounter a vertex with the same color as its neighbor, the graph is not bipartite. We start by assigning a color to the first vertex and then alternate colors for its neighbors.

## Complexity
- Time: O(n + m)
- Space: O(n)

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
0 2
1 3
2 3
Output: true

Input: 
4 4
0 1
0 2
1 2
1 3
Output: false
```

## Key Takeaways
- A graph is bipartite if it can be colored with two colors such that no two adjacent vertices have the same color.
- BFS traversal can be used to assign colors to vertices and check for bipartiteness.
- The time complexity of this solution is O(n + m), where n is the number of vertices and m is the number of edges.