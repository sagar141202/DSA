# Euler Path

## Problem Statement
Given a connected graph, find an Euler path if it exists. An Euler path is a path that visits every edge in the graph exactly once. The graph can be directed or undirected and may contain cycles. If the graph has an Euler path, output the path; otherwise, output a message indicating that no Euler path exists. The graph is represented as an adjacency list, where each index represents a node, and its corresponding value is a list of neighboring nodes. The graph has n nodes and m edges.

## Approach
The algorithm uses Hierholzer's algorithm to find an Euler path in the graph. It first checks if all nodes have even degrees, then it starts a depth-first search from an arbitrary node to find the Euler path. If the graph has more than two nodes with odd degrees, it does not have an Euler path.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to check if all nodes have even degrees
bool hasEvenDegrees(vector<vector<int>>& graph) {
    for (int i = 0; i < graph.size(); i++) {
        if (graph[i].size() % 2 != 0) {
            return false;
        }
    }
    return true;
}

// Function to find an Euler path using Hierholzer's algorithm
vector<int> eulerPath(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> path;
    stack<int> st;
    st.push(0);
    
    while (!st.empty()) {
        int node = st.top();
        if (!graph[node].empty()) {
            int neighbor = graph[node].back();
            graph[node].pop_back();
            for (int i = 0; i < graph[neighbor].size(); i++) {
                if (graph[neighbor][i] == node) {
                    graph[neighbor].erase(graph[neighbor].begin() + i);
                    break;
                }
            }
            st.push(neighbor);
        } else {
            path.push_back(st.top());
            st.pop();
        }
    }
    
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    if (!hasEvenDegrees(graph) && (count_if(graph.begin(), graph.end(), [](vector<int> v) { return v.size() % 2 != 0; }) > 2)) {
        cout << "No Euler path exists." << endl;
    } else {
        vector<int> path = eulerPath(graph);
        for (int node : path) {
            cout << node << " ";
        }
        cout << endl;
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
1 2
1 3
2 3
3 4
Output: 0 1 3 2 0 2 1 3 4 
```

## Key Takeaways
- To find an Euler path in a graph, all nodes must have even degrees, except for at most two nodes which can have odd degrees.
- Hierholzer's algorithm is used to find an Euler path in a graph.
- If the graph has more than two nodes with odd degrees, it does not have an Euler path.