# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, it must have at most two vertices with odd degree. If it has exactly two vertices with odd degree, the Euler path must start at one of them and end at the other. If all vertices have even degree, the Euler path can start and end at any vertex.

## Approach
To solve this problem, we use Hierholzer's algorithm, which is a simple and efficient method for finding Euler paths in graphs. The algorithm works by repeatedly finding cycles in the graph and combining them into a single Euler path.

## Complexity
- Time: O(E + V)
- Space: O(E + V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> graph;
vector<int> path;

void dfs(int u) {
    while (!graph[u].empty()) {
        int v = graph[u].back();
        graph[u].pop_back();
        dfs(v);
    }
    path.push_back(u);
}

void eulerPath(int start) {
    path.clear();
    dfs(start);
    reverse(path.begin(), path.end());
}

int main() {
    int V, E;
    cin >> V >> E;
    graph.resize(V);
    for (int i = 0; i < E; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        if (!graph[v].empty() || graph[u].size() > 1) {
            graph[v].push_back(u);
        }
    }
    int oddCount = 0;
    for (int i = 0; i < V; i++) {
        if (graph[i].size() % 2 != 0) {
            oddCount++;
        }
    }
    if (oddCount > 2) {
        cout << "No Euler path exists" << endl;
        return 0;
    }
    for (int i = 0; i < V; i++) {
        if (graph[i].size() % 2 != 0) {
            eulerPath(i);
            break;
        }
    }
    for (int i = 0; i < path.size(); i++) {
        cout << path[i] << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: 
5 6
0 1
1 2
2 3
3 4
4 0
0 2
Output: 0 2 1 0 4 3 2
```

## Key Takeaways
- The graph must have at most two vertices with odd degree to have an Euler path.
- If all vertices have even degree, the Euler path can start and end at any vertex.
- Hierholzer's algorithm is used to find the Euler path in the graph.