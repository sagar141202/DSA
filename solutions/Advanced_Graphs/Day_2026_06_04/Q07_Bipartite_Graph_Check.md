# Bipartite Graph Check

## Problem Statement
Given an undirected graph, check if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that every edge connects two vertices from different sets. The graph is represented as an adjacency list. The function should return true if the graph is bipartite and false otherwise. The graph can have multiple connected components. The number of vertices in the graph is denoted by 'n' and the number of edges is denoted by 'm'. 1 ≤ n ≤ 10^5, 1 ≤ m ≤ 10^5.

## Approach
To check if a graph is bipartite, we can use a graph traversal algorithm such as BFS or DFS and assign colors to the vertices. If we find an edge between two vertices of the same color, the graph is not bipartite. We will use BFS for this solution. 

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
1 2
2 3
3 0
Output: The graph is not bipartite.
```

## Key Takeaways
- A graph is bipartite if and only if it contains no odd cycles.
- We can use BFS or DFS to check if a graph is bipartite by assigning colors to the vertices.
- The time complexity of this solution is O(n + m), where n is the number of vertices and m is the number of edges.