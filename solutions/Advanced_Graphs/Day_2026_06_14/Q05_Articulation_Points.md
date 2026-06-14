# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a vertex that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of adjacent vertices. The function should return a list of articulation points. For example, in a graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (1, 3), (1, 4)}, the articulation points are {1}.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points by checking if the removal of a vertex increases the number of connected components. We maintain a timer to keep track of the discovery time and low value of each vertex. If a vertex is an articulation point, it must have at least two children, and for each child, the low value of the child must be greater than or equal to the discovery time of the vertex.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> articulationPoints(int n, vector<vector<int>>& connections) {
    vector<vector<int>> graph(n);
    for (auto& connection : connections) {
        graph[connection[0]].push_back(connection[1]);
        graph[connection[1]].push_back(connection[0]);
    }

    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> ap(n, false);
    vector<int> parent(n, -1);
    int time = 0;

    function<void(int)> dfs = [&](int u) {
        disc[u] = low[u] = time++;
        int child = 0;
        for (int v : graph[u]) {
            if (disc[v] == -1) {
                parent[v] = u;
                child++;
                dfs(v);
                low[u] = min(low[u], low[v]);
                if (parent[u] == -1 && child > 1) {
                    ap[u] = true;
                }
                if (parent[u] != -1 && low[v] >= disc[u]) {
                    ap[u] = true;
                }
            } else if (v != parent[u]) {
                low[u] = min(low[u], disc[v]);
            }
        }
    };

    for (int i = 0; i < n; i++) {
        if (disc[i] == -1) {
            dfs(i);
        }
    }

    vector<int> result;
    for (int i = 0; i < n; i++) {
        if (ap[i]) {
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    int n = 5;
    vector<vector<int>> connections = {{0, 1}, {1, 2}, {2, 0}, {1, 3}, {1, 4}};
    vector<int> result = articulationPoints(n, connections);
    for (int i : result) {
        cout << i << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: n = 5, connections = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4]]
Output: [1]
```

## Key Takeaways
- Articulation points are vertices that, when removed, increase the number of connected components in a graph.
- The algorithm uses DFS to traverse the graph and identify articulation points based on their discovery time and low value.
- A vertex is an articulation point if it has at least two children and the low value of each child is greater than or equal to the discovery time of the vertex.