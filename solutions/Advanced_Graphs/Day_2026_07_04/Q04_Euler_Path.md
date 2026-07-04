# Euler Path

## Problem Statement
Given a connected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph can be directed or undirected, and it may contain cycles. The path should start and end at any node. If the graph does not have an Euler path, return a message indicating that it's not possible. For example, consider a graph with nodes A, B, C, and D, and edges (A, B), (B, C), (C, D), and (D, A). An Euler path for this graph would be A -> B -> C -> D -> A.

## Approach
The approach to solve this problem is to use Hierholzer's algorithm, which states that a graph has an Euler path if and only if at most two nodes have odd degrees. The algorithm works by first finding a node with an odd degree, then traversing the graph using depth-first search (DFS) until we reach a node with no more edges to traverse.

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Graph {
public:
    int V;
    vector<vector<int>> adj;

    Graph(int vertices) {
        V = vertices;
        adj.resize(V);
    }

    void addEdge(int u, int v) {
        adj[u].push_back(v);
    }

    vector<int> eulerPath() {
        vector<int> path;
        stack<int> stack;
        int start = 0;

        // Find a node with an odd degree
        for (int i = 0; i < V; i++) {
            if (adj[i].size() % 2 != 0) {
                start = i;
                break;
            }
        }

        stack.push(start);

        while (!stack.empty()) {
            int node = stack.top();
            if (!adj[node].empty()) {
                stack.push(adj[node].back());
                adj[node].pop_back();
            } else {
                path.push_back(stack.top());
                stack.pop();
            }
        }

        reverse(path.begin(), path.end());
        return path;
    }
};

int main() {
    Graph graph(4);
    graph.addEdge(0, 1);
    graph.addEdge(1, 2);
    graph.addEdge(2, 3);
    graph.addEdge(3, 0);

    vector<int> path = graph.eulerPath();

    for (int node : path) {
        cout << node << " ";
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with nodes 0, 1, 2, 3 and edges (0, 1), (1, 2), (2, 3), (3, 0)
Output: 
0 1 2 3 0
```

## Key Takeaways
- An Euler path visits every edge in a graph exactly once.
- Hierholzer's algorithm is used to find an Euler path in a graph.
- A graph has an Euler path if and only if at most two nodes have odd degrees.