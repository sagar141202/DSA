# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a vertex that, when removed, increases the number of connected components in the graph. The graph can have up to 10^5 vertices and 10^5 edges. The vertices are numbered from 1 to n, where n is the number of vertices. The edges are represented as pairs of vertex numbers.

## Approach
We will use Depth-First Search (DFS) to find the articulation points. The algorithm works by maintaining a timer for the discovery time of each vertex and the low value, which is the smallest discovery time reachable from the current vertex. If the current vertex is a cut vertex (articulation point), then the low value of one of its neighbors will be greater than or equal to its discovery time.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void findArticulationPoints(vector<vector<int>>& graph, int vertex, bool& visited, vector<bool>& ap, vector<int>& disc, vector<int>& low, int& time, int parent) {
    visited[vertex] = true;
    disc[vertex] = low[vertex] = time++;
    int children = 0;

    for (int neighbor : graph[vertex]) {
        if (!visited[neighbor]) {
            children++;
            findArticulationPoints(graph, neighbor, visited, ap, disc, low, time, vertex);
            low[vertex] = min(low[vertex], low[neighbor]);

            // Check if the vertex is an articulation point
            if (parent == -1 && children > 1) {
                ap[vertex] = true;
            } else if (parent != -1 && low[neighbor] >= disc[vertex]) {
                ap[vertex] = true;
            }
        } else if (neighbor != parent) {
            low[vertex] = min(low[vertex], disc[neighbor]);
        }
    }
}

void findArticulationPoints(vector<vector<int>>& graph, int n) {
    vector<bool> visited(n, false);
    vector<bool> ap(n, false);
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    int time = 0;

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            findArticulationPoints(graph, i, visited, ap, disc, low, time, -1);
        }
    }

    // Print the articulation points
    for (int i = 0; i < n; i++) {
        if (ap[i]) {
            cout << i + 1 << " ";
        }
    }
    cout << endl;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--; // 0-based indexing
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    findArticulationPoints(graph, n);
    return 0;
}
```

## Test Cases
```
Input: 
5 5
1 2
2 3
1 3
3 4
4 5

Output: 
3 4
```

## Key Takeaways
- Use DFS to find articulation points in an undirected graph.
- Maintain a timer for the discovery time of each vertex and the low value to determine if a vertex is an articulation point.
- Check for articulation points by considering the parent vertex and the low value of its neighbors.