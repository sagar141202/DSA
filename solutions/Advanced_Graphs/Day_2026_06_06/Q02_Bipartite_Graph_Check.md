# Bipartite Graph Check

## Problem Statement
Given an undirected graph, check if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. The graph is represented as an adjacency list. The function should return true if the graph is bipartite, and false otherwise. The graph can have multiple connected components.

## Approach
We can use a graph traversal algorithm (DFS or BFS) to assign colors to each vertex. If we encounter a vertex that has the same color as its neighbor, the graph is not bipartite. We will use BFS for this implementation.

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
- A bipartite graph can be checked using BFS or DFS traversal.
- Assigning colors to vertices and checking for adjacent vertices with the same color is an efficient approach.
- This algorithm works for both connected and disconnected graphs.