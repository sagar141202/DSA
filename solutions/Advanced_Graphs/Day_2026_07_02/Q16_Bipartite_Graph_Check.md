# Bipartite Graph Check

## Problem Statement
Given an undirected graph, check if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. The graph is represented as an adjacency list. The function should return true if the graph is bipartite, false otherwise. The graph can have at most 100 nodes and 500 edges. For example, a graph with edges (1,2), (1,3), (2,4), (3,4) is bipartite, while a graph with edges (1,2), (2,3), (3,1) is not.

## Approach
To solve this problem, we can use a graph traversal algorithm such as BFS or DFS, and try to assign each node to one of two colors. If we encounter a node that is already assigned the same color as its neighbor, we return false. Otherwise, we return true.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isBipartite(vector<vector<int>>& graph) {
    vector<int> color(graph.size(), -1);
    
    for (int i = 0; i < graph.size(); i++) {
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
        u--, v--;
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
1 2
1 3
2 4
3 4
Output: true

Input: 
3 3
1 2
2 3
3 1
Output: false
```

## Key Takeaways
- We use a queue to perform BFS traversal of the graph.
- We assign each node a color (0 or 1) and check if any of its neighbors have the same color.
- If a node has a neighbor with the same color, we return false, indicating that the graph is not bipartite.