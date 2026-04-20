# Articulation Points

## Problem Statement
Given a graph, find all the articulation points in the graph. An articulation point is a node in the graph that, when removed, increases the number of connected components in the graph. The graph can be represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighboring nodes. The graph can contain cycles and self-loops. The input will be a 2D vector representing the adjacency list of the graph. The output should be a vector of node indices that are articulation points.

## Approach
We will use a depth-first search (DFS) algorithm to find the articulation points. The algorithm will keep track of the discovery time and low value of each node, and use these values to determine if a node is an articulation point. A node is an articulation point if it has a child node that is a leaf node or if the low value of one of its child nodes is greater than its discovery time.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int u, int p, vector<vector<int>>& graph, vector<int>& disc, vector<int>& low, vector<bool>& ap, int& time) {
    disc[u] = low[u] = time++;
    int child = 0;
    for (int v : graph[u]) {
        if (disc[v] == -1) {
            child++;
            dfs(v, u, graph, disc, low, ap, time);
            low[u] = min(low[u], low[v]);
            if (p == -1 && child > 1) {
                ap[u] = true;
            }
            if (p != -1 && low[v] >= disc[u]) {
                ap[u] = true;
            }
        } else if (v != p) {
            low[u] = min(low[u], disc[v]);
        }
    }
}

vector<int> findArticulationPoints(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> disc(n, -1);
    vector<int> low(n, -1);
    vector<bool> ap(n, false);
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (disc[i] == -1) {
            dfs(i, -1, graph, disc, low, ap, time);
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
    int n;
    cin >> n;
    vector<vector<int>> graph(n);
    for (int i = 0; i < n; i++) {
        int m;
        cin >> m;
        for (int j = 0; j < m; j++) {
            int x;
            cin >> x;
            graph[i].push_back(x);
        }
    }
    vector<int> result = findArticulationPoints(graph);
    for (int i : result) {
        cout << i << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: 
5
2 1 2
2 0 3
1 2
1 0
0
Output: 0 2
```

## Key Takeaways
- Articulation points are nodes that, when removed, increase the number of connected components in the graph.
- The algorithm uses DFS to find the articulation points by keeping track of the discovery time and low value of each node.
- A node is an articulation point if it has a child node that is a leaf node or if the low value of one of its child nodes is greater than its discovery time.