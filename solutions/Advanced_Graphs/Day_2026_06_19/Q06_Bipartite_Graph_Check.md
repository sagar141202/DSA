# Bipartite Graph Check

## Problem Statement
Given an undirected graph, determine if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. The graph is represented as an adjacency list. The function should return true if the graph is bipartite, and false otherwise. The graph can have at most 100 nodes and 1000 edges. For example, a graph with edges (1,2), (1,3), (2,4), (3,4) is bipartite because we can divide the nodes into two sets {1,4} and {2,3}.

## Approach
We will use a breadth-first search (BFS) traversal to assign each node a color (0 or 1) and check if any adjacent nodes have the same color. If we find any adjacent nodes with the same color, we immediately return false. If we finish the traversal without finding any such nodes, we return true.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isBipartite(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> color(n, -1); // -1: not colored, 0: color 0, 1: color 1

    for (int i = 0; i < n; i++) {
        if (color[i] == -1) { // if node is not colored
            queue<int> q;
            q.push(i);
            color[i] = 0; // assign color 0 to this node

            while (!q.empty()) {
                int node = q.front();
                q.pop();

                for (int neighbor : graph[node]) {
                    if (color[neighbor] == -1) { // if neighbor is not colored
                        q.push(neighbor);
                        color[neighbor] = 1 - color[node]; // assign opposite color to neighbor
                    } else if (color[neighbor] == color[node]) { // if neighbor has same color
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
        u--, v--; // 0-based indexing
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
4 4
1 2
2 3
3 4
4 1
Output: false
```

## Key Takeaways
- A bipartite graph can be checked using BFS traversal and coloring nodes with two colors.
- If any two adjacent nodes have the same color, the graph is not bipartite.
- The time complexity of this solution is O(V + E), where V is the number of vertices and E is the number of edges.