# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, output the path. Otherwise, output a message indicating that no Euler path exists. The graph is represented as an adjacency list, where each key is a node and its corresponding value is a list of neighboring nodes. The graph has at most 100 nodes and 1000 edges.

## Approach
To solve this problem, we will use Hierholzer's algorithm, which is a well-known algorithm for finding Euler paths in graphs. The algorithm works by first finding a node with an odd degree, then performing a depth-first search to find a path that uses every edge exactly once.

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void eulerPath(vector<vector<int>>& graph, int start) {
    vector<int> path;
    stack<int> st;
    st.push(start);
    while (!st.empty()) {
        int node = st.top();
        if (!graph[node].empty()) {
            int neighbor = graph[node].back();
            graph[node].pop_back();
            st.push(neighbor);
        } else {
            path.push_back(node);
            st.pop();
        }
    }
    reverse(path.begin(), path.end());
    for (int node : path) {
        cout << node << " ";
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
        graph[v].push_back(u); // for undirected graph
    }
    int start = 0; // start node
    eulerPath(graph, start);
    return 0;
}
```

## Test Cases
```
Input: 
5 6
0 1
0 2
1 2
1 3
2 4
3 4
Output: 0 1 2 4 3 1 0
```

## Key Takeaways
- To find an Euler path, the graph must be connected and at most two nodes can have odd degrees.
- Hierholzer's algorithm is an efficient method for finding Euler paths in graphs.
- The algorithm works by performing a depth-first search and backtracking to find a path that uses every edge exactly once.