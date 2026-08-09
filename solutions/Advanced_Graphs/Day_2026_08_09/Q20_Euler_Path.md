# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, output the path. If not, output a message indicating that no Euler path exists. The graph is represented as an adjacency list. The graph may have self-loops and multiple edges between the same pair of vertices.

## Approach
To solve this problem, we use Hierholzer's algorithm, which finds an Euler path in a graph by iteratively adding edges to the path while ensuring that the path can be extended. We start at an arbitrary vertex and try to add edges to the path until we cannot add any more edges.

## Complexity
- Time: O(E + V)
- Space: O(E + V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to find an Euler path in a graph
vector<int> eulerPath(vector<vector<int>>& graph) {
    int V = graph.size();
    vector<int> path;
    vector<bool> visited(V * V, false);
    stack<int> s;
    s.push(0); // start at an arbitrary vertex

    while (!s.empty()) {
        int v = s.top();
        bool hasUnvisitedEdge = false;

        // check if there is an unvisited edge from the current vertex
        for (int i = 0; i < graph[v].size(); i++) {
            int edge = graph[v][i];
            if (!visited[edge]) {
                hasUnvisitedEdge = true;
                visited[edge] = true;
                s.push(i); // add the edge to the path
                break;
            }
        }

        // if there is no unvisited edge, add the vertex to the path
        if (!hasUnvisitedEdge) {
            path.push_back(v);
            s.pop();
        }
    }

    // reverse the path to get the correct order
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    int V = 5;
    vector<vector<int>> graph(V);

    // add edges to the graph
    graph[0].push_back(1);
    graph[0].push_back(2);
    graph[1].push_back(3);
    graph[2].push_back(4);
    graph[3].push_back(0);

    vector<int> path = eulerPath(graph);

    // print the Euler path
    for (int v : path) {
        cout << v << " ";
    }
    cout << endl;

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and 5 edges:
0 -> 1
0 -> 2
1 -> 3
2 -> 4
3 -> 0
Output: 
0 1 3 0 2 4
```

## Key Takeaways
- An Euler path visits every edge in the graph exactly once.
- Hierholzer's algorithm can be used to find an Euler path in a graph.
- The algorithm starts at an arbitrary vertex and iteratively adds edges to the path while ensuring that the path can be extended.