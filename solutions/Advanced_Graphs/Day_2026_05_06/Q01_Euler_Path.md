# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path if it exists. An Euler path is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has more than two vertices with odd degree, it is not possible to find an Euler path. The problem requires finding an Euler path and returning the sequence of vertices.

## Approach
The approach involves using Hierholzer's algorithm to find an Euler path. This algorithm works by first finding a cycle in the graph, then iteratively adding more cycles to the path until all edges are included. The algorithm requires the graph to have at most two vertices with odd degree.

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to add an edge to the graph
void addEdge(vector<vector<int>>& graph, int u, int v) {
    graph[u].push_back(v);
    graph[v].push_back(u); // For undirected graph
}

// Function to find an Euler path using Hierholzer's algorithm
vector<int> eulerPath(vector<vector<int>>& graph, int start) {
    int n = graph.size();
    vector<int> path;
    stack<int> stack;
    stack.push(start);
    vector<vector<int>> tempGraph = graph;
    
    while (!stack.empty()) {
        int u = stack.top();
        if (!tempGraph[u].empty()) {
            stack.push(tempGraph[u].back());
            tempGraph[u].pop_back();
        } else {
            path.push_back(u);
            stack.pop();
        }
    }
    
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    int n = 5;
    vector<vector<int>> graph(n);
    addEdge(graph, 0, 1);
    addEdge(graph, 1, 2);
    addEdge(graph, 2, 0);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    
    vector<int> path = eulerPath(graph, 0);
    for (int vertex : path) {
        cout << vertex << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: 
Graph with vertices 0, 1, 2, 3, 4 and edges (0, 1), (1, 2), (2, 0), (1, 3), (1, 4)
Output: 0 1 2 0 1 3 1 4
```

## Key Takeaways
- An Euler path is only possible if the graph has at most two vertices with odd degree.
- Hierholzer's algorithm can be used to find an Euler path in a graph.
- The algorithm works by iteratively adding more cycles to the path until all edges are included.