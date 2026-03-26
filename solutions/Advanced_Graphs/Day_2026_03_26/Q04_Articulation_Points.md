# Articulation Points

## Problem Statement
Given an undirected graph, find all articulation points in the graph. An articulation point is a node that, when removed, increases the number of connected components in the graph. The graph is represented as an adjacency list, and the nodes are numbered from 1 to n. The input consists of the number of nodes (n) and the number of edges (m), followed by m pairs of nodes representing the edges. The output should be a list of all articulation points in the graph.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and identify articulation points. It keeps track of the discovery time and low value of each node to determine if a node is an articulation point. A node is an articulation point if it has at least two children and the low value of one of its children is greater than or equal to its discovery time.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int node, int parent, vector<vector<int>>& graph, vector<bool>& visited, vector<int>& disc, vector<int>& low, vector<bool>& ap, int& time) {
    visited[node] = true;
    disc[node] = low[node] = time++;
    int children = 0;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            children++;
            dfs(neighbor, node, graph, visited, disc, low, ap, time);
            low[node] = min(low[node], low[neighbor]);
            if (parent != -1 && low[neighbor] >= disc[node]) {
                ap[node] = true;
            }
        } else if (neighbor != parent) {
            low[node] = min(low[node], disc[neighbor]);
        }
    }
    if (parent == -1 && children > 1) {
        ap[node] = true;
    }
}

vector<int> findArticulationPoints(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    vector<bool> visited(n, false);
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> ap(n, false);
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1, graph, visited, disc, low, ap, time);
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
    int n, m;
    cin >> n >> m;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1];
        edges[i][0]--;
        edges[i][1]--;
    }
    vector<int> articulationPoints = findArticulationPoints(n, edges);
    for (int point : articulationPoints) {
        cout << point + 1 << " ";
    }
    cout << endl;
    return 0;
}
```

## Test Cases
```
Input: 
5 5
1 2
2 3
3 4
4 5
1 5
Output: 
1 4 
```

## Key Takeaways
- Articulation points are nodes that, when removed, increase the number of connected components in the graph.
- The algorithm uses DFS to traverse the graph and identify articulation points based on the discovery time and low value of each node.
- A node is an articulation point if it has at least two children and the low value of one of its children is greater than or equal to its discovery time.