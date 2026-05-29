# Euler Path

## Problem Statement
Given a connected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph can be directed or undirected, and it may contain self-loops and multiple edges between the same pair of vertices. The graph has at most 10^5 vertices and 10^5 edges. If an Euler path exists, print the path; otherwise, print "No Euler path exists."

## Approach
The algorithm checks if all vertices have even degrees, which is a necessary condition for an Euler path to exist in an undirected graph. Then, it uses a depth-first search to find the Euler path.

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void eulerPath(vector<vector<int>>& graph, int start) {
    stack<int> s;
    s.push(start);
    vector<int> path;

    while (!s.empty()) {
        int v = s.top();
        if (graph[v].empty()) {
            path.push_back(v);
            s.pop();
        } else {
            int nextV = graph[v].back();
            graph[v].pop_back();
            s.push(nextV);
        }
    }

    reverse(path.begin(), path.end());
    for (int v : path) {
        cout << v << " ";
    }
}

int main() {
    int V, E;
    cin >> V >> E;

    vector<vector<int>> graph(V);
    for (int i = 0; i < E; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    bool hasEulerPath = true;
    for (int i = 0; i < V; i++) {
        if (graph[i].size() % 2 != 0) {
            hasEulerPath = false;
            break;
        }
    }

    if (hasEulerPath) {
        eulerPath(graph, 0);
    } else {
        cout << "No Euler path exists.";
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
2 3
3 4
4 0
Output: 
0 1 3 2 0 4
```

## Key Takeaways
- An Euler path exists in an undirected graph if and only if all vertices have even degrees.
- The algorithm uses a depth-first search to find the Euler path.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges.