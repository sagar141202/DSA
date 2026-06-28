# Articulation Points

## Problem Statement
Given an undirected graph, find all the articulation points in the graph. An articulation point is a node in the graph that, when removed, increases the number of connected components in the graph. The graph can have up to 10^5 nodes and 10^5 edges. The nodes are numbered from 1 to n, where n is the number of nodes. The input is an adjacency list representation of the graph.

## Approach
The approach is to use Depth-First Search (DFS) to traverse the graph and identify articulation points. We use a recursive function to perform DFS and keep track of the discovery time and low value of each node. If the node is an articulation point, it will have a low value greater than or equal to its discovery time, or it will be the root node with at least two children.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> graph;
vector<bool> visited;
vector<bool> ap;
vector<int> disc;
vector<int> low;
int time = 0;

void dfs(int u, int parent) {
    visited[u] = true;
    disc[u] = low[u] = time++;
    int child = 0;
    for (int v : graph[u]) {
        if (!visited[v]) {
            child++;
            dfs(v, u);
            low[u] = min(low[u], low[v]);
            if (parent == -1 && child > 1) {
                ap[u] = true;
            } else if (parent != -1 && low[v] >= disc[u]) {
                ap[u] = true;
            }
        } else if (v != parent) {
            low[u] = min(low[u], disc[v]);
        }
    }
}

void findArticulationPoints(int n, vector<vector<int>> &edges) {
    graph.resize(n);
    visited.resize(n, false);
    ap.resize(n, false);
    disc.resize(n, -1);
    low.resize(n, -1);
    for (auto &edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, -1);
        }
    }
    for (int i = 0; i < n; i++) {
        if (ap[i]) {
            cout << i << " ";
        }
    }
}

int main() {
    int n;
    cin >> n;
    int m;
    cin >> m;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }
    findArticulationPoints(n, edges);
    return 0;
}
```

## Test Cases
```
Input:
5
6
0 1
1 2
2 0
1 3
1 4
4 3
Output:
1 4
```

## Key Takeaways
- Articulation points are nodes that increase the number of connected components when removed.
- DFS is used to find articulation points by keeping track of discovery time and low value of each node.
- The algorithm has a time complexity of O(V + E) and a space complexity of O(V).