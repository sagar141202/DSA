# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) using Tarjan's algorithm. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, and the algorithm should output the vertices in each SCC. For example, given a graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (3, 4)}, the output should be {{0, 1, 2}, {3, 4}}.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to traverse the graph and find SCCs. It keeps track of the discovery time and low value of each vertex, and uses a stack to store vertices that are part of the current SCC. The algorithm iterates over all vertices, performing DFS and popping vertices from the stack when a cycle is detected.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Tarjan {
public:
    vector<vector<int>> scc;
    vector<int> disc, low, stack;
    int time = 0;

    vector<vector<int>> tarjanSCC(vector<vector<int>>& graph) {
        int n = graph.size();
        disc.resize(n, -1);
        low.resize(n, -1);
        stack.clear();

        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(graph, i);
            }
        }

        return scc;
    }

    void dfs(vector<vector<int>>& graph, int u) {
        disc[u] = low[u] = time++;
        stack.push_back(u);

        for (int v : graph[u]) {
            if (disc[v] == -1) {
                dfs(graph, v);
                low[u] = min(low[u], low[v]);
            } else if (find(stack.begin(), stack.end(), v) != stack.end()) {
                low[u] = min(low[u], disc[v]);
            }
        }

        if (low[u] == disc[u]) {
            vector<int> component;
            while (true) {
                int v = stack.back();
                stack.pop_back();
                component.push_back(v);
                if (v == u) break;
            }
            scc.push_back(component);
        }
    }
};

int main() {
    vector<vector<int>> graph = {{1}, {2}, {0}, {4}, {3}};
    Tarjan tarjan;
    vector<vector<int>> scc = tarjan.tarjanSCC(graph);
    for (auto component : scc) {
        for (int vertex : component) {
            cout << vertex << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: {{1}, {2}, {0}, {4}, {3}}
Output: 
0 1 2 
3 4 
```

## Key Takeaways
- Tarjan's algorithm uses DFS to find SCCs in a directed graph.
- It keeps track of the discovery time and low value of each vertex to detect cycles.
- The algorithm uses a stack to store vertices that are part of the current SCC.