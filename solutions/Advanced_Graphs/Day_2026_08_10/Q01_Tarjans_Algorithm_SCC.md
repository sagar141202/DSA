# Tarjan's Algorithm (SCC)

## Problem Statement
Tarjan's algorithm is used to find Strongly Connected Components (SCCs) in a directed graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The problem statement is to find all SCCs in a given directed graph. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The algorithm should return a list of lists, where each sublist contains the vertices of an SCC.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to traverse the graph and find SCCs. It maintains a stack of vertices and assigns a low-link value to each vertex, which is the smallest index reachable from that vertex. The algorithm iterates through the graph, popping vertices from the stack when it finds an SCC.

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
    vector<vector<int>> sccs;
    int idx = 0;

    function<void(int)> strongconnect = [&](int node) {
        index[node] = idx;
        low[node] = idx;
        idx++;
        stack.push(node);
        onStack[node] = true;

        for (int neighbor : graph[node]) {
            if (index[neighbor] == -1) {
                strongconnect(neighbor);
                low[node] = min(low[node], low[neighbor]);
            } else if (onStack[neighbor]) {
                low[node] = min(low[node], index[neighbor]);
            }
        }

        if (low[node] == index[node]) {
            vector<int> scc;
            while (true) {
                int w = stack.top();
                stack.pop();
                onStack[w] = false;
                scc.push_back(w);
                if (w == node) break;
            }
            sccs.push_back(scc);
        }
    };

    for (int i = 0; i < n; i++) {
        if (index[i] == -1) strongconnect(i);
    }

    return sccs;
}

int main() {
    // Example usage
    vector<vector<int>> graph = {
        {1},
        {0, 2},
        {1, 3},
        {2}
    };

    vector<vector<int>> sccs = tarjanSCC(graph);
    for (const auto& scc : sccs) {
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
Input: graph = {
        {1},
        {0, 2},
        {1, 3},
        {2}
    }
Output: 
0 1 2 3 
```

## Key Takeaways
- Tarjan's algorithm uses DFS to find SCCs in a directed graph.
- The algorithm maintains a stack of vertices and assigns a low-link value to each vertex.
- The time complexity of Tarjan's algorithm is O(V + E), where V is the number of vertices and E is the number of edges.