# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, and the function should return a list of lists, where each inner list contains the vertices of an SCC. The graph has n vertices and m edges. The function should handle graphs with self-loops and parallel edges.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to find SCCs. It assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm then groups vertices with the same lowest reachable index into an SCC.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> tarjanSCC(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> index(n, -1);
    vector<int> low(n, -1);
    vector<bool> onStack(n, false);
    stack<int> stack;
    vector<vector<int>> result;
    int idx = 0;

    function<void(int)> strongConnect = [&](int u) {
        index[u] = idx;
        low[u] = idx;
        idx++;
        stack.push(u);
        onStack[u] = true;

        for (int v : graph[u]) {
            if (index[v] == -1) {
                strongConnect(v);
                low[u] = min(low[u], low[v]);
            } else if (onStack[v]) {
                low[u] = min(low[u], index[v]);
            }
        }

        if (low[u] == index[u]) {
            vector<int> component;
            while (true) {
                int v = stack.top();
                stack.pop();
                onStack[v] = false;
                component.push_back(v);
                if (v == u) break;
            }
            result.push_back(component);
        }
    };

    for (int i = 0; i < n; i++) {
        if (index[i] == -1) {
            strongConnect(i);
        }
    }

    return result;
}

int main() {
    // Example usage:
    int n = 5;
    vector<vector<int>> graph(n);
    graph[0].push_back(1);
    graph[1].push_back(2);
    graph[2].push_back(0);
    graph[2].push_back(3);
    graph[3].push_back(4);

    vector<vector<int>> sccs = tarjanSCC(graph);
    for (const auto& scc : sccs) {
        cout << "SCC: ";
        for (int vertex : scc) {
            cout << vertex << " ";
        }
        cout << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and 5 edges:
0 -> 1
1 -> 2
2 -> 0
2 -> 3
3 -> 4

Output: 
SCC: 0 1 2 
SCC: 3 
SCC: 4 
```

## Key Takeaways
- Tarjan's algorithm is an efficient method for finding strongly connected components in a directed graph.
- The algorithm uses a recursive DFS approach to assign a unique index to each vertex and group vertices with the same lowest reachable index into an SCC.
- The time complexity of Tarjan's algorithm is O(V + E), making it suitable for large graphs.