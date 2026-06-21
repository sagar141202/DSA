# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) using Tarjan's algorithm. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The input graph is represented as an adjacency list, and the output should be a list of lists, where each inner list contains the vertices of an SCC. The graph can have up to 10^5 vertices and 10^5 edges.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to find SCCs. It assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm then uses this information to identify the roots of SCCs and their corresponding components.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> tarjanSCC(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> index(n, -1), low(n, -1);
    vector<bool> onStack(n, false);
    stack<int> stack;
    vector<vector<int>> scc;
    int idx = 0;

    function<void(int)> dfs = [&](int v) {
        index[v] = low[v] = idx++;
        stack.push(v);
        onStack[v] = true;

        for (int u : graph[v]) {
            if (index[u] == -1) {
                dfs(u);
                low[v] = min(low[v], low[u]);
            } else if (onStack[u]) {
                low[v] = min(low[v], index[u]);
            }
        }

        if (low[v] == index[v]) {
            vector<int> component;
            while (true) {
                int u = stack.top();
                stack.pop();
                onStack[u] = false;
                component.push_back(u);
                if (u == v) break;
            }
            scc.push_back(component);
        }
    };

    for (int i = 0; i < n; i++) {
        if (index[i] == -1) dfs(i);
    }

    return scc;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
    }

    vector<vector<int>> scc = tarjanSCC(graph);

    for (const auto& component : scc) {
        for (int v : component) {
            cout << v << " ";
        }
        cout << endl;
    }

    return 0;
}
```

## Test Cases
```
Input:
5 5
0 1
1 2
2 0
1 3
3 4
Output:
0 2 1 
3 
4 
```

## Key Takeaways
- Tarjan's algorithm uses a single DFS pass to find all SCCs in a directed graph.
- The algorithm assigns a unique index to each vertex and keeps track of the lowest reachable index to identify the roots of SCCs.
- The time complexity of Tarjan's algorithm is O(V + E), making it efficient for large graphs.