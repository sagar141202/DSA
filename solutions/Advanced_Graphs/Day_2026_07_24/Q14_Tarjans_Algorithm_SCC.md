# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, and the task is to identify all SCCs and output the vertices in each component. For example, consider a graph with vertices {1, 2, 3, 4, 5} and edges {(1, 2), (2, 3), (3, 1), (4, 5)}. The SCCs in this graph are {1, 2, 3} and {4, 5}.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to traverse the graph and identify SCCs. It maintains a stack of vertices and assigns a low-link value to each vertex, which represents the smallest index reachable from the vertex. The algorithm iteratively pops vertices from the stack and adds them to the current SCC if their low-link value matches the current index.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Tarjan {
public:
    vector<vector<int>> scc(const vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> index(n, -1), low(n, -1);
        vector<bool> onStack(n, false);
        vector<vector<int>> sccs;
        stack<int> stack;

        int idx = 0;
        for (int i = 0; i < n; ++i) {
            if (index[i] == -1) {
                strongConnect(i, graph, index, low, onStack, stack, sccs, idx);
            }
        }

        return sccs;
    }

private:
    void strongConnect(int v, const vector<vector<int>>& graph, vector<int>& index, vector<int>& low, vector<bool>& onStack, stack<int>& stack, vector<vector<int>>& sccs, int& idx) {
        index[v] = idx;
        low[v] = idx;
        idx++;
        stack.push(v);
        onStack[v] = true;

        for (int w : graph[v]) {
            if (index[w] == -1) {
                strongConnect(w, graph, index, low, onStack, stack, sccs, idx);
                low[v] = min(low[v], low[w]);
            } else if (onStack[w]) {
                low[v] = min(low[v], index[w]);
            }
        }

        if (low[v] == index[v]) {
            vector<int> scc;
            while (true) {
                int w = stack.top();
                stack.pop();
                onStack[w] = false;
                scc.push_back(w);
                if (w == v) break;
            }
            sccs.push_back(scc);
        }
    }
};

int main() {
    vector<vector<int>> graph = {{1}, {2}, {0}, {4}, {3}};
    Tarjan tarjan;
    vector<vector<int>> sccs = tarjan.scc(graph);
    for (const auto& scc : sccs) {
        for (int v : scc) {
            cout << v << " ";
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
- Tarjan's algorithm uses DFS to identify SCCs in a directed graph.
- The algorithm maintains a stack of vertices and assigns a low-link value to each vertex.
- The low-link value represents the smallest index reachable from a vertex, which helps identify SCCs.